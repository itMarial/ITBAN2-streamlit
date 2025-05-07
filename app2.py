import streamlit as st
import pandas as pd

st.title("  DataFrame Viewer")
st.write("Upload a CSV file and interact with its contents.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)


    if st.checkbox("Show raw data"):
        st.dataframe(df)

    
    column_to_filter = st.selectbox("Select column to filter", df.columns)

    if df[column_to_filter].dtype == 'object' or df[column_to_filter].nunique() < 50:
        selected_value = st.selectbox(f"Filter {column_to_filter} by value", df[column_to_filter].unique())
        filtered_df = df[df[column_to_filter] == selected_value]
        st.write(f"Filtered data for {column_to_filter} = {selected_value}")
        st.dataframe(filtered_df)
    else:
        st.write("Selected column is not filterable")
else:
    st.info("upload a CSV file")
