
import polars as pl

# URL of the CSV file
url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/21c83b32-d5a8-4106-a54f-010dbe49f6f2/resource/ffd20867-6e3c-4074-8427-d63810edf231/download/Daily%20shelter%20overnight%20occupancy.csv"

# Read the CSV file into a Polars DataFrame
df = pl.read_csv(url)

# Save the raw data
df.write_parquet("shelter_usage.parquet")