import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("COVID-19 Statistics Dashboard")
# Sidebar  country selection
st.sidebar.header("Choose a country")
country = st.sidebar.selectbox("Country", ["Philippines", "USA", "India", "Brazil", "Russia", "Japan"])
# Fetch ang API
url = f"https://disease.sh/v3/covid-19/historical/{country}?lastdays=300"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    timeline = data["timeline"]
    df_cases = pd.DataFrame(timeline["cases"].items(), columns=["Date", "Cases"])
    df_deaths = pd.DataFrame(timeline["deaths"].items(), columns=["Date", "Deaths"])
    df_recovered = pd.DataFrame(timeline["recovered"].items(), columns=["Date", "Recovered"])

    df = df_cases.merge(df_deaths, on="Date").merge(df_recovered, on="Date")
    df["Date"] = pd.to_datetime(df["Date"])

    st.subheader(f"COVID-19 Trends in {country} (Last 300 Days)(2022)")
    # Line Chart
    st.plotly_chart(px.line(df, x="Date", y=["Cases", "Deaths", "Recovered"], title="Line Chart: COVID Trends"))

    # Bar Chart (Latest Data)
    latest = df.iloc[-1]
    bar_data = pd.DataFrame({
        "Category": ["Cases", "Deaths", "Recovered"],
        "Count": [latest["Cases"], latest["Deaths"], latest["Recovered"]]
    })
    st.plotly_chart(px.bar(bar_data, x="Category", y="Count", title="Bar Chart: Latest Totals"))

    # Pie Chart
    st.plotly_chart(px.pie(bar_data, names="Category", values="Count", title="Pie Chart: Proportions"))

    # Area Chart
    st.plotly_chart(px.area(df, x="Date", y="Cases", title="Area Chart: Case Growth"))

    # Data Table
    st.subheader(" Raw Data Table")
    st.dataframe(df.tail(10))

else:
    st.error("Failed to fetch data from the API.")
