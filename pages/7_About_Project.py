import streamlit as st
from nav import show_nav

show_nav()

st.title("ℹ About Project")

st.write("AI Resume Analyzer helps analyze resumes and suggest careers.")
st.write("Built using Streamlit + Python + ML logic")

if st.button("🏠 Home"):
    st.switch_page("app")
