#### Preamble ####
# Purpose: The tests that the analysis dataset must pass. They are written
#   once, here, and run against both the simulated and the real data.
# Author: Rohan Alexander
# Contact: rohan.alexander@utoronto.ca

import datetime

import polars as pl

SECTORS = ["Families", "Men", "Mixed Adult", "Women", "Youth"]
CAPACITY_UNITS = ["bed", "room"]

SCHEMA = {
    "occupancy_date": pl.Date,
    "program_id": pl.String,  # an identifier, not a number, so we will never add them up
    "sector": pl.String,
    "capacity_unit": pl.String,
    "service_users": pl.Int64,
    "capacity": pl.Int64,
    "occupied": pl.Int64,
    "occupancy_rate": pl.Float64,
}


def test_shelter(df: pl.DataFrame) -> None:
    # Class: every variable is there, and is the type that we planned
    assert dict(df.schema) == SCHEMA, dict(df.schema)

    # Content: every variable takes values that it could take
    assert df["occupancy_date"].is_between(datetime.date(2021, 1, 1), datetime.date.today()).all()
    assert df["program_id"].str.contains(r"^\d{5}$").all()
    assert df["sector"].is_in(SECTORS).all()
    assert df["capacity_unit"].is_in(CAPACITY_UNITS).all()
    assert (df["service_users"] >= 0).all()
    assert (df["capacity"] > 0).all()
    assert (df["occupied"] >= 0).all()
    assert df["occupancy_rate"].is_between(0, 100).all()

    # Nothing is missing: bed and room programs now share columns
    assert sum(df.null_count().row(0)) == 0

    # A row is a program on a night
    assert not df.select(pl.struct(["occupancy_date", "program_id"]).is_duplicated()).to_series().any()

    # Relationships: what we know about the world
    assert (df["occupied"] <= df["capacity"]).all()
    implied_rate = 100 * df["occupied"] / df["capacity"]
    assert ((implied_rate - df["occupancy_rate"]).abs() < 0.01).all()
    # A room can hold more than one person, a bed cannot
    beds = df.filter(pl.col("capacity_unit") == "bed")
    assert (beds["service_users"] == beds["occupied"]).all()
    rooms = df.filter(pl.col("capacity_unit") == "room")
    assert (rooms["service_users"] >= rooms["occupied"]).all()
