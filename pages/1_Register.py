import streamlit as st
from nav import show_nav

show_nav()

st.title("📝 Register Page")

if "users" not in st.session_state:
    st.session_state["users"] = {}

username = st.text_input("Create Username")
password = st.text_input("Create Password", type="password")

if st.button("Register"):

    if username == "" or password == "":
        st.warning("Please fill all fields")

    elif username in st.session_state["users"]:
        st.error("User already exists")

    else:
        st.session_state["users"][username] = password
        st.success("Registration successful 🎉")

st.divider()

if st.button("➡ Go to Login"):
    st.switch_page("pages/2_Login.py")
