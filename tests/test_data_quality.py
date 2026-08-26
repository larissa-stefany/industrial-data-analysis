from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.data_quality import validate_production_data


def test_valid_production_dataset():
    df = pd.DataFrame(
        {
            "date": ["2026-01-01"],
            "machine_id": ["M-01"],
            "shift": ["1st"],
            "total_units": [100],
            "good_units": [96],
            "defective_units": [4],
            "downtime_minutes": [12.0],
            "oee": [0.82],
        }
    )

    report = validate_production_data(df)
    assert report["is_valid"] is True
    assert report["invalid_unit_balance"] == 0
    assert report["invalid_oee"] == 0


def test_invalid_unit_balance_is_detected():
    df = pd.DataFrame(
        {
            "date": ["2026-01-01"],
            "machine_id": ["M-01"],
            "shift": ["1st"],
            "total_units": [100],
            "good_units": [90],
            "defective_units": [4],
            "downtime_minutes": [12.0],
            "oee": [0.82],
        }
    )

    report = validate_production_data(df)
    assert report["is_valid"] is False
    assert report["invalid_unit_balance"] == 1
