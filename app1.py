import streamlit as st


st.title("Hello, Streamlit  (st.title)")
st.header("Welcome to your first Streamlit app(st.header)")
st.write("Write your name and age (st.write)")


name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=100, step=1)



if name:
    st.write(f"Hello, **{name}**! You are **{age}** years old.")



