from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.generate_data import generate_dataset


def test_generator_columns():
    df = generate_dataset(n_rows=500, seed=1)
    expected = {'date','machine_id','shift','total_units','defective_units','oee'}
    assert expected.issubset(df.columns)
    assert len(df) == 500


def test_generated_business_rules():
    df = generate_dataset(n_rows=500, seed=2)
    assert (df['defective_units'] <= df['total_units']).all()
    assert (df['good_units'] >= 0).all()
    assert df['oee'].dropna().between(0,1).all()
