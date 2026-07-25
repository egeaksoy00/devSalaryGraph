import pandas as pd


EXPERIENCE_MAPPING = {
    "0 - 1 Yıl": 0.5,
    "1 - 3 Yıl": 2.0,
    "3 - 5 Yıl": 4.0,
    "5 - 7 Yıl": 6.0,
    "7 - 10 Yıl": 8.5,
    "10 - 12 Yıl": 11.0,
    "12 - 14 Yıl": 13.0,
    "15 Yıl ve üzeri": 15.0,
}


def clean_experience(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Convert experience ranges into representative numeric values."""

    cleaned_dataframe = dataframe.copy()

    cleaned_dataframe["Experience"] = (
        cleaned_dataframe["Experience"]
        .astype(str)
        .str.strip()
    )

    numeric_experience = cleaned_dataframe["Experience"].map(
        EXPERIENCE_MAPPING
    )

    if numeric_experience.isna().any():
        unsupported_values = sorted(
            cleaned_dataframe.loc[
                numeric_experience.isna(),
                "Experience",
            ].unique()
        )

        raise ValueError(
            f"Unsupported experience values: {unsupported_values}"
        )

    cleaned_dataframe["Experience"] = numeric_experience

    return cleaned_dataframe