from pathlib import Path
import sqlite3

import pandas as pd


def _load_production(db_path: Path) -> pd.DataFrame:
    """Load the production fact table from SQLite."""
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql_query("SELECT * FROM production", conn)


def calculate_kpis(db_path: Path) -> dict:
    """Calculate the main manufacturing KPIs used by the dashboard."""
    df = _load_production(db_path)

    total_units = int(df["total_units"].sum())
    defective_units = int(df["defective_units"].sum())

    return {
        "total_production": total_units,
        "good_units": int(df["good_units"].sum()),
        "defective_units": defective_units,
        "defect_rate": float(defective_units / total_units),
        "downtime_hours": float(df["downtime_minutes"].sum() / 60),
        "avg_oee": float(df["oee"].mean()),
        "avg_availability": float(df["availability"].mean()),
        "avg_performance": float(df["performance"].clip(upper=1).mean()),
        "avg_quality": float(df["quality"].mean()),
    }


def machine_performance(db_path: Path) -> pd.DataFrame:
    """Return a machine-level scorecard ordered by lowest OEE."""
    df = _load_production(db_path)

    scorecard = (
        df.groupby("machine_id", as_index=False)
        .agg(
            total_units=("total_units", "sum"),
            defective_units=("defective_units", "sum"),
            downtime_minutes=("downtime_minutes", "sum"),
            avg_oee=("oee", "mean"),
        )
    )
    scorecard["defect_rate"] = (
        scorecard["defective_units"] / scorecard["total_units"]
    )
    scorecard["downtime_hours"] = scorecard["downtime_minutes"] / 60

    return scorecard.sort_values("avg_oee").reset_index(drop=True)


def shift_performance(db_path: Path) -> pd.DataFrame:
    """Summarize production, quality and OEE by shift."""
    df = _load_production(db_path)

    summary = (
        df.groupby("shift", as_index=False)
        .agg(
            total_units=("total_units", "sum"),
            good_units=("good_units", "sum"),
            defective_units=("defective_units", "sum"),
            avg_oee=("oee", "mean"),
            downtime_minutes=("downtime_minutes", "sum"),
        )
    )
    summary["defect_rate"] = (
        summary["defective_units"] / summary["total_units"]
    )
    summary["downtime_hours"] = summary["downtime_minutes"] / 60

    return summary.sort_values("avg_oee", ascending=False).reset_index(drop=True)


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    database = root / "data" / "processed" / "manufacturing.db"

    for key, value in calculate_kpis(database).items():
        print(f"{key}: {value}")
