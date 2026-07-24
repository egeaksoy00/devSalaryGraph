import pytest

from salary_switch.transformation.salary_parser import parse_salary_range

def test_parse_salary_range_returns_value_for_open_ended_range() -> None:
    result = parse_salary_range("400.000+")

    assert result == 400000

def test_parse_salary_range_returns_lower_bound() -> None:
    result = parse_salary_range("120.000 - 124.999")

    assert result == 120000


def test_parse_salary_range_raises_error_for_invalid_value() -> None:
    with pytest.raises(ValueError, match="Invalid salary range"):
        parse_salary_range("unknown")