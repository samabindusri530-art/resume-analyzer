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

        st.info("Go to Resume Analyzer")

    else:
        st.error("Invalid Credentials")

st.divider()

# FLOW BUTTONS (IMPORTANT FOR YOUR PROJECT)

col1, col2 = st.columns(2)

with col1:
    if st.button("⬅ Go to Register"):
        st.switch_page("1_Register")

with col2:
    if st.button("➡ Continue"):
        st.switch_page("3_Resume_Analyzer")
