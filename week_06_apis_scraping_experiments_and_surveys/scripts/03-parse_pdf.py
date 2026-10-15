#### Preamble ####
# Purpose: Turn Table 3.1 of the 1993 Kenya DHS final report into a dataset
# Author: Rohan Alexander
# Contact: rohan.alexander@utoronto.ca
# Pre-requisites: uv add requests pdfplumber polars; 00-simulate.py
# Source: https://dhsprogram.com/pubs/pdf/FR54/FR54.pdf

import re
from pathlib import Path

import pdfplumber
import polars as pl
import requests

URL = "https://dhsprogram.com/pubs/pdf/FR54/FR54.pdf"
HEADERS = {"User-Agent": "INF3104 class demonstration (rohan.alexander@utoronto.ca)"}
PDF = Path("inputs/kenya_dhs_1993_final_report.pdf")
PAGE = 47  # as a PDF viewer counts, not the number printed on the page

# 1. Get the PDF once and keep it in inputs
if not PDF.exists():
    response = requests.get(URL, headers=HEADERS, timeout=120)
    response.raise_for_status()
    PDF.write_bytes(response.content)

# 2. First parse: whatever the machine gives us, saved before we touch it.
#    This report is a scan that has already had OCR applied, so there is a
#    text layer, and it has errors. Look for "axe" and "yeaxs" in the note.
FIRST_PARSE = Path("data/raw/first_parse.txt")
if not FIRST_PARSE.exists():
    with pdfplumber.open(PDF) as pdf:
        FIRST_PARSE.write_text(pdf.pages[PAGE - 1].extract_text())

# Everything after this reads from the saved first parse
text = FIRST_PARSE.read_text()

# 3. Rebuild the table. A row of interest is an age group, then three
#    numbers, some of which are in parentheses.
pattern = re.compile(r"^(\d{2}-\d{2})\s+(\(?\d+\)?)\s+(\(?\d+\)?)\s+(\(?\d+\)?)\s*$")

rows = []
for line in text.splitlines():
    match = pattern.match(line.strip())
    if match:
        age_group, *values = match.groups()
        for residence, value in zip(["Urban", "Rural", "Total"], values):
            rows.append(
                {
                    "age_group": age_group,
                    "residence": residence,
                    "births_per_1000_women": int(value.strip("()")),
                    # The note to the table says that parentheses mean the
                    # rate is based on fewer than 250 woman-years of exposure.
                    # That is information, so it gets its own column.
                    "small_exposure": value.startswith("("),
                }
            )

fertility = pl.DataFrame(rows)

# 4. Tests. The first three come from the simulation. The last is a gift from
#    the table itself. The total fertility rate is five times the sum of the
#    age-specific rates, divided by 1,000, and the table reports it.
assert fertility.height == 21
assert fertility["age_group"].n_unique() == 7
assert fertility["births_per_1000_women"].is_between(0, 400).all()

reported_tfr = {"Urban": 3.44, "Rural": 5.80, "Total": 5.40}
for residence, reported in reported_tfr.items():
    rates = fertility.filter(pl.col("residence") == residence)["births_per_1000_women"]
    implied = 5 * rates.sum() / 1000
    assert abs(implied - reported) < 0.02, (residence, implied, reported)
    print(f"{residence}: implied TFR {implied:.3f}, reported {reported:.2f}")

fertility.write_parquet("data/kenya_1993_fertility.parquet")
print(fertility)
