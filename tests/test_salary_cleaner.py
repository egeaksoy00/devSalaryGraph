import pandas as pd

from salary_switch.transformation.salary_cleaner import clean_salary_ranges


def test_clean_salary_ranges_parses_salary_column() -> None:
    dataframe = pd.DataFrame(
        {
            "Position": ["Data Engineer"],
            "Salary": ["120.000 - 124.999"],
        }
    )

    cleaned_df = clean_salary_ranges(dataframe)

    assert cleaned_df["Salary"].tolist() == [120000]
    # Convert the Series to a Python list for easy comparison.

    #   print(type(cleaned_df)) output= <class 'pandas.core.frame.DataFrame'>
    #  print(type(cleaned_df["Salary"])) output = <class 'pandas.core.series.Series'>
    # print(type(cleaned_df["Salary"].tolist())) output = <class 'list'>