"""Data-quality checks for the manufacturing dataset."""

import pandas as pd


REQUIRED_COLUMNS = {
    "date",
    "machine_id",
    "shift",
    "total_units",
    "good_units",
    "defective_units",
    "downtime_minutes",
    "oee",
}


def validate_production_data(df: pd.DataFrame) -> dict:
    """Return a compact data-quality report for a production DataFrame."""
    missing_columns = sorted(REQUIRED_COLUMNS - set(df.columns))

    report = {
        "rows": int(len(df)),
        "missing_required_columns": missing_columns,
        "duplicate_rows": int(df.duplicated().sum()),
        "null_cells": int(df.isna().sum().sum()),
        "invalid_unit_balance": 0,
        "invalid_oee": 0,
    }

    if not missing_columns:
        report["invalid_unit_balance"] = int(
            (df["good_units"] + df["defective_units"] != df["total_units"]).sum()
        )
        report["invalid_oee"] = int((~df["oee"].between(0, 1)).sum())

    report["is_valid"] = not any(
        [
            report["missing_required_columns"],
            report["invalid_unit_balance"],
            report["invalid_oee"],
        ]
    )
    return report
