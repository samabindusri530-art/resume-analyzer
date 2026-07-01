iimport streamlit as st
from nav import show_nav

show_nav()

st.title("📝 Register Page")

# ---------------- SESSION ----------------
if "users" not in st.session_state:
    st.session_state["users"] = {}

# ---------------- INPUTS ----------------
username = st.text_input("Create Username")
password = st.text_input("Create Password", type="password")

# ---------------- REGISTER ----------------
if st.button("Register"):

    if username == "" or password == "":
        st.warning("Please fill all fields")

    elif username in st.session_state["users"]:
        st.error("User already exists")

    else:
        st.session_state["users"][username] = password
        st.success("Registration successful 🎉")
        st.info("Now go to Login page from sidebar navigation")

st.divider()

# ---------------- NAVIGATION (FIXED) ----------------
if st.button("➡ Go to Login"):
    st.switch_page("Login")
