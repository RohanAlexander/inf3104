
import polars as pl

df = pl.read_parquet("shelter_usage.parquet")

# Select specific columns
selected_columns = ["OCCUPANCY_DATE", "SHELTER_ID", "OCCUPIED_BEDS", "CAPACITY_ACTUAL_BED"]

selected_df = df.select(selected_columns)

# Filter to only rows that have data
filtered_df = selected_df.filter(df["OCCUPIED_BEDS"].is_not_null())

print(filtered_df.head())

renamed_df = filtered_df.rename({"OCCUPANCY_DATE": "date",
                                 "SHELTER_ID": "Shelters",
                                 "CAPACITY_ACTUAL_BED": "Capacity",
                                 "OCCUPIED_BEDS": "Usage"
                                 })

print(renamed_df.head())

renamed_df.write_parquet("cleaned_shelter_usage.parquet")