# Data Dictionary

This project uses a synthetic manufacturing dataset designed to reproduce common production, quality and efficiency scenarios.

| Column | Type | Description |
|---|---|---|
| `date` | date | Production date |
| `machine_id` | string | Unique machine identifier |
| `shift` | string | Production shift |
| `operator_id` | string | Operator identifier |
| `planned_minutes` | numeric | Planned production time |
| `downtime_minutes` | numeric | Unplanned/recorded downtime |
| `runtime_minutes` | numeric | Effective runtime |
| `ideal_cycle_time_seconds` | numeric | Ideal time required per unit |
| `total_units` | integer | Total units produced |
| `defective_units` | integer | Units classified as defective |
| `good_units` | integer | Accepted units after quality losses |
| `availability` | numeric | Runtime divided by planned production time |
| `performance` | numeric | Production speed relative to ideal cycle time |
| `quality` | numeric | Good units divided by total units |
| `oee` | numeric | Availability × Performance × Quality |
| `month` | integer | Numeric month used for chronological sorting |
| `month_name` | string | Month label used in reporting |

## KPI definitions

### Defect Rate

```text
defective_units / total_units
```

Measures the proportion of output that fails quality requirements.

### Availability

```text
runtime_minutes / planned_minutes
```

Indicates how much of the scheduled production time the asset was actually running.

### Performance

Compares the actual output with the theoretical production capacity based on ideal cycle time.

### Quality

```text
good_units / total_units
```

Measures the share of production accepted as good output.

### OEE

```text
availability × performance × quality
```

Overall Equipment Effectiveness combines the three main manufacturing loss dimensions into one operational indicator.

## Notes

- All records are synthetic and do not represent any real company.
- Machine and operator identifiers are fictitious.
- Values are generated with controlled variability to create realistic analytical scenarios such as quality loss, downtime and differences between shifts.
