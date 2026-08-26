from pathlib import Path

from src.kpis import calculate_kpis, machine_performance, shift_performance


def build_executive_summary(db_path: Path) -> list[str]:
    """Generate concise business insights from the manufacturing dataset."""
    kpis = calculate_kpis(db_path)
    machines = machine_performance(db_path)
    shifts = shift_performance(db_path)

    worst_machine = machines.iloc[0]
    best_shift = shifts.iloc[0]
    worst_shift = shifts.iloc[-1]

    return [
        (
            f"Overall OEE is {kpis['avg_oee']:.1%} with a defect rate of "
            f"{kpis['defect_rate']:.1%}."
        ),
        (
            f"Machine {worst_machine['machine_id']} has the lowest average OEE "
            f"at {worst_machine['avg_oee']:.1%} and a defect rate of "
            f"{worst_machine['defect_rate']:.1%}."
        ),
        (
            f"Shift {best_shift['shift']} leads performance with "
            f"{best_shift['avg_oee']:.1%} average OEE."
        ),
        (
            f"Shift {worst_shift['shift']} requires attention, with "
            f"{worst_shift['avg_oee']:.1%} average OEE and "
            f"{worst_shift['downtime_hours']:.1f} downtime hours."
        ),
    ]


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    database = root / "data" / "processed" / "manufacturing.db"

    for insight in build_executive_summary(database):
        print(f"- {insight}")
