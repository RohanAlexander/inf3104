import polars as pl

df = pl.read_parquet("simulated_data.parquet")

print(df.head(5))