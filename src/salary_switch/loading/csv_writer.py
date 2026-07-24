import pandas as pd


def save_to_csv(
    dataframe: pd.DataFrame,
    output_path: str,
) -> None:
    """Save a DataFrame as a CSV file."""

    dataframe.to_csv(
        output_path,
        index=False,
    )