from pathlib import Path

from salary_switch.extraction.excel_reader import read_salary_excel
from salary_switch.loading.csv_writer import save_to_csv
from salary_switch.transformation.aggregation import aggregate_salaries
from salary_switch.transformation.currency_converter import (
    convert_salaries_to_try,
)
from salary_switch.transformation.experience_cleaner import (
    clean_experience,
)
from salary_switch.transformation.salary_cleaner import clean_salary_ranges
from salary_switch.validation.schema_validator import validate_required_columns


REQUIRED_COLUMNS = {
    "Year",
    "Position",
    "Salary",
    "Experience",
    "Currency",
}


def run_pipeline(
    input_path: Path,
    output_path: Path,
) -> None:
    dataframe = read_salary_excel(input_path)

    validate_required_columns(
        dataframe,
        REQUIRED_COLUMNS,
    )

    salary_cleaned_dataframe = clean_salary_ranges(
        dataframe
    )

    experience_cleaned_dataframe = clean_experience(
        salary_cleaned_dataframe
    )

    converted_dataframe = convert_salaries_to_try(
        experience_cleaned_dataframe
    )

    aggregated_dataframe = aggregate_salaries(
        converted_dataframe
    )

    save_to_csv(
        aggregated_dataframe,
        output_path,
    )

    print(f"Pipeline completed: {output_path}")


if __name__ == "__main__":
    run_pipeline(
        input_path=Path("data/raw/salary_2026.xlsx"),
        output_path=Path("data/processed/salary_summary.csv"),
    )