import streamlit as st

PAGES = {
    "🏠 Home": "app",
    "📝 Register": "pages/1_Register",
    "🔐 Login": "pages/2_Login",
    "📄 Resume Analyzer": "pages/3_Resume_Analyzer",
    "🤖 AI Tips": "pages/4_Resume_Tips",
    "🎯 Career Advisor": "pages/5_AI_Career_Advisor",
    "💼 Job Roles": "pages/6_Job_Roles",
    "ℹ About": "pages/7_About_Project"
}

def show_nav():
    st.sidebar.title("📌 Navigation")

    choice = st.sidebar.radio(
        "Go to",
        list(PAGES.keys())
    )

    st.switch_page(PAGES[choice])
