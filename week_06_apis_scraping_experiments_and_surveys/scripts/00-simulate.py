#### Preamble ####
# Purpose: Simulate the dataset that we expect to end up with from Table 3.1
#   of the 1993 Kenya DHS final report, before we parse anything
# Author: Rohan Alexander
# Contact: rohan.alexander@utoronto.ca
# Pre-requisites: uv add numpy polars

import numpy as np
import polars as pl

rng = np.random.default_rng(seed=853)

age_groups = ["15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49"]
residences = ["Urban", "Rural", "Total"]

# Age-specific fertility rates are births per 1,000 women, so integers
# between 0 and about 400
simulated = pl.DataFrame(
    [
        {"age_group": age, "residence": residence, "births_per_1000_women": int(rng.integers(0, 400))}
        for residence in residences
        for age in age_groups
    ]
)

assert simulated.height == 21
assert simulated["births_per_1000_women"].is_between(0, 400).all()

simulated.write_parquet("data/simulated_fertility.parquet")
print(simulated.head(7))
