import pandas as pd
import pytest

from salary_switch.validation.schema_validator import (
    validate_required_columns,
)


def test_validate_required_columns_accepts_valid_dataframe() -> None:
    dataframe = pd.DataFrame(
        {
            "Position": ["Data Engineer"],
            "Salary": ["120.000 - 124.999"],
        }
    )

    validate_required_columns(
        dataframe,
        {"Position", "Salary"},
    )


def test_validate_required_columns_raises_error_for_missing_columns() -> None:
    dataframe = pd.DataFrame(
        {
            "Position": ["Data Engineer"],
        }
    )

    with pytest.raises(
        ValueError,
        match="Missing required columns",
    ):
        validate_required_columns(
            dataframe,
            {"Position", "Salary"},
        )