import streamlit as st

st.title("User Registration")

name = st.text_input("Enter Name")
email = st.text_input("Enter Email")
password = st.text_input("Enter Password", type="password")

if st.button("Register"):
    st.success("Registration Successful")
