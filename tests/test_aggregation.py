import pandas as pd

from salary_switch.transformation.aggregation import aggregate_salaries


def test_aggregate_salaries() -> None:
    input_df = pd.DataFrame(
        {
            "Year": [2025, 2025, 2025],
            "Position": [
                "Data Engineer",
                "Data Engineer",
                "Data Engineer",
            ],
            "Salary": [100000, 130000, 160000],
            "Experience": [3, 5, 4],
        }
    )

    result_df = aggregate_salaries(input_df)

    assert len(result_df) == 1

    assert result_df.iloc[0]["Year"] == 2025
    assert result_df.iloc[0]["Position"] == "Data Engineer"

    assert result_df.iloc[0]["Min Salary"] == 100000
    assert result_df.iloc[0]["Median Salary"] == 130000
    assert result_df.iloc[0]["Max Salary"] == 160000

    assert result_df.iloc[0]["Sample Count"] == 3
    assert result_df.iloc[0]["Average Experience"] == 4