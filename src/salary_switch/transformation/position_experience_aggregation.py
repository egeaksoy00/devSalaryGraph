import pandas as pd


def aggregate_position_experience_salaries(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    aggregated_dataframe = (
        dataframe.groupby(
            [
                "Year",
                "Position",
                "Experience",
            ],
            as_index=False,
        )
        .agg(
            Median_Salary=("Salary", "median"),
            Sample_Count=("Salary", "count"),
        )
    )

    aggregated_dataframe = aggregated_dataframe.rename(
        columns={
            "Median_Salary": "Median Salary",
            "Sample_Count": "Sample Count",
        }
    )

    return aggregated_dataframe