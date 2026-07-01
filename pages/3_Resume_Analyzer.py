import streamlit as st
from analyzer import extract_text, analyze_resume
from skills import job_roles
import matplotlib.pyplot as plt
from nav import show_nav

show_nav()

st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

role = st.selectbox("Select Job Role", list(job_roles.keys()))

if uploaded_file:

    text = extract_text(uploaded_file)

    st.session_state["resume_text"] = text

    found, missing, score = analyze_resume(text, role)

    st.subheader("Resume Score")
    st.progress(score / 100)
    st.write(f"{score}/100")

    fig, ax = plt.subplots()
    ax.bar(["Matched", "Missing"], [len(found), len(missing)])
    st.pyplot(fig)

    st.subheader("Skills Found")
    st.write(found)

    st.subheader("Missing Skills")
    st.write(missing)

    report = f"""
Score: {score}
Found: {found}
Missing: {missing}
"""

    st.download_button("Download Report", report, "resume.txt")

    st.divider()

    if st.button("➡ Resume Tips"):
        st.switch_page("4_Resume_Tips.py")
