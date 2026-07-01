import streamlit as st
from nav import show_nav

st.set_page_config(page_title="AI Resume Analyzer")

show_nav()

st.title("🤖 AI Resume Analyzer")
st.write("Welcome to AI Resume Analyzer")

st.subheader("Choose a Page")

if st.button("📝 Register"):
    st.switch_page("1_Register")

if st.button("🔐 Login"):
    st.switch_page("2_Login")

if st.button("📄 Resume Analyzer"):
    st.switch_page("3_Resume_Analyzer")

if st.button("🤖 Resume Tips"):
    st.switch_page("4_Resume_Tips")

if st.button("🎯 Career Advisor"):
    st.switch_page("5_AI_Career_Advisor")

if st.button("💼 Job Roles"):
    st.switch_page("6_Job_Roles")

if st.button("ℹ About"):
    st.switch_page("7_About_Project")
