-- 1. Overall production KPIs
SELECT SUM(total_units) AS total_units, SUM(good_units) AS good_units, SUM(defective_units) AS defective_units, ROUND(100.0*SUM(defective_units)/SUM(total_units),2) AS defect_rate_pct, ROUND(AVG(oee)*100,2) AS avg_oee_pct, ROUND(SUM(downtime_minutes)/60.0,2) AS downtime_hours FROM production;

-- 2. Machines with highest defect rate
SELECT machine_id, SUM(total_units) AS total_units, SUM(defective_units) AS defective_units, ROUND(100.0*SUM(defective_units)/SUM(total_units),2) AS defect_rate_pct, ROUND(AVG(oee)*100,2) AS avg_oee_pct FROM production GROUP BY machine_id ORDER BY defect_rate_pct DESC;

-- 3. Efficiency by shift
SELECT shift, SUM(total_units) AS total_units, ROUND(AVG(oee)*100,2) AS avg_oee_pct, ROUND(AVG(availability)*100,2) AS availability_pct, ROUND(AVG(performance)*100,2) AS performance_pct, ROUND(AVG(quality)*100,2) AS quality_pct, ROUND(SUM(downtime_minutes)/60.0,2) AS downtime_hours FROM production GROUP BY shift ORDER BY avg_oee_pct DESC;

-- 4. Monthly evolution
SELECT month, month_name, SUM(total_units) AS total_units, SUM(defective_units) AS defective_units, ROUND(100.0*SUM(defective_units)/SUM(total_units),2) AS defect_rate_pct, ROUND(AVG(oee)*100,2) AS avg_oee_pct FROM production GROUP BY month,month_name ORDER BY month;

-- 5. Downtime versus production by machine
SELECT machine_id, ROUND(AVG(downtime_minutes),2) AS avg_downtime_minutes, ROUND(AVG(total_units),2) AS avg_units_per_record, ROUND(AVG(oee)*100,2) AS avg_oee_pct FROM production GROUP BY machine_id ORDER BY avg_downtime_minutes DESC;

-- 6. Top operators by OEE
SELECT operator_id, COUNT(*) AS records, SUM(good_units) AS good_units, ROUND(AVG(oee)*100,2) AS avg_oee_pct, ROUND(100.0*SUM(defective_units)/SUM(total_units),2) AS defect_rate_pct FROM production WHERE operator_id <> 'UNKNOWN' GROUP BY operator_id HAVING COUNT(*) >= 500 ORDER BY avg_oee_pct DESC LIMIT 15;
