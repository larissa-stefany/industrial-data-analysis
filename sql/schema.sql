DROP TABLE IF EXISTS production;

CREATE TABLE production (
    date TEXT NOT NULL,
    machine_id TEXT NOT NULL,
    line TEXT NOT NULL,
    product TEXT NOT NULL,
    shift TEXT NOT NULL,
    operator_id TEXT,
    planned_minutes REAL NOT NULL,
    downtime_minutes REAL NOT NULL,
    operating_minutes REAL NOT NULL,
    total_units INTEGER NOT NULL,
    defective_units INTEGER NOT NULL,
    good_units INTEGER NOT NULL,
    availability REAL NOT NULL,
    performance REAL NOT NULL,
    quality REAL NOT NULL,
    oee REAL NOT NULL,
    defect_rate REAL NOT NULL,
    year INTEGER,
    month INTEGER,
    month_name TEXT,
    week INTEGER,
    day_of_week TEXT
);
