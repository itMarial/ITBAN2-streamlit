import streamlit as st
st.set_page_config(page_title="Data Warehousing & EDM", layout="wide")
st.sidebar.title("Settings")
topic = st.sidebar.selectbox("Choose a topic", ["Data Warehousing", "Enterprise Data Management"])


st.title("Data Warehousing & Enterprise Data Management")
col1, col2 = st.columns(2)
with col1:
    if topic == "Data Warehousing":
        st.subheader("Data Warehousing Concepts")
        st.markdown("""
        - Central repository for integrated data
        - Used for business intelligence and reporting
        - Supports historical data analysis
        """)
    else:
        st.subheader("Enterprise Data Management Overview")
        st.markdown("""
        - Managing data as a strategic asset
        - Encompasses data governance, quality, and integration
        - Ensures data is accurate and accessible across systems
        """)

with col2:
    st.write("")
tab1, tab2 = st.tabs(["Key Features", "Use Cases"])
with tab1:
    st.write("### Key Features")
    st.markdown("""
    - **Data Warehousing**:
      -  ETL (Extract, Transform, Load) pipelines and OLAP cubes
      - Scalability and storage optimization
      
    - **Enterprise Data Management**:
      - Data quality monitoring
      - Data stewardship roles
      - Master data management
    """)
with tab2:
    st.write("### Use Cases")
    st.markdown("""
    - **Retail Analytics**
    - **Customer Relationship Management (CRM)**
    - **Finance and Budgeting**
    - **Health Data Compliance**
    """)

# Expander section
with st.expander("More About OLAP vs OLTP"):
    st.write("""
    - **OLTP**: Optimized for transactional processing (insert/update/delete)
    - **OLAP**: Optimized for querying and reporting, especially on historical data
    """)
