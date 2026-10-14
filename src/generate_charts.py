"""Generate portfolio charts from the project's processed SQLite database."""

from pathlib import Path

from src.kpis import machine_performance
from src.visualizations import save_machine_oee_chart, save_defect_pareto_chart


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    db = root / "data" / "processed" / "manufacturing.db"
    if not db.exists():
        raise SystemExit("Banco nao encontrado. Execute python src/generate_data.py e python src/etl.py primeiro.")

    output_dir = root / "images"
    output_dir.mkdir(parents=True, exist_ok=True)
    scorecard = machine_performance(db)
    save_machine_oee_chart(scorecard, output_dir / "oee_by_machine.png")
    save_defect_pareto_chart(scorecard, output_dir / "defect_pareto_by_machine.png")
    print(f"Graficos salvos em: {output_dir}")


if __name__ == "__main__":
    main()
