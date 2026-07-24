import pandas as pd

from salary_switch.loading.csv_writer import save_to_csv


def test_save_to_csv(tmp_path) -> None:
    input_df = pd.DataFrame(
        {
            "Year": [2025],
            "Position": ["Data Engineer"],
            "Min Salary": [100000],
            "Median Salary": [130000],
            "Max Salary": [160000],
            "Sample Count": [3],
            "Average Experience": [4.0],
        }
    )

    output_path = tmp_path / "salary_summary.csv"

    save_to_csv(input_df, str(output_path))

    assert output_path.exists()

    saved_df = pd.read_csv(output_path)

    pd.testing.assert_frame_equal(saved_df, input_df)