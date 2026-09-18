import polars as pl

df = pl.read_parquet("cleaned_shelter_usage.parquet")

# Convert the date column to datetime and rename it for clarity
df = df.with_columns(pl.col("date").str.strptime(pl.Date, "%Y-%m-%d").alias("date"))

# Group by "Dates" and calculate total "Capacity" and "Usage"
aggregated_df = (
    df.group_by("date")
    .agg([
        pl.col("Capacity").sum().alias("Total_Capacity"),
        pl.col("Usage").sum().alias("Total_Usage")
    ])
    .sort("date")  # Sort the results by date
)

# Display the aggregated DataFrame
print(aggregated_df)