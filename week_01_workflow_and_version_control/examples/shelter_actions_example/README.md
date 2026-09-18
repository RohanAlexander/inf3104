# Toronto shelter occupancy downloader

Downloads the City of Toronto's daily shelter overnight occupancy data once a day and saves a dated parquet file to `data/`, using GitHub Actions. No account or credentials needed.

## Setup

1. Fork this repository.
2. Go to Settings > Actions > General, and under "Workflow permissions" select "Read and write permissions". Save.
3. Go to the Actions tab, click "Daily shelter occupancy download", then "Run workflow". A file should appear in `data/` within a couple of minutes.

After that it runs on its own every day at 7am Toronto time.

## Files

- `download_shelter.py`: downloads the CSV and saves it as parquet.
- `.github/workflows/daily_download.yml`: the GitHub Actions workflow.
- `pyproject.toml`: Python dependencies, managed with uv.
- `data/`: output files, one per day.

## To run it on your own computer

```
uv sync
uv run download_shelter.py
```

## Customization

To download a different dataset, change `url` in `download_shelter.py`. Open Data Toronto is at https://open.toronto.ca. To change the schedule, edit the cron expression in the workflow file; https://crontab.guru will translate it for you.
