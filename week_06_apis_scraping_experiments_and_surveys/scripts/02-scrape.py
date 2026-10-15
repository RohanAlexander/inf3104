#### Preamble ####
# Purpose: Scrape the table of Canadian prime ministers from Wikipedia
# Author: Rohan Alexander
# Contact: rohan.alexander@utoronto.ca
# Pre-requisites: uv add requests beautifulsoup4 polars
# Note: Wikipedia has an API, and for real work we would use that. We use
#   the page here because everyone can see it, and it is a realistic mess.

import re
from pathlib import Path

import polars as pl
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_prime_ministers_of_Canada"
HEADERS = {"User-Agent": "INF3104 class demonstration (rohan.alexander@utoronto.ca)"}
RAW = Path("data/raw/prime_ministers.html")

# 1. Get the page once, and save it. Everything after this reads from disk,
#    so that we do not go back to the website every time we fix our code.
if not RAW.exists():
    response = requests.get(URL, headers=HEADERS, timeout=30)
    response.raise_for_status()
    RAW.write_text(response.text, encoding="utf-8")

soup = BeautifulSoup(RAW.read_text(encoding="utf-8"), "html.parser")

# 2. Find what we want. Using "Inspect" in the browser, each prime minister's
#    name is a bold link inside a table with class "wikitable", and the life
#    span follows it in the same cell, as (1815-1891) or, if alive, (b. 1939).
#    The first table with that class turns out to be the key to the province
#    abbreviations, which returned nothing. We want the one with the most rows.
tables = soup.find_all("table", class_="wikitable")
table = max(tables, key=lambda t: len(t.find_all("tr")))

rows = []
for cell in table.find_all(["td", "th"]):
    bold_link = cell.select_one("b > a")
    span = re.search(r"\((?:b\.\s*)?(\d{4})(?:\s*[–-]\s*(\d{4}))?\s*\)", cell.get_text(" "))
    if bold_link and span:
        rows.append(
            {
                "name": bold_link.get_text(strip=True),
                "born": int(span.group(1)),
                "died": int(span.group(2)) if span.group(2) else None,
            }
        )

# Some prime ministers served more than once and so appear more than once
prime_ministers = pl.DataFrame(rows).unique(subset="name", maintain_order=True)

# 3. Test what came back. Websites change, and a scraper that silently
#    returns nothing is worse than one that fails.
assert prime_ministers.height >= 23, "Fewer prime ministers than there have been"
assert prime_ministers["name"][0] == "John A. Macdonald"
assert prime_ministers["born"].is_between(1800, 2000).all()
assert (prime_ministers.drop_nulls("died")["died"] > prime_ministers.drop_nulls("died")["born"]).all()

prime_ministers.write_parquet("data/prime_ministers.parquet")
print(prime_ministers)
