import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")

st.write("Welcome to AI Resume Analyzer")

st.subheader("Choose a Page")

if st.button("Resume Analyzer"):
    st.switch_page("pages/1_Resume_Analyzer.py")

if st.button("Resume Tips"):
    st.switch_page("pages/2_Resume_Tips.py")

if st.button("Job Roles"):
    st.switch_page("pages/3_Job_Roles.py")

if st.button("About Project"):
    st.switch_page("pages/4_About_Project.py")
