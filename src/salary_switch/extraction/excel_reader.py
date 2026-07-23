from pathlib import Path

import pandas as pd


def read_salary_excel(file_path: Path) -> pd.DataFrame:
    """Read a salary Excel file and return its raw contents as a DataFrame."""

    if not file_path.exists():
        raise FileNotFoundError(f"Excel file not found: {file_path}")

    if file_path.suffix.lower() != ".xlsx":
        raise ValueError(f"Expected an .xlsx file, received: {file_path.suffix}")

    return pd.read_excel(file_path, engine="openpyxl")