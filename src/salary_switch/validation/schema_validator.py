import pandas as pd


def validate_required_columns(
    dataframe: pd.DataFrame,
    required_columns: set[str],
) -> None:
    missing_columns = required_columns - set(dataframe.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )