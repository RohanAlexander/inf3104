#### Preamble ####
# Purpose: Downloads the City of Toronto daily shelter occupancy data and saves it as parquet
# Author: Rohan Alexander
# Date: 9 September 2026
# Contact: rohan.alexander@utoronto.ca
# License: MIT
# Pre-requisites:
# - Add `polars`: uv add polars

#### Workspace setup ####
import polars as pl
from datetime import date

#### Download ####
url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/21c83b32-d5a8-4106-a54f-010dbe49f6f2/resource/ffd20867-6e3c-4074-8427-d63810edf231/download/Daily%20shelter%20overnight%20occupancy.csv"

df = pl.read_csv(url)

#### Save ####
# One dated file per run, so the repo keeps a history of what the city published each day
df.write_parquet(f"data/shelter_usage_{date.today().isoformat()}.parquet")

print(f"Saved {df.height} rows")
