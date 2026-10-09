#### Preamble ####
# Purpose: Simulate a city of 100,000 households in which to try sampling designs
# Author: Rohan Alexander
# Contact: rohan.alexander@utoronto.ca
# Pre-requisites: uv add numpy polars

import numpy as np
import polars as pl

rng = np.random.default_rng(seed=853)

NUM_WARDS = 20
BLOCKS_PER_WARD = 25
HOUSEHOLDS_PER_BLOCK = 200
POVERTY_LINE = 600  # dollars a week

# Wards differ from each other, blocks differ within a ward, and households
# differ within a block. All on the log scale, so income is right-skewed.
ward_effect = rng.normal(loc=0, scale=0.35, size=NUM_WARDS)
block_effect = rng.normal(loc=0, scale=0.25, size=(NUM_WARDS, BLOCKS_PER_WARD))

rows = []
for ward in range(NUM_WARDS):
    for block in range(BLOCKS_PER_WARD):
        log_income = (
            np.log(1000)
            + ward_effect[ward]
            + block_effect[ward, block]
            + rng.normal(loc=0, scale=0.45, size=HOUSEHOLDS_PER_BLOCK)
        )
        rows.append(
            pl.DataFrame(
                {
                    "ward": ward + 1,
                    "block": ward * BLOCKS_PER_WARD + block + 1,
                    "weekly_income": np.exp(log_income).round(0),
                }
            )
        )

population = (
    pl.concat(rows)
    .with_row_index("household", offset=1)
    .with_columns((pl.col("weekly_income") < POVERTY_LINE).alias("in_poverty"))
)

# Tests: the population is the size and shape we planned
assert population.height == NUM_WARDS * BLOCKS_PER_WARD * HOUSEHOLDS_PER_BLOCK
assert population["ward"].n_unique() == NUM_WARDS
assert population["block"].n_unique() == NUM_WARDS * BLOCKS_PER_WARD
assert population["weekly_income"].min() > 0
assert population["household"].is_unique().all()

population.write_parquet("data/population.parquet")
print(population.head())
print(f"Poverty rate in the population: {population['in_poverty'].mean():.4f}")
