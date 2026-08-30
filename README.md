# 🌍 Global Income Inequality Explorer

An interactive data analytics dashboard that explores global income inequality and its relationship with GDP per capita and population across countries and years.

## 📊 Project Overview

This project analyzes real-world World Bank data to understand how income inequality varies across countries and changes over time.

The interactive Streamlit dashboard allows users to:

* Select a country and year
* View the Gini Index
* View GDP per capita
* View population
* Analyze inequality trends over time
* Compare countries using an interactive world map
* Identify countries with the highest reported Gini Index values

## 🎯 Business Objective

The objective is to explore global income inequality and investigate how it varies across countries and over time, while examining its relationship with economic and demographic indicators such as GDP per capita and population.

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
Visualization
        ↓
Streamlit Dashboard
        ↓
GitHub
        ↓
Deployment
```

## 🗂️ Data Sources

The project uses World Bank Open Data for:

* Gini Index
* GDP per capita
* Population

The datasets were cleaned and investigated before being merged into a single analytical dataset.

## 🧹 Data Preparation

The analysis included:

* Handling missing values
* Checking duplicate country-year combinations
* Identifying and removing World Bank aggregate entities
* Standardizing country and year information
* Merging multiple datasets using country codes and year
* Validating the final analytical dataset

## 📈 Dashboard Features

### 1. Country & Year Filters

Users can interactively select a country and year to explore the corresponding indicators.

### 2. KPI Cards

The dashboard displays:

* **Gini Index**
* **GDP per Capita**
* **Population**

### 3. Inequality Trend

An interactive line chart shows how the selected country's Gini Index changes over time.

### 4. Interactive World Map

A choropleth map compares Gini Index values across countries for the selected year.

### 5. Highest Inequality Ranking

A Top 10 bar chart highlights countries with the highest reported Gini Index values for the selected year.

### 6. Automated Trend Insight

The dashboard calculates the change between the earliest and latest available Gini observations for the selected country.

## 🛠️ Technologies Used

### Programming & Data Analysis

* Python
* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib
* Seaborn

### Dashboard

* Streamlit

### Development

* Jupyter Notebook
* VS Code
* Git
* GitHub

## 📁 Project Structure

```text
Global-Income-Inequality/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
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

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
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

Windows PowerShell:

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

## 🌐 Live Dashboard

**Streamlit App:** YOUR_STREAMLIT_APP_URL

## 💡 Key Skills Demonstrated

* Data collection from public APIs
* Data cleaning
* Data validation
* Missing-value handling
* Duplicate investigation
* Aggregate/entity identification
* Dataset merging
* Exploratory Data Analysis
* KPI development
* Time-series analysis
* Geographic analysis
* Interactive visualization
* Dashboard development
* Git/GitHub version control
* Streamlit deployment

## 📌 Project Outcome

This project transforms multiple World Bank datasets into an interactive analytical dashboard that makes it easier to explore global inequality patterns and compare countries across different years.

## 👩‍💻 Author

**Revathi Tamarana**

B.Tech Information Technology Student

Interested in Data Analytics and Business Analytics.
