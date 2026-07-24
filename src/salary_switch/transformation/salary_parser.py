def parse_salary_range(salary_range: str) -> int:
    """Return the lower bound of a salary range as an integer."""

    normalized_value = salary_range.strip()

    if "-" in normalized_value:
        lower_bound = normalized_value.split("-", maxsplit=1)[0].strip()
    elif normalized_value.endswith("+"):
        lower_bound = normalized_value.removesuffix("+").strip()
    else:
        lower_bound = normalized_value

    normalized_salary = lower_bound.replace(".", "")

    if not normalized_salary.isdigit():
        raise ValueError(f"Invalid salary range: {salary_range}")

    return int(normalized_salary)