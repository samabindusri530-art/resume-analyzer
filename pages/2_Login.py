import streamlit as st
from nav import show_nav

show_nav()

st.title("🔐 Login Page")

if "users" not in st.session_state:
    st.session_state["users"] = {}

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    users = st.session_state["users"]

    if username in users and users[username] == password:
        st.success("Login Successful 🎉")
        st.session_state["logged_in"] = True
        st.session_state["user"] = username
    else:
        st.error("Invalid Credentials")

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Register"):
        st.switch_page("1_Register")

with col2:
    if st.button("➡ Resume Analyzer"):
        st.switch_page("pages/3_Resume_Analyzer.py")
