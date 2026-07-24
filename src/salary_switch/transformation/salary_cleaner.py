import pandas as pd

from salary_switch.transformation.salary_parser import parse_salary_range


def clean_salary_ranges(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the DataFrame with parsed salary values."""

    cleaned_df = dataframe.copy()

    cleaned_df["Salary"] = cleaned_df["Salary"].apply(
        parse_salary_range
    )

    return cleaned_df