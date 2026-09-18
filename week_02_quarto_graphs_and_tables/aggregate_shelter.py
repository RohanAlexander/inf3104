#### Preamble ####
# Purpose: Download Toronto's daily shelter occupancy data and aggregate it by date and sector
# Author: Rohan Alexander
# Date: 16 September 2026
# Contact: rohan.alexander@utoronto.ca
# License: MIT
# Pre-requisites: uv add polars
# Run: uv run 01-aggregate_shelter.py
# Output: data/shelter_daily.parquet, one row per date and sector

#### Workspace setup ####
import polars as pl
from pathlib import Path

Path("data").mkdir(exist_ok=True)

url = (
    "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/"
    "21c83b32-d5a8-4106-a54f-010dbe49f6f2/resource/"
    "ffd20867-6e3c-4074-8427-d63810edf231/download/"
    "Daily%20shelter%20overnight%20occupancy.csv"
)

#### Acquire ####
raw = pl.read_csv(url, infer_schema_length=10000)
raw.write_parquet("data/shelter_raw.parquet")

#### Clean and aggregate ####
daily = (
    raw.select(
        pl.col("OCCUPANCY_DATE").str.strptime(pl.Date, "%Y-%m-%d").alias("date"),
        pl.col("SECTOR").alias("sector"),
        pl.col("SERVICE_USER_COUNT").alias("service_users"),
        pl.col("OCCUPIED_BEDS").fill_null(0).alias("occupied_beds"),
        pl.col("CAPACITY_ACTUAL_BED").fill_null(0).alias("capacity_beds"),
        pl.col("OCCUPIED_ROOMS").fill_null(0).alias("occupied_rooms"),
        pl.col("CAPACITY_ACTUAL_ROOM").fill_null(0).alias("capacity_rooms"),
    )
    .group_by("date", "sector")
    .agg(pl.all().sum())
    .sort("date", "sector")
)

daily.write_parquet("data/shelter_daily.parquet")
print(daily.tail(5))
print(f"{daily.height} rows, {daily['date'].min()} to {daily['date'].max()}")
