import streamlit as st
from analyzer import extract_text
from ai_engine import analyze_resume_ai

st.title("📄 AI Resume Analyzer")

# ---------------- SESSION INIT ----------------
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "analysis" not in st.session_state:
    st.session_state.analysis = ""

# ---------------- UPLOAD ----------------
uploaded_file = st.file_uploader("Upload Resume PDF")

job_role = st.selectbox("Select Job Role", [
    "Data Analyst",
    "Software Engineer",
    "AI/ML Engineer",
    "Web Developer",
    "Cyber Security",
    "Other"
])

if uploaded_file:
    st.session_state.resume_text = extract_text(uploaded_file)

    st.success("Resume Uploaded Successfully")

# ---------------- ANALYZE ----------------
if st.button("Generate AI Resume Score"):
    st.session_state.analysis = analyze_resume_ai(
        st.session_state.resume_text,
        job_role
    )

# ---------------- OUTPUT ----------------
if st.session_state.analysis:
    st.subheader("📊 AI Resume Report")
    st.write(st.session_state.analysis)

# ---------------- DOWNLOAD REPORT ----------------
if st.session_state.analysis:
    st.download_button(
        "⬇ Download Report",
        st.session_state.analysis,
        file_name="resume_report.txt"
    )

# ---------------- NEXT PAGE ----------------
if st.session_state.analysis:
    if st.button("Next ➡ Resume Tips"):
        st.switch_page("pages/4_Resume_Tips.py")
