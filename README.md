# 🌍 Global Seismic Trends Analysis

## 📌 Project Overview

This project analyzes global earthquake data using Python, MySQL, SQL, and Streamlit.

The objective is to:
- Clean and preprocess earthquake data
- Store cleaned data in MySQL
- Perform analytical SQL queries
- Generate insights on seismic activity
- Visualize earthquake trends using Streamlit dashboards

---

# 📂 Dataset Source

Earthquake data was collected from the USGS Earthquake API.

The dataset includes:
- Magnitude
- Depth
- Location
- Tsunami alerts
- Event types
- Network information
- Seismic quality metrics
- Time and date information

---

# 🛠️ Technologies Used

- Python
- Pandas
- Regex
- MySQL
- SQLAlchemy
- Streamlit
- Matplotlib
- VS Code

---

# ⚙️ Data Preprocessing

The following preprocessing steps were performed:

- Converted datetime columns
- Cleaned string and categorical fields
- Extracted countries using Regex
- Converted numeric fields
- Handled missing values
- Created derived features:
  - Year
  - Month
  - Day
  - Day of week
  - Shallow/Deep earthquake classification
  - Strong earthquake flags

---

# 🗄️ Database Integration

The cleaned dataset was stored in MySQL using SQLAlchemy.

Database:
```text
seismic_db

Table:
earthquakes

📊 Analytical SQL Queries

The project includes SQL analysis for:

Magnitude & Depth Analysis
Strongest earthquakes
Deepest earthquakes
Shallow high-magnitude earthquakes
Average depth by continent
Average magnitude by magType
Time Analysis
Yearly earthquake trends
Monthly earthquake frequency
Day-wise activity
Hourly activity
Reporting network analysis
Event Metrics
Review status analysis
Earthquake type distribution
Data type analysis
High station coverage events
Tsunami & Alert Analysis
Tsunami events per year
Alert level distribution
Tsunami vs non-tsunami magnitude comparison
Seismic Trend Analysis
Most active regions
Year-over-year growth
Mixed depth earthquake analysis
Average magnitude by country
Advanced Analysis
Equatorial earthquake depth analysis
Shallow-to-deep earthquake ratios
Low reliability seismic events
Deep-focus earthquake regions

📈 Streamlit Dashboard

An interactive Streamlit dashboard was developed to visualize:

Earthquake trends
Magnitude analysis
Time analysis
Tsunami activity
Seismic patterns
Reliability metrics

📷 Dashboard Screenshots
Overview

Magnitude & Depth

Time Analysis

Event Metrics

Tsunami & Alerts

Seismic Trends

Advanced Analysis

🚀 How to Run the Project
Clone Repository
git clone <repository_link>
Install Requirements
pip install -r requirements.txt
Run Streamlit App
streamlit run app.py

📌 Key Insights
Most earthquakes are shallow-focus events
High magnitude earthquakes are relatively rare
Pacific regions show intense seismic activity
Tsunami-triggering earthquakes generally have higher magnitudes
Deep-focus earthquakes are concentrated in specific tectonic regions

👨‍💻 Author

Ajith Balaji