#### Preamble ####
# Purpose: Simulate the shelter dataset that we want to end up with, and
#   check that the tests pass on it, before looking at the real data
# Author: Rohan Alexander
# Contact: rohan.alexander@utoronto.ca
# Pre-requisites: uv add numpy polars

import datetime

import numpy as np
import polars as pl
from tests import CAPACITY_UNITS, SCHEMA, SECTORS, test_shelter

rng = np.random.default_rng(seed=853)

NUM_PROGRAMS = 100
NUM_NIGHTS = 5

program_id = [str(i) for i in rng.choice(np.arange(10000, 20000), size=NUM_PROGRAMS, replace=False)]
sector = rng.choice(SECTORS, size=NUM_PROGRAMS)
capacity_unit = rng.choice(CAPACITY_UNITS, size=NUM_PROGRAMS, p=[0.75, 0.25])
capacity = rng.integers(5, 120, size=NUM_PROGRAMS)

rows = []
for night in range(NUM_NIGHTS):
    for p in range(NUM_PROGRAMS):
        occupied = int(rng.binomial(n=capacity[p], p=0.97))
        # One person to a bed; one or more people to a room
        people = occupied if capacity_unit[p] == "bed" else occupied + int(rng.poisson(occupied))
        rows.append(
            {
                "occupancy_date": datetime.date(2026, 9, 12) + datetime.timedelta(days=night),
                "program_id": program_id[p],
                "sector": str(sector[p]),
                "capacity_unit": str(capacity_unit[p]),
                "service_users": people,
                "capacity": int(capacity[p]),
                "occupied": occupied,
                "occupancy_rate": round(100 * occupied / int(capacity[p]), 2),
            }
        )

simulated = pl.DataFrame(rows, schema=SCHEMA)
test_shelter(simulated)

simulated.write_parquet("data/simulated_shelter.parquet")
print(simulated.head())
