
import streamlit as st
import pandas as pd
import plotly.express as px


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Global Income Inequality Explorer",
    page_icon="🌍",
    layout="wide"
)


# -----------------------------
# Load data
# -----------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/master_inequality_dataset.csv"
    )


master = load_data()

# Make sure Year is an integer
master["Year"] = master["Year"].astype(int)


# -----------------------------
# Title
# -----------------------------

st.title("🌍 Global Income Inequality Explorer")

st.markdown(
    """
    Explore how income inequality varies across countries and
    changes over time, and examine its relationship with
    GDP per capita.
    """
)

st.caption(
    "Data source: World Bank Open Data | "
    "Gini Index, GDP per capita and Population"
)

st.info(
    "The Gini Index measures income inequality. "
    "Higher values indicate greater inequality."
)


# -----------------------------
# Dataset Overview
# -----------------------------

st.subheader("Dataset Overview")

overview_col1, overview_col2, overview_col3 = st.columns(3)

overview_col1.metric(
    "Observations",
    f"{len(master):,}"
)

overview_col2.metric(
    "Countries",
    f"{master['Country'].nunique():,}"
)

overview_col3.metric(
    "Years",
    f"{master['Year'].min()} – {master['Year'].max()}"
)


# -----------------------------
# Sidebar Filters
# -----------------------------

st.sidebar.title("🔎 Explore Data")

st.sidebar.caption(
    "Choose a country and year to explore inequality."
)


# Country filter
countries = sorted(
    master["Country"].dropna().unique()
)

selected_country = st.sidebar.selectbox(
    "Select a country",
    countries
)


# Country-specific data
country_data = master[
    master["Country"] == selected_country
].sort_values("Year")


# -----------------------------
# Year Filter
# -----------------------------
# Year is independent of country.
# This means every country gets the same year options.

available_years = sorted(
    master["Year"].dropna().unique()
)

selected_year = st.sidebar.selectbox(
    "Select a year",
    available_years,
    index=len(available_years) - 1
)


# Data for selected year
year_data = master[
    master["Year"] == selected_year
]


# Data for selected country + selected year
selected_row = master[
    (master["Country"] == selected_country) &
    (master["Year"] == selected_year)
]


# -----------------------------
# KPI Cards
# -----------------------------

if not selected_row.empty:

    row = selected_row.iloc[0]

    col1, col2, col3 = st.columns(3)

    gini_value = (
        f"{row['Gini']:.1f}"
        if pd.notna(row["Gini"])
        else "N/A"
    )

    gdp_value = (
        f"${row['GDP_per_capita']:,.0f}"
        if pd.notna(row["GDP_per_capita"])
        else "N/A"
    )

    population_value = (
        f"{row['Population']:,.0f}"
        if pd.notna(row["Population"])
        else "N/A"
    )

    col1.metric(
        "Gini Index",
        gini_value
    )

    col2.metric(
        "GDP per Capita",
        gdp_value
    )

    col3.metric(
        "Population",
        population_value
    )

else:

    st.warning(
        f"No data available for {selected_country} "
        f"in {selected_year}."
    )


# -----------------------------
# Country Trend
# -----------------------------

st.divider()

st.subheader(
    f"📈 {selected_country} — Inequality Over Time"
)


# Only keep years where Gini is available
trend_data = country_data.dropna(
    subset=["Gini"]
)


if not trend_data.empty:

    fig = px.line(
        trend_data,
        x="Year",
        y="Gini",
        markers=True,
        labels={
            "Year": "Year",
            "Gini": "Gini Index"
        },
        hover_data={
            "Year": True,
            "Gini": ":.1f"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # -----------------------------
    # Trend Insight
    # -----------------------------

    if len(trend_data) >= 2:

        first_gini = trend_data.iloc[0]["Gini"]
        latest_gini = trend_data.iloc[-1]["Gini"]

        first_year = int(
            trend_data.iloc[0]["Year"]
        )

        latest_year = int(
            trend_data.iloc[-1]["Year"]
        )

        change = latest_gini - first_gini

        if change > 0:

            st.write(
                f"📌 The Gini Index increased by "
                f"{change:.1f} points between "
                f"{first_year} and {latest_year}."
            )

        elif change < 0:

            st.write(
                f"📌 The Gini Index decreased by "
                f"{abs(change):.1f} points between "
                f"{first_year} and {latest_year}."
            )

        else:

            st.write(
                "📌 The Gini Index remained relatively "
                "unchanged between the first and latest "
                "available observations."
            )

else:

    st.warning(
        f"No Gini data is available for {selected_country}."
    )


# -----------------------------
# World Map
# -----------------------------

st.divider()

st.subheader(
    f"🌍 Global Income Inequality — {selected_year}"
)


# Only countries with Gini data
map_data = year_data.dropna(
    subset=["Gini", "Country_Code"]
)


if not map_data.empty:

    fig_map = px.choropleth(
        map_data,
        locations="Country_Code",
        color="Gini",
        hover_name="Country",
        hover_data={
            "Gini": ":.1f"
        },
        color_continuous_scale="RdBu_r",
        labels={
            "Gini": "Gini Index"
        }
    )

    fig_map.update_layout(
        margin=dict(
            l=0,
            r=0,
            t=20,
            b=0
        )
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True
    )

else:

    st.warning(
        f"No Gini data is available for {selected_year}."
    )


# -----------------------------
# Top 10 Countries
# -----------------------------

st.divider()

top10 = (
    year_data
    .dropna(subset=["Gini"])
    .sort_values(
        "Gini",
        ascending=False
    )
    .head(10)
    .sort_values("Gini")
)


st.subheader(
    f"📊 Highest Inequality — {selected_year}"
)

st.caption(
    "Countries with the highest reported Gini Index "
    "values for the selected year."
)


if not top10.empty:

    fig_bar = px.bar(
        top10,
        x="Gini",
        y="Country",
        orientation="h",
        text="Gini",
        labels={
            "Gini": "Gini Index",
            "Country": "Country"
        }
    )

    fig_bar.update_traces(
        texttemplate="%{text:.1f}",
        textposition="outside"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

else:

    st.warning(
        f"No Gini data is available for {selected_year}."
    )


# -----------------------------
# How to Use
# -----------------------------

st.divider()

with st.expander("ℹ️ How to use this dashboard"):

    st.write(
        """
        1. Select a country from the sidebar.

        2. Select a year from the year filter.

        3. Review the Gini Index, GDP per capita,
           and population for that country and year.

        4. Use the trend chart to examine inequality
           over time.

        5. Use the world map to compare inequality
           across countries.

        6. Use the ranking chart to identify countries
           with the highest reported Gini values.

        Note: Gini data is not available for every
        country in every year. When data is unavailable,
        the dashboard displays N/A or an appropriate
        message.
        """
    )

