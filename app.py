import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sqlalchemy import create_engine

st.title("🌍 Global Seismic Trends Dashboard")

st.write("Data-Driven Earthquake Insights")

engine = create_engine(
    "mysql+pymysql://root:1997@localhost/seismic_db"
)

query = "SELECT * FROM earthquakes LIMIT 5"

df = pd.read_sql(query, engine)

st.dataframe(df)

st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go To",
    [
        "Overview",
        "Magnitude & Depth",
        "Time Analysis",
        "Event Metrics",
        "Tsunami & Alerts",
        "Seismic Trends",
        "Advanced Analysis"
    ]
)

if section == "Overview":

    st.header("Project Overview")
    total_query = "SELECT COUNT(*) AS total FROM earthquakes"
    total_df = pd.read_sql(total_query, engine)

    maxmag_query = "SELECT MAX(mag) AS max_mag FROM earthquakes"
    maxmag_df = pd.read_sql(maxmag_query, engine)

    tsunami_query = """
    SELECT COUNT(*) AS tsunami_count
    FROM earthquakes
    WHERE tsunami = 1
    """
    tsunami_df = pd.read_sql(tsunami_query, engine)

    country_query = """
    SELECT COUNT(DISTINCT country) AS total_countries
    FROM earthquakes
    """
    country_df = pd.read_sql(country_query, engine)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Earthquakes",
        int(total_df['total'][0])
    )

    col2.metric(
        "Maximum Magnitude",
        round(maxmag_df['max_mag'][0],2)
    )

    col3.metric(
        "Tsunami Events",
        int(tsunami_df['tsunami_count'][0])
    )

    col4.metric(
        "Countries & Regions affected",
        int(country_df['total_countries'][0])
    )

elif section == "Magnitude & Depth":

    st.header("Magnitude & Depth Analysis")

    query1 = """
    SELECT place, country, mag
    FROM earthquakes
    ORDER BY mag DESC
    LIMIT 10
    """

    top_mag = pd.read_sql(query1, engine)

    st.subheader("1.Top 10 Strongest Earthquakes")

    st.dataframe(top_mag)

    fig, ax = plt.subplots(figsize=(12,5))

    ax.bar(top_mag['country'], top_mag['mag'])

    plt.xticks(rotation=90)

    plt.ylabel("Magnitude")

    st.pyplot(fig)
    st.divider()

    query2 = """
    SELECT place, depth_km, country
    FROM earthquakes
    ORDER BY depth_km DESC
    LIMIT 10
    """

    top_depth = pd.read_sql(query2, engine)

    st.subheader("2.Top 10 Deepest Earthquakes")

    st.dataframe(top_depth)

    fig, ax = plt.subplots(figsize=(12,5))

    ax.bar(top_depth['country'], top_depth['depth_km'])

    plt.xticks(rotation=90)

    plt.ylabel("Depth (km)")

    st.pyplot(fig)
    st.divider()

    query3 = """
    SELECT country, mag, depth_km
    FROM earthquakes
    WHERE depth_km < 50
    AND mag > 7.5
    ORDER BY mag DESC
    """

    shallow_strong = pd.read_sql(query3, engine)

    st.subheader("3.Shallow Earthquakes with Magnitude > 7.5")

    st.dataframe(shallow_strong)

    query4 = """
    SELECT continent,
           AVG(depth_km) AS avg_depth
    FROM earthquakes
    GROUP BY continent
    """

    continent_depth = pd.read_sql(query4, engine)

    st.subheader("4.Average Depth per Continent")

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        continent_depth['continent'],
        continent_depth['avg_depth']
    )

    plt.xticks(rotation=45)

    plt.ylabel("Average Depth")

    st.pyplot(fig)
    st.divider()

    query5 = """
    SELECT magType,
           AVG(mag) AS avg_mag
    FROM earthquakes
    GROUP BY magType
    ORDER BY avg_mag DESC
    """

    magtype_df = pd.read_sql(query5, engine)

    st.subheader("5.Average Magnitude by Magnitude Type")

    st.dataframe(magtype_df)
    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        magtype_df['magType'],
        magtype_df['avg_mag']
    )

    plt.xticks(rotation=45)

    plt.ylabel("Average Magnitude")

    st.pyplot(fig)
    st.divider()

elif section == "Time Analysis":

    st.header("Time Analysis")

    query6 = """
    SELECT year,
           COUNT(*) AS total_earthquakes
    FROM earthquakes
    GROUP BY year
    ORDER BY total_earthquakes DESC
    """

    yearly_df = pd.read_sql(query6, engine)

    st.subheader("6.Earthquakes by Year")


    yearly_df = yearly_df.sort_values(by='year')

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(
       yearly_df['year'],
       yearly_df['total_earthquakes'],
       marker='o',
       linewidth=3
    )


    ax.set_xticks(yearly_df['year'])

    plt.xlabel("Year")
    plt.ylabel("Total Earthquakes")
    plt.title("Yearly Earthquake Trend")

    plt.grid(True)

    st.pyplot(fig)
    st.divider()

    query7 = """
    SELECT month,
           COUNT(*) AS total_earthquakes
    FROM earthquakes
    GROUP BY month
    ORDER BY total_earthquakes
    """

    monthly_df = pd.read_sql(query7, engine)

    st.subheader("7.Earthquakes by Month")

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        monthly_df['month'],
        monthly_df['total_earthquakes']
    )

    plt.xlabel("Month")
    plt.ylabel("Earthquake Count")

    st.pyplot(fig)
    st.divider()

    query8 = """
    SELECT day_of_week,
           COUNT(*) AS total_earthquakes
    FROM earthquakes
    GROUP BY day_of_week
    ORDER BY total_earthquakes DESC
    """

    day_df = pd.read_sql(query8, engine)

    st.subheader("8.Earthquakes by Day of Week")

    st.dataframe(day_df)
    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        day_df['day_of_week'],
        day_df['total_earthquakes']
    )

    plt.xticks(rotation=45)

    plt.ylabel("Earthquake Count")

    st.pyplot(fig)
    st.divider()

    query9 = """
    SELECT hour,
           COUNT(*) AS total_earthquakes
    FROM earthquakes
    GROUP BY hour
    ORDER BY hour
    """

    hour_df = pd.read_sql(query9, engine)

    st.subheader("9.Earthquakes by Hour of Day")

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(
        hour_df['hour'],
        hour_df['total_earthquakes'],
        marker='o'
    )

    plt.xlabel("Hour")
    plt.ylabel("Earthquake Count")

    st.pyplot(fig)
    st.divider()

    query10 = """
    SELECT net,
           COUNT(*) AS total_reports
    FROM earthquakes
    GROUP BY net
    ORDER BY total_reports DESC
    LIMIT 10
    """

    net_df = pd.read_sql(query10, engine)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        net_df['net'],
        net_df['total_reports']
    )

    plt.xticks(rotation=45)

    plt.ylabel("Reports")

    st.pyplot(fig)
    st.divider()

elif section == "Event Metrics":

    st.header("Event Type & Quality Metrics")

    query11 = """
    SELECT place,
           mag,
           felt,
           casualties
    FROM earthquakes
    ORDER BY casualties DESC
    LIMIT 5
    """

    casualty_df = pd.read_sql(query11, engine)

    st.subheader("11.Top 5 Places with Highest Casualties")

    st.dataframe(casualty_df)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        casualty_df['place'],
        casualty_df['casualties']
    )

    plt.xticks(rotation=45)

    plt.ylabel("Estimated Casualties")

    st.pyplot(fig)
    st.divider()


    query14 = """
    SELECT status,
           COUNT(*) AS total_events
    FROM earthquakes
    GROUP BY status
    """

    status_df = pd.read_sql(query14, engine)

    st.subheader("14.Reviewed vs Automatic Earthquakes")

    st.dataframe(status_df)

    fig, ax = plt.subplots(figsize=(6,6))

    ax.pie(
        status_df['total_events'],
        labels=status_df['status'],
        autopct='%1.1f%%'
    )

    plt.title("Earthquake Review Status")

    st.pyplot(fig)
    st.divider()

    query15 = """
    SELECT type,
           COUNT(*) AS total_events
    FROM earthquakes
    GROUP BY type
    ORDER BY total_events DESC
    """

    type_df = pd.read_sql(query15, engine)

    st.subheader("15.Earthquake Count by Type")

    st.dataframe(type_df)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        type_df['type'],
        type_df['total_events']
    )

    plt.xticks(rotation=45)

    plt.ylabel("Count")

    st.pyplot(fig)
    st.divider()

    query16 = """
    SELECT types,
           COUNT(*) AS total_events
    FROM earthquakes
    GROUP BY types
    ORDER BY total_events DESC
    LIMIT 10
    """

    types_df = pd.read_sql(query16, engine)

    st.subheader("16.Top Data Types")

    st.dataframe(types_df)

    fig, ax = plt.subplots(figsize=(12,5))

    ax.bar(
        types_df['types'],
        types_df['total_events']
    )

    plt.xticks(rotation=90)

    plt.ylabel("Count")

    st.pyplot(fig)
    st.divider()

    query18 = """
    SELECT place,
           country,
           mag,
           nst
    FROM earthquakes
    WHERE nst > 100
    ORDER BY nst DESC
    LIMIT 20
    """

    nst_df = pd.read_sql(query18, engine)

    st.subheader("18.High Station Coverage Events")

    st.dataframe(nst_df)

    fig, ax = plt.subplots(figsize=(12,5))

    ax.bar(
        nst_df['country'],
        nst_df['nst']
    )

    plt.xticks(rotation=90)

    plt.ylabel("Number of Stations")

    st.pyplot(fig)
    st.divider()

elif section == "Tsunami & Alerts":

    st.header("Tsunami & Alerts Analysis")

    query19 = """
    SELECT year,
           COUNT(*) AS tsunami_events
    FROM earthquakes
    WHERE tsunami = 1
    GROUP BY year
    ORDER BY year
    """

    tsunami_year_df = pd.read_sql(query19, engine)

    st.subheader("19.Tsunami Events Per Year")

    st.dataframe(tsunami_year_df)

    fig, ax = plt.subplots(figsize=(10,5))

    tsunami_year_df = tsunami_year_df.sort_values(by='year')

    ax.plot(
        tsunami_year_df['year'],
        tsunami_year_df['tsunami_events'],
        marker='o',
        linewidth=3
    )

    ax.set_xticks(tsunami_year_df['year'])

    plt.xlabel("Year")
    plt.ylabel("Tsunami Events")
    plt.title("Yearly Tsunami Trend")

    plt.grid(True)

    st.pyplot(fig)
    st.divider()

    query20 = """
    SELECT alert,
           COUNT(*) AS total_alerts
    FROM earthquakes
    GROUP BY alert
    """

    alert_df = pd.read_sql(query20, engine)

    alert_chart_df = alert_df[
    alert_df['alert'] != 'unknown'
]

    st.subheader("20.Earthquake Alert Levels")

    st.dataframe(alert_df)

    fig, ax = plt.subplots(figsize=(8,5))

    ax.bar(
    alert_chart_df['alert'],
    alert_chart_df['total_alerts']
    )

    plt.xlabel("Alert Level")
    plt.ylabel("Count")
    plt.title("Official Earthquake Alert Levels")

    st.pyplot(fig)
    st.divider()


    query27 = """
    SELECT tsunami,
           AVG(mag) AS avg_magnitude
    FROM earthquakes
    GROUP BY tsunami
    """

    tsunami_mag_df = pd.read_sql(query27, engine)

    tsunami_mag_df['tsunami'] = tsunami_mag_df['tsunami'].replace({
        0: 'No Tsunami',
        1: 'Tsunami'
    })

    st.subheader("27.Average Magnitude: Tsunami vs Non-Tsunami")

    st.dataframe(tsunami_mag_df)

    fig, ax = plt.subplots(figsize=(8,5))

    ax.bar(
        tsunami_mag_df['tsunami'],
        tsunami_mag_df['avg_magnitude']
    )

    plt.ylabel("Average Magnitude")

    plt.title("Magnitude Comparison")

    st.pyplot(fig)
    st.divider()

elif section == "Seismic Trends":

    st.header("Seismic Pattern & Trends Analysis")

    query21 = """
    SELECT country,
           AVG(mag) AS avg_magnitude
    FROM earthquakes
    WHERE country != 'Unknown'
    GROUP BY country
    HAVING COUNT(*) > 10
    ORDER BY avg_magnitude DESC
    LIMIT 5
    """

    top_country_df = pd.read_sql(query21, engine)

    st.subheader("21.Top 5 Countries by Average Magnitude")

    st.dataframe(top_country_df)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        top_country_df['country'],
        top_country_df['avg_magnitude']
    )

    plt.ylabel("Average Magnitude")

    plt.title("Highest Average Magnitude Countries")

    st.pyplot(fig)
    st.divider()

    query22 = """
    SELECT DISTINCT a.country,
                    a.year,
                    a.month
    FROM earthquakes a
    JOIN earthquakes b
        ON a.country = b.country
        AND a.year = b.year
        AND a.month = b.month
    WHERE a.depth_km < 70
      AND b.depth_km > 300
      AND a.country != 'Unknown'
    """

    mixed_depth_df = pd.read_sql(query22, engine)

    st.subheader("22.Countries Experiencing Both Shallow & Deep Earthquakes")

    st.dataframe(mixed_depth_df.head(20))

    query23 = """
    SELECT year,
           COUNT(*) AS total_earthquakes
    FROM earthquakes
    GROUP BY year
    ORDER BY year
    """

    yoy_df = pd.read_sql(query23, engine)

    yoy_df['growth_rate'] = (
        yoy_df['total_earthquakes']
        .pct_change() * 100
    )

    st.subheader("23.Year-over-Year Earthquake Growth")

    st.dataframe(yoy_df)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(
        yoy_df['year'],
        yoy_df['growth_rate'],
        marker='o',
        linewidth=3
    )

    ax.set_xticks(yoy_df['year'])

    plt.xlabel("Year")
    plt.ylabel("Growth Rate (%)")

    plt.title("Year-over-Year Growth Rate")

    plt.grid(True)

    st.pyplot(fig)
    st.divider()

    query24 = """
    SELECT country,
           COUNT(*) AS earthquake_count,
           AVG(mag) AS avg_magnitude
    FROM earthquakes
    WHERE country != 'Unknown'
    GROUP BY country
    ORDER BY earthquake_count DESC,
             avg_magnitude DESC
    LIMIT 10
    """

    active_region_df = pd.read_sql(query24, engine)

    st.subheader("24.Most Seismically Active Regions")

    st.dataframe(active_region_df)

    fig, ax = plt.subplots(figsize=(12,5))

    ax.bar(
        active_region_df['country'],
        active_region_df['earthquake_count']
    )

    plt.xticks(rotation=45)

    plt.ylabel("Earthquake Count")

    plt.title("Most Active Seismic Regions")

    st.pyplot(fig)
    st.divider()

elif section == "Advanced Analysis":

    st.header("Advanced Seismic Analysis")

    query25 = """
    SELECT country,
           AVG(depth_km) AS avg_depth
    FROM earthquakes
    WHERE latitude BETWEEN -5 AND 5
      AND country != 'Unknown'
    GROUP BY country
    ORDER BY avg_depth DESC
    LIMIT 10
    """

    equator_df = pd.read_sql(query25, engine)

    st.subheader("25.Average Earthquake Depth Near Equator")

    st.dataframe(equator_df)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        equator_df['country'],
        equator_df['avg_depth']
    )

    plt.xticks(rotation=45)

    plt.ylabel("Average Depth (km)")

    plt.title("Equatorial Earthquake Depth")

    st.pyplot(fig)
    st.divider()

    query26 = """
    SELECT

        country,

        SUM(CASE
                WHEN depth_km < 50 THEN 1
                ELSE 0
            END) AS shallow_count,

        SUM(CASE
                WHEN depth_km > 50 THEN 1
                ELSE 0
            END) AS deep_count,

        ROUND(
            SUM(CASE
                    WHEN depth_km < 50 THEN 1
                    ELSE 0
                END)

            /

            NULLIF(
                SUM(CASE
                        WHEN depth_km > 50 THEN 1
                        ELSE 0
                    END),
                0
            ),

            2

        ) AS shallow_deep_ratio

    FROM earthquakes

    WHERE country != 'Unknown'

    GROUP BY country

    HAVING deep_count > 0

    ORDER BY shallow_deep_ratio DESC

    LIMIT 10
    """

    ratio_df = pd.read_sql(query26, engine)


    st.subheader("26.Countries with Highest Shallow-to-Deep Ratio")

    st.dataframe(ratio_df)

    fig, ax = plt.subplots(figsize=(12,5))

    ax.bar(
        ratio_df['country'],
        ratio_df['shallow_deep_ratio']
    )

    plt.xticks(rotation=45)

    plt.ylabel("Shallow / Deep Ratio")

    plt.title("Shallow-to-Deep Earthquake Ratio")

    st.pyplot(fig)
    st.divider()

    query28 = """
    SELECT place,
           mag,
           gap,
           rms,
           ((gap + rms)/2) AS reliability_score
    FROM earthquakes
    WHERE gap IS NOT NULL
      AND rms IS NOT NULL
    ORDER BY reliability_score DESC
    LIMIT 20
    """

    reliability_df = pd.read_sql(query28, engine)

    st.subheader("28.Events with Lowest Data Reliability")

    st.dataframe(reliability_df)

    fig, ax = plt.subplots(figsize=(12,5))

    ax.bar(
        reliability_df['place'],
        reliability_df['reliability_score']
    )

    plt.xticks(rotation=90)

    plt.ylabel("Reliability Error Score")

    plt.title("Lowest Reliability Seismic Events")

    st.pyplot(fig)
    st.divider()

    query30 = """
    SELECT country,
           COUNT(*) AS deep_focus_count
    FROM earthquakes
    WHERE depth_km > 300
      AND country != 'Unknown'
    GROUP BY country
    ORDER BY deep_focus_count DESC
    LIMIT 10
    """

    deep_focus_df = pd.read_sql(query30, engine)

    st.subheader("30.Regions with Most Deep-Focus Earthquakes")

    st.dataframe(deep_focus_df)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        deep_focus_df['country'],
        deep_focus_df['deep_focus_count']
    )

    plt.xticks(rotation=45)

    plt.ylabel("Deep Focus Earthquakes")

    plt.title("Deep-Focus Seismic Regions")

    st.pyplot(fig)

    st.divider()
    st.divider()

st.caption(
    "Global Seismic Trends Dashboard | Built using Python, MySQL, Streamlit, and SQL Analytics"
)
