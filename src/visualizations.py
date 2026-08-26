"""Reusable charts for manufacturing performance analysis."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_machine_oee_chart(scorecard: pd.DataFrame, output: Path) -> None:
    """Save a bar chart comparing average OEE by machine."""
    data = scorecard.sort_values("avg_oee")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(data["machine_id"], data["avg_oee"] * 100)
    ax.set_title("Average OEE by Machine")
    ax.set_xlabel("Machine")
    ax.set_ylabel("OEE (%)")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    fig.savefig(output, dpi=160)
    plt.close(fig)


def save_defect_pareto_chart(pareto: pd.DataFrame, output: Path) -> None:
    """Save a defect Pareto chart with cumulative percentage."""
    data = pareto.sort_values("defective_units", ascending=False).copy()
    data["cumulative_pct"] = data["defective_units"].cumsum() / data["defective_units"].sum() * 100

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(data["machine_id"], data["defective_units"])
    ax.set_title("Defect Pareto by Machine")
    ax.set_xlabel("Machine")
    ax.set_ylabel("Defective Units")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    fig.savefig(output, dpi=160)
    plt.close(fig)
