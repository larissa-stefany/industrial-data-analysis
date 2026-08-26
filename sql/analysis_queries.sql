-- 1. Overall production KPIs
SELECT
    SUM(total_units) AS total_units,
    SUM(good_units) AS good_units,
    SUM(defective_units) AS defective_units,
    ROUND(100.0 * SUM(defective_units) / SUM(total_units), 2) AS defect_rate_pct,
    ROUND(AVG(oee) * 100, 2) AS avg_oee_pct,
    ROUND(SUM(downtime_minutes) / 60.0, 2) AS downtime_hours
FROM production;

-- 2. Machines with highest defect rate
SELECT
    machine_id,
    SUM(total_units) AS total_units,
    SUM(defective_units) AS defective_units,
    ROUND(100.0 * SUM(defective_units) / SUM(total_units), 2) AS defect_rate_pct,
    ROUND(AVG(oee) * 100, 2) AS avg_oee_pct
FROM production
GROUP BY machine_id
ORDER BY defect_rate_pct DESC;

-- 3. Efficiency by shift
SELECT
    shift,
    SUM(total_units) AS total_units,
    ROUND(AVG(oee) * 100, 2) AS avg_oee_pct,
    ROUND(AVG(availability) * 100, 2) AS availability_pct,
    ROUND(AVG(performance) * 100, 2) AS performance_pct,
    ROUND(AVG(quality) * 100, 2) AS quality_pct,
    ROUND(SUM(downtime_minutes) / 60.0, 2) AS downtime_hours
FROM production
GROUP BY shift
ORDER BY avg_oee_pct DESC;

-- 4. Monthly evolution
SELECT
    month,
    month_name,
    SUM(total_units) AS total_units,
    SUM(defective_units) AS defective_units,
    ROUND(100.0 * SUM(defective_units) / SUM(total_units), 2) AS defect_rate_pct,
    ROUND(AVG(oee) * 100, 2) AS avg_oee_pct
FROM production
GROUP BY month, month_name
ORDER BY month;

-- 5. Downtime versus production by machine
SELECT
    machine_id,
    ROUND(AVG(downtime_minutes), 2) AS avg_downtime_minutes,
    ROUND(AVG(total_units), 2) AS avg_units_per_record,
    ROUND(AVG(oee) * 100, 2) AS avg_oee_pct
FROM production
GROUP BY machine_id
ORDER BY avg_downtime_minutes DESC;

-- 6. Top operators by OEE
SELECT
    operator_id,
    COUNT(*) AS records,
    SUM(good_units) AS good_units,
    ROUND(AVG(oee) * 100, 2) AS avg_oee_pct,
    ROUND(100.0 * SUM(defective_units) / SUM(total_units), 2) AS defect_rate_pct
FROM production
WHERE operator_id <> 'UNKNOWN'
GROUP BY operator_id
HAVING COUNT(*) >= 500
ORDER BY avg_oee_pct DESC
LIMIT 15;

-- 7. Pareto-style ranking of quality losses
WITH machine_losses AS (
    SELECT
        machine_id,
        SUM(defective_units) AS defective_units
    FROM production
    GROUP BY machine_id
),
ranked AS (
    SELECT
        machine_id,
        defective_units,
        SUM(defective_units) OVER (
            ORDER BY defective_units DESC
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS cumulative_defects,
        SUM(defective_units) OVER () AS total_defects
    FROM machine_losses
)
SELECT
    machine_id,
    defective_units,
    ROUND(100.0 * defective_units / total_defects, 2) AS share_of_defects_pct,
    ROUND(100.0 * cumulative_defects / total_defects, 2) AS cumulative_defects_pct
FROM ranked
ORDER BY defective_units DESC;

-- 8. Identify machine-shift combinations below the OEE target
SELECT
    machine_id,
    shift,
    COUNT(*) AS records,
    ROUND(AVG(oee) * 100, 2) AS avg_oee_pct,
    ROUND(100.0 * SUM(defective_units) / SUM(total_units), 2) AS defect_rate_pct,
    ROUND(SUM(downtime_minutes) / 60.0, 2) AS downtime_hours
FROM production
GROUP BY machine_id, shift
HAVING AVG(oee) < 0.75
ORDER BY avg_oee_pct ASC, downtime_hours DESC;

-- 9. Month-over-month OEE change using a window function
WITH monthly AS (
    SELECT
        month,
        month_name,
        AVG(oee) AS avg_oee
    FROM production
    GROUP BY month, month_name
)
SELECT
    month,
    month_name,
    ROUND(avg_oee * 100, 2) AS avg_oee_pct,
    ROUND(
        (avg_oee - LAG(avg_oee) OVER (ORDER BY month)) * 100,
        2
    ) AS oee_change_pp
FROM monthly
ORDER BY month;
