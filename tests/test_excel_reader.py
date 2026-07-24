from pathlib import Path
import pytest
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

def test_read_salary_excel_raises_error_when_file_does_not_exist(
    tmp_path: Path,
) -> None:
    missing_file = tmp_path / "missing.xlsx"

    with pytest.raises(FileNotFoundError):
        read_salary_excel(missing_file)


def test_read_salary_excel_rejects_non_xlsx_file(tmp_path: Path) -> None:
    csv_file = tmp_path / "salary_data.csv"
    csv_file.write_text(
        "Position,Salary\nData Engineer,120000",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        read_salary_excel(csv_file)