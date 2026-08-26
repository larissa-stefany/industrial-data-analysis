from pathlib import Path
import sqlite3
import pandas as pd


def load_and_clean(raw_path: Path) -> pd.DataFrame:
    df = pd.read_csv(raw_path, parse_dates=['date'])
    df = df.drop_duplicates().copy()
    df = df[df['total_units'].fillna(0) > 0].copy()
    df['operator_id'] = df['operator_id'].fillna('UNKNOWN')
    df['downtime_minutes'] = df['downtime_minutes'].fillna(df['downtime_minutes'].median())
    df['operating_minutes'] = (df['planned_minutes'] - df['downtime_minutes']).clip(lower=1)
    df['good_units'] = (df['total_units'] - df['defective_units']).clip(lower=0)
    df['defect_rate'] = (df['defective_units'] / df['total_units']).clip(0, 1)
    df['availability'] = (df['operating_minutes'] / df['planned_minutes']).clip(0, 1)
    ideal_rate_per_min = 0.72
    df['performance'] = (df['total_units'] / (df['operating_minutes'] * ideal_rate_per_min)).clip(0, 1.15)
    df['quality'] = (df['good_units'] / df['total_units']).clip(0, 1)
    df['oee'] = df['availability'] * df['performance'].clip(upper=1) * df['quality']
    numeric_cols = ['downtime_minutes','operating_minutes','defect_rate','availability','performance','quality','oee']
    df[numeric_cols] = df[numeric_cols].round(4)
    df['year']=df['date'].dt.year; df['month']=df['date'].dt.month; df['month_name']=df['date'].dt.strftime('%b'); df['week']=df['date'].dt.isocalendar().week.astype(int); df['day_of_week']=df['date'].dt.day_name()
    return df


def save_outputs(df: pd.DataFrame, csv_path: Path, db_path: Path) -> None:
    csv_path.parent.mkdir(parents=True,exist_ok=True); db_path.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(csv_path,index=False)
    with sqlite3.connect(db_path) as conn:
        df.to_sql('production',conn,if_exists='replace',index=False)
        conn.execute('CREATE INDEX IF NOT EXISTS idx_production_date ON production(date)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_production_machine ON production(machine_id)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_production_shift ON production(shift)')


def main() -> None:
    root=Path(__file__).resolve().parents[1]
    raw_path=root/'data'/'raw'/'manufacturing_production_raw.csv'
    processed_path=root/'data'/'processed'/'manufacturing_production_clean.csv'
    db_path=root/'data'/'processed'/'manufacturing.db'
    df=load_and_clean(raw_path); save_outputs(df,processed_path,db_path)
    print(f'ETL complete: {len(df):,} clean rows')
    print(f'CSV: {processed_path}'); print(f'SQLite: {db_path}')


if __name__ == '__main__':
    main()
