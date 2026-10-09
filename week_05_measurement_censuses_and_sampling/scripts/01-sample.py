#### Preamble ####
# Purpose: Draw 1,000 samples of 1,000 households under five designs and
#   save the estimate of the poverty rate from each
# Author: Rohan Alexander
# Contact: rohan.alexander@utoronto.ca
# Pre-requisites: 00-simulate_population.py

import numpy as np
import polars as pl

rng = np.random.default_rng(seed=853)

population = pl.read_parquet("data/population.parquet")
N = population.height
n = 1000
REPS = 1000

in_poverty = population["in_poverty"].to_numpy()
ward = population["ward"].to_numpy()
block = population["block"].to_numpy()
wards = np.unique(ward)
blocks = np.unique(block)
index_by_ward = {w: np.flatnonzero(ward == w) for w in wards}
index_by_block = {b: np.flatnonzero(block == b) for b in blocks}


def simple_random():
    chosen = rng.choice(N, size=n, replace=False)
    return in_poverty[chosen].mean()


def systematic():
    # The list is ordered by ward and block, as a street directory would be
    k = N // n
    start = rng.integers(0, k)
    return in_poverty[start::k].mean()


def stratified():
    # Proportional allocation: every ward is the same size, so 50 from each.
    # With equal-sized strata the weights are equal and the mean of means is fine.
    per_ward = n // len(wards)
    means = []
    for w in wards:
        chosen = rng.choice(index_by_ward[w], size=per_ward, replace=False)
        means.append(in_poverty[chosen].mean())
    return np.mean(means)


def two_stage_cluster():
    # 25 blocks at random, then 40 households within each
    chosen_blocks = rng.choice(blocks, size=25, replace=False)
    means = []
    for b in chosen_blocks:
        chosen = rng.choice(index_by_block[b], size=40, replace=False)
        means.append(in_poverty[chosen].mean())
    return np.mean(means)


def convenience():
    # Whoever is easiest to reach: households in the two wards nearest the office
    nearby = np.concatenate([index_by_ward[1], index_by_ward[2]])
    return in_poverty[rng.choice(nearby, size=n, replace=False)].mean()


designs = {
    "Simple random": simple_random,
    "Systematic": systematic,
    "Stratified by ward": stratified,
    "Two-stage cluster": two_stage_cluster,
    "Convenience": convenience,
}

estimates = pl.DataFrame(
    [{"design": name, "rep": rep, "estimate": float(draw())} for name, draw in designs.items() for rep in range(1, REPS + 1)]
)

assert estimates.height == len(designs) * REPS
assert estimates["estimate"].is_between(0, 1).all()

estimates.write_parquet("data/estimates.parquet")

truth = in_poverty.mean()
print(f"Truth: {truth:.4f}")
print(
    estimates.group_by("design", maintain_order=True).agg(
        pl.col("estimate").mean().alias("mean"),
        pl.col("estimate").std().alias("sd"),
        ((pl.col("estimate") - truth) ** 2).mean().sqrt().alias("rmse"),
    )
)
