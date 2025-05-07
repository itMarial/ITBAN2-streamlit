import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database credentials
DATABASE_URL = 'mysql+mysqlconnector://root:@localhost/streamlit'  # Adjust with your MySQL credentials

# Create an engine that will connect to the MySQL database
engine = create_engine(DATABASE_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Fetch and display data from the "users" table using SQLAlchemy
query = "SELECT * FROM users"
df = pd.read_sql(query, engine)
st.dataframe(df)

# Insert new rows with a form
with st.form(key='insert_form'):
    name = st.text_input("Enter name:")
    password = st.text_input("Enter password:", type="password")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        # Insert new row into the "users" table using SQLAlchemy
        query = f"INSERT INTO users (name, password) VALUES (%s, %s)"
        engine.execute(query, (name, password))
        st.success("Data inserted successfully!")

# User authentication form
with st.form(key='login_form'):
    username = st.text_input("Username:")
    user_password = st.text_input("Password:", type="password")
    login_button = st.form_submit_button("Login")

    if login_button:
        # Use parameterized query to prevent SQL injection
        query = "SELECT * FROM users WHERE name = %s AND password = %s"
        result = pd.read_sql(query, engine, params=(username, user_password))

        if not result.empty:
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid username or password")