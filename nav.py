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
            "AI Tips",
            "Career Advisor",
            "Job Roles",
            "About"
        ]
    )

    # SIMPLE DIRECT NAVIGATION (NO BUTTON NEEDED)

    if page == "Home":
        st.switch_page("app")

    elif page == "Register":
        st.switch_page("Register")

    elif page == "Login":
        st.switch_page("Login")

    elif page == "Resume Analyzer":
        st.switch_page("Resume_Analyzer")

    elif page == "AI Tips":
        st.switch_page("Resume_Tips")

    elif page == "Career Advisor":
        st.switch_page("Career_Advisor")

    elif page == "Job Roles":
        st.switch_page("Job_Roles")

    elif page == "About":
        st.switch_page("About_Project")
