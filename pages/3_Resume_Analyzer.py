import streamlit as st
from analyzer import extract_text, analyze_resume
from skills import job_roles
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Resume Analyzer", layout="centered")

# ---------------- NAVIGATION (INSIDE SAME FILE) ----------------
st.sidebar.title("📌 Navigation")

if st.sidebar.button("🏠 Home"):
    st.switch_page("app.py")

if st.sidebar.button("📝 Register"):
    st.switch_page("pages/1_Register.py")

if st.sidebar.button("🔐 Login"):
    st.switch_page("pages/2_Login.py")

if st.sidebar.button("📄 Resume Analyzer"):
    st.switch_page("pages/3_Resume_Analyzer.py")

if st.sidebar.button("🤖 Resume Tips"):
    st.switch_page("pages/4_Resume_Tips.py")

if st.sidebar.button("🎯 Career Advisor"):
    st.switch_page("pages/5_AI_Career_Advisor.py")

if st.sidebar.button("💼 Job Roles"):
    st.switch_page("pages/6_Job_Roles.py")

if st.sidebar.button("ℹ About"):
    st.switch_page("pages/7_About_Project.py")

# ---------------- TITLE ----------------
st.title("📄 Resume Analyzer")
st.write("Upload your resume and check skill match with job roles.")

# ---------------- INPUTS ----------------
uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

role = st.selectbox(
    "Select Job Role",
    list(job_roles.keys())
)

# ---------------- MAIN LOGIC ----------------
if uploaded_file is not None:

    text = extract_text(uploaded_file)

    st.session_state["resume_text"] = text

    found, missing, score = analyze_resume(text, role)

    st.session_state["resume_score"] = score
    st.session_state["found_skills"] = found
    st.session_state["missing_skills"] = missing

    # ---------------- SCORE ----------------
    st.subheader("📊 Resume Score")
    st.progress(score / 100)
    st.write(f"**{score} / 100**")

    # ---------------- GRAPH ----------------
    st.subheader("📈 Skill Analysis")

    fig, ax = plt.subplots()
    ax.bar(
        ["Matched Skills", "Missing Skills"],
        [len(found), len(missing)]
    )

    ax.set_ylabel("Count")
    st.pyplot(fig)

    # ---------------- SKILLS ----------------
    st.subheader("✅ Skills Found")
    st.write(found if found else "No skills matched")

    st.subheader("❌ Missing Skills")
    st.write(missing if missing else "No missing skills")

    # ---------------- REPORT ----------------
    report = f"""
RESUME ANALYSIS REPORT
----------------------

Score: {score} / 100

Skills Found:
{', '.join(found) if found else 'None'}

Missing Skills:
{', '.join(missing) if missing else 'None'}
"""

    st.download_button(
        label="⬇ Download Report",
        data=report,
        file_name="resume_report.txt",
        mime="text/plain"
    )

    # ---------------- RESULT MESSAGE ----------------
    if score > 70:
        st.success("🎉 Good Resume Match")
    elif score > 40:
        st.warning("⚠ Moderate Resume - Improve Skills")
    else:
        st.error("❌ Weak Resume - Needs Improvement")

    # ---------------- NEXT PAGE BUTTON ----------------
    st.divider()

    if st.button("➡ Go to Next Page (Suggestions)"):
        st.switch_page("pages/4_Resume_Tips.py")
