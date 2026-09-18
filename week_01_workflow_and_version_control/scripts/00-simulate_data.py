#### Workspace setup ####
import polars as pl
import numpy as np
from datetime import date

rng = np.random.default_rng(seed=853)


#### Simulate data ####
# Simulate 10 shelters and some set capacity
shelters_df = pl.DataFrame(
    {
        "Shelters": [f"Shelter {i}" for i in range(1, 11)],
        "Capacity": rng.integers(low=10, high=100, size=10),
    }
)

# Create data frame of dates
dates = pl.date_range(
    start=date(2024, 1, 1), end=date(2024, 12, 31), interval="1d", eager=True
).alias("Dates")

# Convert dates into a data frame
dates_df = pl.DataFrame(dates)

# Combine dates and shelters
data = dates_df.join(shelters_df, how="cross")

# Add usage as a Poisson draw
poisson_draw = rng.poisson(lam=data["Capacity"])
usage = np.minimum(poisson_draw, data["Capacity"])

data = data.with_columns([pl.Series("Usage", usage)])

data.write_parquet("simulated_data.parquet")