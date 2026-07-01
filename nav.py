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
            "Career Advisor",
            "Job Roles",
            "About"
        ]
    )

    if page == "Home":
        st.rerun()   # ✅ FIX HERE

    elif page == "Register":
        st.switch_page("1_Register")

    elif page == "Login":
        st.switch_page("2_Login")

    elif page == "Resume Analyzer":
        st.switch_page("3_Resume_Analyzer")

    elif page == "Resume Tips":
        st.switch_page("4_Resume_Tips")

    elif page == "Career Advisor":
        st.switch_page("5_AI_Career_Advisor")

    elif page == "Job Roles":
        st.switch_page("6_Job_Roles")

    elif page == "About":
        st.switch_page("7_About_Project")
