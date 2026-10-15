#### Preamble ####
# Purpose: Ask the Open Data Toronto API what files make up the shelter
#   occupancy dataset, then get the most recent rows through the API
# Author: Rohan Alexander
# Contact: rohan.alexander@utoronto.ca
# Pre-requisites: uv add requests polars python-dotenv

import json
import os
import time

import polars as pl
import requests
from dotenv import load_dotenv

# Open Data Toronto does not need a key, but most APIs do. The pattern is
# always that the key lives in a file called .env, which is in .gitignore,
# and the code only ever refers to it by name.
load_dotenv()
API_KEY = os.environ.get("EXAMPLE_API_KEY")  # None here, and that is fine

BASE_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action"
HEADERS = {"User-Agent": "INF3104 class demonstration (rohan.alexander@utoronto.ca)"}

# 1. What is in the dataset?
response = requests.get(
    f"{BASE_URL}/package_show",
    params={"id": "daily-shelter-overnight-service-occupancy-capacity"},
    headers=HEADERS,
    timeout=30,
)
response.raise_for_status()
package = response.json()

# Save exactly what came back before doing anything to it
with open("data/raw/package_show.json", "w") as f:
    json.dump(package, f, indent=2)

# Nested JSON to a rectangle: we decide that a row is a file
resources = pl.DataFrame(
    [
        {
            "name": r["name"],
            "format": r["format"],
            "in_datastore": r["datastore_active"],
            "last_modified": r["last_modified"],
            "id": r["id"],
        }
        for r in package["result"]["resources"]
    ]
)
resources.write_parquet("data/resources.parquet")
print(resources)

# 2. Get some rows. Be polite and pause between requests.
time.sleep(1)

current = resources.filter(pl.col("in_datastore")).row(0, named=True)
response = requests.get(
    f"{BASE_URL}/datastore_search",
    params={"resource_id": current["id"], "limit": 500, "sort": "_id desc"},
    headers=HEADERS,
    timeout=30,
)
response.raise_for_status()
records = response.json()["result"]["records"]

latest = pl.DataFrame(records, infer_schema_length=None)
assert latest.height == 500
assert "OCCUPANCY_DATE" in latest.columns

latest.write_parquet("data/shelter_latest_500.parquet")
print(latest.select(["OCCUPANCY_DATE", "SECTOR", "SERVICE_USER_COUNT"]).head())
