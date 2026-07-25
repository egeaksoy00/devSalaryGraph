from pathlib import Path

from salary_switch.extraction.excel_reader import read_salary_excel
from salary_switch.loading.csv_writer import save_to_csv
from salary_switch.transformation.company_size_cleaner import (
    clean_company_size,
)
from salary_switch.transformation.company_size_seniority_aggregation import (
    aggregate_company_size_seniority_salaries,
)
from salary_switch.transformation.currency_converter import (
    convert_salaries_to_try,
)
from salary_switch.transformation.salary_cleaner import clean_salary_ranges
from salary_switch.transformation.seniority_cleaner import clean_seniority
from salary_switch.validation.schema_validator import validate_required_columns


REQUIRED_COLUMNS = {
    "Year",
    "Salary",
    "Currency",
    "Company Size",
    "Seniority",
}


def run_company_size_seniority_pipeline(
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

    company_size_cleaned_dataframe = clean_company_size(
        salary_cleaned_dataframe
    )

    seniority_cleaned_dataframe = clean_seniority(
        company_size_cleaned_dataframe
    )

    converted_dataframe = convert_salaries_to_try(
        seniority_cleaned_dataframe
    )

    aggregated_dataframe = (
        aggregate_company_size_seniority_salaries(
            converted_dataframe
        )
    )

    save_to_csv(
        aggregated_dataframe,
        output_path,
    )

    print(
        "Company-size seniority pipeline completed: "
        f"{output_path}"
    )


if __name__ == "__main__":
    run_company_size_seniority_pipeline(
        input_path=Path("data/raw/salary_2026.xlsx"),
        output_path=Path(
            "data/processed/company_size_seniority_salary_summary.csv"
        ),
    )