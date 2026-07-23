from pathlib import Path

import pandas as pd

from salary_switch.extraction.excel_reader import read_salary_excel


def test_read_salary_excel_returns_dataframe(tmp_path: Path) -> None:
    test_file = tmp_path / "salary_data.xlsx"

    expected_data = pd.DataFrame(
        {
            "Position": ["Software Engineer", "Data Engineer"],
            "Salary": ["120.000 - 124.999", "130.000 - 134.999"],
        }
    )

    expected_data.to_excel(test_file, index=False)

    result = read_salary_excel(test_file)

    assert isinstance(result, pd.DataFrame)
    assert result.equals(expected_data)