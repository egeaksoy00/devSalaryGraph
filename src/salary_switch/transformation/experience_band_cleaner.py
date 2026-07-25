import pandas as pd


def clean_experience_band(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Clean experience band values."""

    cleaned_dataframe = dataframe.copy()

    cleaned_dataframe["Experience"] = (
        cleaned_dataframe["Experience"]
        .astype(str)
        .str.strip()
    )

    return cleaned_dataframe