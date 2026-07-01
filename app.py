import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")

st.write("Welcome to AI Resume Analyzer")

st.subheader("Choose a Page")

if st.button("Register"):
    st.switch_page("pages/1_Register.py")

if st.button("Login"):
    st.switch_page("pages/2_Login.py")

if st.button("Resume Analyzer"):
    st.switch_page("pages/3_Resume_Analyzer.py")
    
if st.button("AI Career Advisor"):
    st.switch_page("pages/4_AI_Career_Advisor.py")

if st.button("Resume Tips"):
    st.switch_page("pages/5_Resume_Tips.py")

if st.button("Job Roles"):
    st.switch_page("pages/6_Job_Roles.py")

if st.button("About Project"):
    st.switch_page("pages/7_About_Project.py")

if st.button("Company Resume Check"):
    st.switch_page("pages/8_Company_Check.py")
