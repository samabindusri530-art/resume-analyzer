import streamlit as st

# Back button
if st.button("Back to Home"):
    st.switch_page("app.py")
st.title("About Project")

st.write(
    "AI Resume Analyzer is a project "
    "that analyzes resume PDF files."
)

st.write(
    "It compares user skills with "
    "job role requirements."
)

st.write(
    "Built using Python, Streamlit and PyPDF2"
)
