import streamlit as st
import csv

if st.button("Back to Home"):
    st.switch_page("app.py")

st.title("Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    with open("users.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:

            if row[1] == email and row[2] == password:
                st.success("Login Successful")
                break
