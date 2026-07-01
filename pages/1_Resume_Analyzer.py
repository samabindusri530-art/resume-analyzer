import streamlit as st
from analyzer import extract_text, analyze_resume
from skills import job_roles


st.title("Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

role = st.selectbox(
    "Select Job Role",
    list(job_roles.keys())
)

if uploaded_file:

    text = extract_text(uploaded_file)

    found, missing, score = analyze_resume(text, role)

    st.subheader("Resume Score")
    st.write(str(score) + " /100")

    st.subheader("Skills Found")
    st.write(found)

    st.subheader("Missing Skills")
    st.write(missing)

    if score > 70:
        st.success("Good Resume Match")

    else:
        st.warning("Need Improvement")
