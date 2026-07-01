import streamlit as st
from analyzer import extract_text, analyze_resume
from skills import job_roles
import matplotlib.pyplot as plt

# ---------------- NAVIGATION ----------------
col1, col2 = st.columns([1, 5])

with col1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

st.title("📄 Resume Analyzer")

st.write("Upload your resume and check skill match with job roles.")

# ---------------- INPUTS ----------------
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

role = st.selectbox(
    "Select Job Role",
    list(job_roles.keys())
)

# ---------------- PROCESS ----------------
if uploaded_file:

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
    st.subheader("📈 Skill Comparison")

    fig, ax = plt.subplots()
    ax.bar(
        ["Matched Skills", "Missing Skills"],
        [len(found), len(missing)]
    )
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # ---------------- SKILLS ----------------
    st.subheader("✅ Skills Found")
    if found:
        st.write(found)
    else:
        st.info("No skills matched")

    st.subheader("❌ Missing Skills")
    if missing:
        st.write(missing)
    else:
        st.success("No missing skills 🎉")

    # ---------------- REPORT ----------------
    report = f"""
RESUME ANALYSIS REPORT
----------------------

Role: {role}
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

    # ---------------- RESULT ----------------
    if score > 70:
        st.success("🎉 Good Resume Match")
    elif score > 40:
        st.warning("⚠ Moderate Resume - Improve Skills")
    else:
        st.error("❌ Weak Resume - Needs Improvement")

    # ---------------- NEXT PAGE BUTTON ----------------
    st.divider()

    if st.button("➡ Go to Suggestions Page"):
        st.switch_page("pages/suggestions.py")
