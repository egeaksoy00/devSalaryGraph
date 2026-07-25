import pandas as pd


def clean_company_size(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    cleaned_dataframe = dataframe.copy()

    cleaned_dataframe["Company Size"] = (
        cleaned_dataframe["Company Size"]
        .astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.replace(r"\s*-\s*", " - ", regex=True)
    )

    return cleaned_dataframe