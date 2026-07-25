import pandas as pd


SENIORITY_MAPPING = {
    "Junior": "Junior",
    "Middle": "Middle",
    "Senior": "Senior",
}


def clean_seniority(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    cleaned_dataframe = dataframe.copy()

    cleaned_dataframe["Seniority"] = (
        cleaned_dataframe["Seniority"]
        .astype(str)
        .str.strip()
    )

    normalized_seniority = cleaned_dataframe["Seniority"].map(
        SENIORITY_MAPPING
    )

    if normalized_seniority.isna().any():
        unsupported_values = sorted(
            cleaned_dataframe.loc[
                normalized_seniority.isna(),
                "Seniority",
            ].unique()
        )

        raise ValueError(
            f"Unsupported seniority values: {unsupported_values}"
        )

    cleaned_dataframe["Seniority"] = normalized_seniority

    return cleaned_dataframe