import pandas as pd


EXCHANGE_RATES_TO_TRY = {
    "₺ - Türk Lirası": 1.0,
    "$ - Dolar": 47.0,
    "€ - Euro": 55.0,
    "£ - Sterlin": 63.0,
}


def convert_salaries_to_try(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Convert salary values to TRY."""

    converted_dataframe = dataframe.copy()

    converted_dataframe["Currency"] = (
        converted_dataframe["Currency"]
        .astype(str)
        .str.strip()
    )

    converted_dataframe["Exchange Rate"] = converted_dataframe[
        "Currency"
    ].map(EXCHANGE_RATES_TO_TRY)

    if converted_dataframe["Exchange Rate"].isna().any():
        unsupported_currencies = sorted(
            converted_dataframe.loc[
                converted_dataframe["Exchange Rate"].isna(),
                "Currency",
            ].unique()
        )

        raise ValueError(
            f"Unsupported currencies: {unsupported_currencies}"
        )

    converted_dataframe["Salary"] = (
        converted_dataframe["Salary"]
        * converted_dataframe["Exchange Rate"]
    )

    converted_dataframe["Currency"] = "₺ - Türk Lirası"

    return converted_dataframe