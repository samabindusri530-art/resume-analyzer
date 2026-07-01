import streamlit as st

def show_nav():

    st.sidebar.title("📌 Navigation")

    page = st.sidebar.radio(
        "Go to",
        [
            "Home",
            "Register",
            "Login",
            "Resume Analyzer",
            "Resume Tips",
            "AI Career Advisor",
            "Job Roles",
            "About Project"
        ]
    )

    st.session_state["nav_page"] = page
