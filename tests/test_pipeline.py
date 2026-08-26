from pathlib import Path
import sqlite3
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.generate_data import generate_dataset
from src.kpis import calculate_kpis, machine_performance, shift_performance


def _build_test_database(tmp_path: Path) -> Path:
    df = generate_dataset(n_rows=500, seed=7)
    db_path = tmp_path / "test_manufacturing.db"

    with sqlite3.connect(db_path) as conn:
        df.to_sql("production", conn, index=False, if_exists="replace")

    return db_path


def test_generator_columns():
    df = generate_dataset(n_rows=500, seed=1)
    expected = {
        "date",
        "machine_id",
        "shift",
        "total_units",
        "defective_units",
        "oee",
    }
    assert expected.issubset(df.columns)
    assert len(df) == 500


def test_generated_business_rules():
    df = generate_dataset(n_rows=500, seed=2)
    assert (df["defective_units"] <= df["total_units"]).all()
    assert (df["good_units"] >= 0).all()
    assert df["oee"].dropna().between(0, 1).all()


def test_kpis_are_consistent(tmp_path):
    db_path = _build_test_database(tmp_path)
    kpis = calculate_kpis(db_path)

    assert kpis["total_production"] > 0
    assert kpis["good_units"] + kpis["defective_units"] == kpis["total_production"]
    assert 0 <= kpis["defect_rate"] <= 1
    assert 0 <= kpis["avg_oee"] <= 1


def test_machine_scorecard(tmp_path):
    db_path = _build_test_database(tmp_path)
    scorecard = machine_performance(db_path)

    assert not scorecard.empty
    assert {"machine_id", "avg_oee", "defect_rate", "downtime_hours"}.issubset(
        scorecard.columns
    )
    assert scorecard["avg_oee"].is_monotonic_increasing


def test_shift_scorecard(tmp_path):
    db_path = _build_test_database(tmp_path)
    summary = shift_performance(db_path)

    assert not summary.empty
    assert summary["shift"].nunique() <= 3
    assert summary["avg_oee"].is_monotonic_decreasing
    assert (summary["defect_rate"].between(0, 1)).all()
