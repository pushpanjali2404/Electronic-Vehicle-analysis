-- ev_sales_kpi.sql
-- Electric Vehicle Sales Analysis - India

-- Total EV Sales
SELECT SUM(EV_Sales_Quantity) AS total_ev_sales
FROM ev_sales;

-- Year-over-Year Growth
WITH yearly_sales AS (
    SELECT
        EXTRACT(YEAR FROM date) AS year,
        SUM(EV_Sales_Quantity) AS total_sales
    FROM ev_sales
    GROUP BY year
)
SELECT
    year,
    total_sales,
    ROUND(
        (total_sales - LAG(total_sales) OVER (ORDER BY year)) * 100.0 /
        LAG(total_sales) OVER (ORDER BY year), 2
    ) AS yoy_growth_pct
FROM yearly_sales;

-- Active States Count
SELECT COUNT(DISTINCT state) AS active_states
FROM ev_sales
WHERE EV_Sales_Quantity > 0;

-- Top State by EV Sales
SELECT state, SUM(EV_Sales_Quantity) AS total_sales
FROM ev_sales
GROUP BY state
ORDER BY total_sales DESC
LIMIT 1;
