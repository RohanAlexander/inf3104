#### Preamble ####
# Purpose: Clean the 500 rows that the Open Data Toronto API gave us in Week 6
# Author: Rohan Alexander
# Contact: rohan.alexander@utoronto.ca
# Pre-requisites: 00-simulate.py; data/raw/shelter_latest_500.parquet

import polars as pl
from tests import test_shelter

raw = pl.read_parquet("data/raw/shelter_latest_500.parquet")
rows_at_start = raw.height

cleaned = (
    raw
    # Names: lower case, and ours
    .rename({c: c.lower() for c in raw.columns})
    .rename({"service_user_count": "service_users"})
    # Classes: the API gave us everything as a string
    .with_columns(
        pl.col("occupancy_date").str.to_date("%Y-%m-%d"),
        pl.col("service_users").cast(pl.Int64),
        pl.col(
            "capacity_actual_bed", "capacity_actual_room", "occupied_beds", "occupied_rooms"
        ).cast(pl.Int64),
        pl.col("occupancy_rate_beds", "occupancy_rate_rooms").cast(pl.Float64),
    )
    # Structure: capacity is measured in beds for some programs and rooms
    # for others, across two sets of columns, each empty when the other is
    # full. One thing, one column: say what the unit is, and then coalesce.
    .with_columns(
        pl.col("capacity_type")
        .replace_strict({"Bed Based Capacity": "bed", "Room Based Capacity": "room"})
        .alias("capacity_unit"),
        pl.coalesce("capacity_actual_bed", "capacity_actual_room").alias("capacity"),
        pl.coalesce("occupied_beds", "occupied_rooms").alias("occupied"),
        pl.coalesce("occupancy_rate_beds", "occupancy_rate_rooms").alias("occupancy_rate"),
    )
    .select(
        "occupancy_date",
        "program_id",
        "sector",
        "capacity_unit",
        "service_users",
        "capacity",
        "occupied",
        "occupancy_rate",
    )
)

# Count rows before and after
assert cleaned.height == rows_at_start

test_shelter(cleaned)

cleaned.write_parquet("data/cleaned_shelter.parquet")
print(cleaned.head())
