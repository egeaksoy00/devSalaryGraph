import pandas as pd


def aggregate_salaries(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate salary data by year and position."""

    grouped_df = df.groupby(["Year", "Position"])

    aggregated_df = grouped_df.agg(
        {
            "Salary": ["min", "median", "max", "count"],
            "Experience": "mean",
        }
    )

    aggregated_df = aggregated_df.reset_index()

    aggregated_df.columns = [
    "Year",
    "Position",
    "Min Salary",
    "Median Salary",
    "Max Salary",
    "Sample Count",
    "Average Experience",
]

    return aggregated_df