import streamlit as st
from analyzer import extract_text, analyze_resume
from skills import job_roles
import pandas as pd
import matplotlib.pyplot as plt

if st.button("Back to Home"):
    st.switch_page("app.py")

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

    # graph
    fig, ax = plt.subplots()

    ax.bar(
        ["Matched Skills", "Missing Skills"],
        [len(found), len(missing)]
    )

    st.pyplot(fig)

    st.subheader("Skills Found")
    st.write(found)

    st.subheader("Missing Skills")
    st.write(missing)

    # download report
    report = f"""
Resume Score: {score}

Skills Found:
{found}

Missing Skills:
{missing}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="resume_report.txt",
        mime="text/plain"
    )

    if score > 70:
        st.success("Good Resume Match")

    else:
        st.warning("Need Improvement")
