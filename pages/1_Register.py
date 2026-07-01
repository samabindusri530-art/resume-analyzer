import streamlit as st
import csv

st.title("Register")

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):

    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, password])

    st.success("Registered Successfully")
