import pandas as pd


def aggregate_company_size_seniority_salaries(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    aggregated_dataframe = (
        dataframe.groupby(
            [
                "Year",
                "Company Size",
                "Seniority",
            ],
            as_index=False,
        )
        .agg(
            Median_Salary=("Salary", "median"),
            Sample_Count=("Salary", "count"),
        )
        .rename(
            columns={
                "Median_Salary": "Median Salary",
                "Sample_Count": "Sample Count",
            }
        )
    )

    return aggregated_dataframe