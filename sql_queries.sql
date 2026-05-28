-- Q1 Top 10 Strongest Earthquakes
SELECT place, country, mag, depth_km, continent, time
FROM earthquakes
ORDER BY mag DESC
LIMIT 10;

-- Q2 - Top 10 Deepest Earthquakes
SELECT place, country, depth_km, mag, continent, time
FROM earthquakes
ORDER BY depth_km DESC
LIMIT 10;

-- Q3 - Shallow Earthquakes (<50 KM) and Mag > 7.5
SELECT place, country, mag, depth_km, continent, time
FROM earthquakes
WHERE depth_km < 50
AND mag > 7.5
ORDER BY mag DESC;

-- Q4 - Average Depth per continent
SELECT continent,
       ROUND(AVG(depth_km),2) AS avg_depth
FROM earthquakes
GROUP BY continent
ORDER BY avg_depth DESC;

-- Q5 - Average Magnitude per Magnitude Type (magType)
SELECT magType,
       ROUND(AVG(mag),2) AS avg_magnitude,
       COUNT(*) AS total_events
FROM earthquakes
GROUP BY magType
ORDER BY avg_magnitude DESC;

-- Q6 — Year with Most Earthquakes
SELECT year,
       COUNT(*) AS total_earthquakes
FROM earthquakes
GROUP BY year
ORDER BY total_earthquakes DESC;

-- Q7 — Month with Highest Number of Earthquakes
SELECT month,
       COUNT(*) AS total_earthquakes
FROM earthquakes
GROUP BY month
ORDER BY total_earthquakes DESC;

-- Q8 — Day of Week with Most Earthquakes
SELECT day_of_week,
       COUNT(*) AS total_earthquakes
FROM earthquakes
GROUP BY day_of_week
ORDER BY total_earthquakes DESC;

-- Q9 — Count of Earthquakes per Hour of Day
SELECT HOUR(time) AS hour_of_day,
       COUNT(*) AS total_earthquakes
FROM earthquakes
GROUP BY hour_of_day
ORDER BY hour_of_day;

-- Q10 — Most Active Reporting Network (net)
SELECT net,
       COUNT(*) AS total_reports
FROM earthquakes
GROUP BY net
ORDER BY total_reports DESC;
-------------
-- Q11 — Top 5 Places with Highest Casualties
SELECT place,
       country,
       mag,
       felt,
       casualties
FROM earthquakes
ORDER BY casualties DESC
LIMIT 5;
-- Q14 — Count of Reviewed vs Automatic Earthquakes
SELECT
    status,
    COUNT(*) AS total_events
FROM earthquakes
GROUP BY status
ORDER BY total_events DESC;

-- Q15 — Count by Earthquake Type
SELECT
    type,
    COUNT(*) AS total_events
FROM earthquakes
GROUP BY type
ORDER BY total_events DESC;

-- Q16 — Number of Earthquakes by Data Type
SELECT
    types,
    COUNT(*) AS total_events
FROM earthquakes
GROUP BY types
ORDER BY total_events DESC
LIMIT 10;

-- Q18 — Events with High Station Coverage
SELECT
    place,
    country,
    mag,
    nst
FROM earthquakes
WHERE nst > 100
ORDER BY nst DESC;

-- Q19 — Number of Tsunamis Triggered per Year
SELECT
    year,
    COUNT(*) AS tsunami_events
FROM earthquakes
WHERE tsunami = 1
GROUP BY year
ORDER BY year;

-- Q20 — Count Earthquakes by Alert Levels
SELECT
    alert,
    COUNT(*) AS total_events
FROM earthquakes
GROUP BY alert
ORDER BY total_events DESC;

-- Q21 — Top 5 Countries with Highest Average Magnitude
SELECT
    country,
    ROUND(AVG(mag),2) AS avg_magnitude,
    COUNT(*) AS total_earthquakes
FROM earthquakes
GROUP BY country
HAVING COUNT(*) > 10
ORDER BY avg_magnitude DESC
LIMIT 5;

-- Q22 — Countries with Both Shallow and Deep Earthquakes in Same Month
SELECT DISTINCT
    e1.country,
    e1.year,
    e1.month
FROM earthquakes e1
JOIN earthquakes e2
ON e1.country = e2.country
AND e1.year = e2.year
AND e1.month = e2.month

WHERE e1.depth_km < 70
AND e2.depth_km > 300;

-- Q23 — Year-over-Year Growth Rate
SELECT
    year,

    COUNT(*) AS total_earthquakes,

    LAG(COUNT(*)) OVER (ORDER BY year) AS previous_year,

    ROUND(
        (
            (COUNT(*) - LAG(COUNT(*)) OVER (ORDER BY year))
            /
            LAG(COUNT(*)) OVER (ORDER BY year)
        ) * 100,
        2
    ) AS growth_rate_percentage

FROM earthquakes

GROUP BY year
ORDER BY year;

-- Q24 — Most Seismically Active Regions
SELECT
    country,

    COUNT(*) AS total_earthquakes,

    ROUND(AVG(mag),2) AS avg_magnitude,

    ROUND(
        COUNT(*) * AVG(mag),
        2
    ) AS seismic_activity_score

FROM earthquakes

GROUP BY country

HAVING COUNT(*) > 20

ORDER BY seismic_activity_score DESC
LIMIT 5;

-- Q25 — Average Depth Near Equator (±5° Latitude)
SELECT
    country,

    ROUND(AVG(depth_km),2) AS avg_depth

FROM earthquakes

WHERE latitude BETWEEN -5 AND 5

GROUP BY country

ORDER BY avg_depth DESC;

-- Q26 — Highest Ratio of Shallow to Deep Earthquakes
SELECT

    country,

    SUM(CASE WHEN depth_km < 50 THEN 1 ELSE 0 END) AS shallow_count,

    SUM(CASE WHEN depth_km > 50 THEN 1 ELSE 0 END) AS deep_count,

    ROUND(
        SUM(CASE WHEN depth_km < 50 THEN 1 ELSE 0 END)
        /
        NULLIF(
            SUM(CASE WHEN depth_km > 50 THEN 1 ELSE 0 END),
            0
        ),
        2
    ) AS shallow_deep_ratio

FROM earthquakes

GROUP BY country

HAVING deep_count > 0

ORDER BY shallow_deep_ratio DESC;

-- Q27 — Average Magnitude: Tsunami vs Non-Tsunami
SELECT

    tsunami,

    ROUND(AVG(mag),2) AS avg_magnitude,

    COUNT(*) AS total_events

FROM earthquakes

GROUP BY tsunami;

-- Q28 — Lowest Data Reliability Events
SELECT

    place,
    country,
    mag,
    gap,
    rms,

    ROUND((gap + rms)/2,2) AS reliability_error_score

FROM earthquakes

ORDER BY reliability_error_score DESC
LIMIT 10;

-- Q30 — Regions with Highest Deep-Focus Earthquakes
SELECT

    country,

    COUNT(*) AS deep_focus_earthquakes

FROM earthquakes

WHERE depth_km > 50

GROUP BY country

ORDER BY deep_focus_earthquakes DESC;