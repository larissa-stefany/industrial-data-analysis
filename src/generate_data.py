from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
N_ROWS = 100_000


def generate_dataset(n_rows: int = N_ROWS, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.date_range('2025-01-01', '2025-12-31', freq='D')
    machines = [f'M-{i:02d}' for i in range(1, 13)]
    lines = ['Linha A', 'Linha B', 'Linha C']
    products = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
    shifts = ['1º Turno', '2º Turno', '3º Turno']
    operators = [f'OP-{i:03d}' for i in range(1, 61)]
    df = pd.DataFrame({'date': rng.choice(dates, n_rows),'machine_id': rng.choice(machines, n_rows),'line': rng.choice(lines, n_rows, p=[0.38, 0.34, 0.28]),'product': rng.choice(products, n_rows, p=[0.30, 0.28, 0.24, 0.18]),'shift': rng.choice(shifts, n_rows, p=[0.40, 0.36, 0.24]),'operator_id': rng.choice(operators, n_rows)})
    machine_speed_factor = {m: v for m, v in zip(machines, np.linspace(0.90, 1.08, len(machines)))}
    machine_defect_factor = {'M-01':0.020,'M-02':0.022,'M-03':0.025,'M-04':0.028,'M-05':0.031,'M-06':0.034,'M-07':0.037,'M-08':0.041,'M-09':0.046,'M-10':0.053,'M-11':0.060,'M-12':0.071}
    shift_productivity = {'1º Turno':1.05,'2º Turno':1.00,'3º Turno':0.94}
    shift_defect_add = {'1º Turno':0.000,'2º Turno':0.006,'3º Turno':0.013}
    product_cycle = {'Produto A':1.00,'Produto B':0.92,'Produto C':0.86,'Produto D':0.80}
    planned_minutes = rng.integers(420, 481, n_rows)
    downtime_base = rng.gamma(shape=2.2, scale=11.0, size=n_rows)
    machine_downtime_penalty = df['machine_id'].map({m:i*1.3 for i,m in enumerate(machines)}).to_numpy()
    shift_downtime_penalty = df['shift'].map({'1º Turno':0,'2º Turno':4,'3º Turno':8}).to_numpy()
    downtime = np.clip(downtime_base + machine_downtime_penalty + shift_downtime_penalty + rng.normal(0,4,n_rows),0,planned_minutes*0.55)
    operating_minutes = np.maximum(planned_minutes-downtime,1)
    ideal_rate_per_min = 0.72
    theoretical_output = operating_minutes*ideal_rate_per_min*df['machine_id'].map(machine_speed_factor).to_numpy()*df['shift'].map(shift_productivity).to_numpy()*df['product'].map(product_cycle).to_numpy()
    total_units = np.maximum((theoretical_output+rng.normal(0,8,n_rows)).round().astype(int),1)
    defect_rate_expected = df['machine_id'].map(machine_defect_factor).to_numpy()+df['shift'].map(shift_defect_add).to_numpy()+np.where(df['product'].eq('Produto D'),0.007,0)+(downtime/planned_minutes)*0.025
    defect_rate_expected = np.clip(defect_rate_expected,0.005,0.18)
    defective_units = rng.binomial(total_units, defect_rate_expected)
    good_units = total_units-defective_units
    availability = operating_minutes/planned_minutes
    performance = np.clip(total_units/np.maximum(operating_minutes*ideal_rate_per_min,1),0,1.15)
    quality = good_units/total_units
    oee = availability*np.minimum(performance,1)*quality
    df['planned_minutes']=planned_minutes; df['downtime_minutes']=downtime.round(1); df['operating_minutes']=operating_minutes.round(1); df['total_units']=total_units; df['defective_units']=defective_units; df['good_units']=good_units; df['availability']=availability.round(4); df['performance']=performance.round(4); df['quality']=quality.round(4); df['oee']=oee.round(4); df['defect_rate']=(defective_units/total_units).round(4)
    dirty_idx = rng.choice(df.index,size=max(50,n_rows//1000),replace=False)
    df.loc[dirty_idx[:len(dirty_idx)//2],'operator_id']=None
    df.loc[dirty_idx[len(dirty_idx)//2:],'downtime_minutes']=np.nan
    return df.sort_values('date').reset_index(drop=True)


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    output = project_root/'data'/'raw'/'manufacturing_production_raw.csv'
    output.parent.mkdir(parents=True,exist_ok=True)
    df=generate_dataset(); df.to_csv(output,index=False)
    print(f'Dataset generated: {output} ({len(df):,} rows)')


if __name__ == '__main__':
    main()
