from pathlib import Path
import sqlite3
import pandas as pd


def calculate_kpis(db_path: Path) -> dict:
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query('SELECT * FROM production', conn)
    return {'total_production':int(df['total_units'].sum()),'good_units':int(df['good_units'].sum()),'defective_units':int(df['defective_units'].sum()),'defect_rate':float(df['defective_units'].sum()/df['total_units'].sum()),'downtime_hours':float(df['downtime_minutes'].sum()/60),'avg_oee':float(df['oee'].mean()),'avg_availability':float(df['availability'].mean()),'avg_performance':float(df['performance'].clip(upper=1).mean()),'avg_quality':float(df['quality'].mean())}


if __name__ == '__main__':
    root=Path(__file__).resolve().parents[1]
    kpis=calculate_kpis(root/'data'/'processed'/'manufacturing.db')
    for key,value in kpis.items(): print(f'{key}: {value}')
