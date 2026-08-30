# 🌍 Global Income Inequality Explorer

An interactive data analytics dashboard that explores **global income inequality** and its relationship with **GDP per capita and population** across countries and years.

🔗 **Live Dashboard:** Add your Streamlit app URL here https://global-income-inequality-explorer-su62ysz3k5wxe37ukxq77m.streamlit.app/

---

## 📊 Project Overview

This project uses real-world **World Bank Open Data** to analyze how income inequality varies across countries and changes over time.

The project combines three major indicators:

* **Gini Index** — measure of income inequality
* **GDP per Capita** — indicator of economic development
* **Population** — demographic indicator

The final result is an interactive **Streamlit dashboard** that allows users to explore inequality patterns at both country and global levels.

---

## 🎯 Business Objective

The objective is to understand:

* How income inequality varies between countries
* How inequality changes over time
* How inequality relates to GDP per capita
* Which countries report the highest Gini Index values
* How economic and demographic indicators differ across countries

---

## 🔄 Project Workflow

```text
World Bank Open Data
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
Aggregate Entity Removal
        ↓
Duplicate Investigation
        ↓
Dataset Merging
        ↓
Exploratory Data Analysis
        ↓
Data Visualization
        ↓
Streamlit Dashboard
        ↓
GitHub
        ↓
Streamlit Community Cloud
```

---

## 🗂️ Data Sources

The project uses **World Bank Open Data** for:

* Gini Index
* GDP per capita
* Population

The individual datasets were cleaned, validated, and merged using **country codes and year**.

World Bank aggregate entities such as income groups were identified and removed before country-level analysis.

---

## 🧹 Data Preparation

The data preparation process included:

* Handling missing values
* Standardizing country and year information
* Investigating duplicate country-year combinations
* Identifying World Bank aggregate entities
* Removing aggregate entities from country-level analysis
* Merging datasets using country codes and year
* Validating the final analytical dataset

This ensured that the final dataset contained meaningful country-level observations for analysis.

---

## 📈 Dashboard Features

### 1. 🌍 Country & Year Filters

Users can select a country and an available year from the sidebar.

The dashboard dynamically updates based on the selected values.

### 2. 📌 KPI Cards

The dashboard displays:

* Gini Index
* GDP per Capita
* Population

for the selected country and year.

### 3. 📈 Inequality Trend

An interactive line chart shows how the selected country's **Gini Index changes over time**.

The dashboard also provides an automated insight comparing the earliest and latest available Gini observations.

### 4. 🗺️ Interactive World Map

A choropleth map compares Gini Index values across countries for the selected year.

Users can hover over countries to inspect their reported Gini values.

### 5. 📊 Highest Inequality Ranking

A Top 10 bar chart identifies countries with the highest reported Gini Index values for the selected year.

### 6. ℹ️ Dashboard Guidance

An expandable section explains how users can interact with and interpret the dashboard.

---

## 🖼️ Dashboard Screenshots

### Dashboard Overview

![Dashboard Overview](screenshots/dashboard-overview.png)

### Country Analysis

![Country Analysis](screenshots/country-analysis.png)

### World Map

![World Map](screenshots/world-map.png)

### Top 10 Inequality Ranking

![Top 10 Inequality Ranking](screenshots/top-10-inequality.png)

---

## 🛠️ Technologies Used

### Programming & Data Analysis

* Python
* Pandas
* NumPy

### Data Visualization

* Plotly
* Matplotlib
* Seaborn

### Dashboard

* Streamlit

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 📁 Project Structure

```text
Global-Income-Inequality/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── dashboard-overview.png
│   ├── country-analysis.png
│   ├── world-map.png
│   └── top-10-inequality.png
│
├── data/
│   └── master_inequality_dataset.csv
│
├── notebooks/
│   ├── 01_gini_data.ipynb
│   ├── 02_gdp_data.ipynb
│   ├── 03_population_data.ipynb
│   └── 04_merge_analysis.ipynb
│
└── .streamlit/
    └── config.toml
```

---

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://global-income-inequality-explorer-su62ysz3k5wxe37ukxq77m.streamlit.app/
```

### 2. Navigate into the project

```bash
cd Global-Income-Inequality
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## 📊 Key Analytical Questions

This project was designed to answer questions such as:

* Which countries have the highest reported inequality?
* How does inequality change over time?
* How does GDP per capita differ between countries?
* How do population sizes vary across countries?
* What inequality patterns can be observed globally?

---

## 💡 Key Data Analyst Skills Demonstrated

This project demonstrates practical experience with:

* Data collection from public sources
* Data cleaning and preprocessing
* Missing-value handling
* Duplicate investigation
* Data validation
* Dataset integration
* Exploratory Data Analysis
* Data visualization
* KPI development
* Interactive dashboard development
* Git/GitHub version control
* Cloud deployment

---

## 👩‍💻 Author

**Revathi Tamarana**

B.Tech — Information Technology

Interested in **Data Analytics, Business Analytics, and AI-powered analytics**.

---

## ⭐ Project Highlights

**End-to-end Data Analytics Project**

```text
Raw Data → Cleaning → Analysis → Visualization
                    ↓
             Interactive Dashboard
                    ↓
               Deployment
```

If you found this project useful, consider giving the repository a ⭐.
