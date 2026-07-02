import streamlit as st
import matplotlib.pyplot as plt
from analyzer import extract_text
from skills import job_roles

st.title("📄 AI Resume Analyzer")

# ---------------- UPLOAD ----------------
uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

# ---------------- ROLE ----------------
role = st.selectbox("Select Job Role", list(job_roles.keys()))

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    st.subheader("📄 Extracted Resume")
    st.write(resume_text)

    if st.button("🚀 Analyze Resume"):

        # ---------------- SKILLS LOGIC ----------------
        required_skills = set(job_roles[role])

        words = set(resume_text.lower().split())

        matched = list(required_skills & words)
        missing = list(required_skills - words)

        # ---------------- SCORE ----------------
        score = int((len(matched) / len(required_skills)) * 100)

        st.subheader("📊 Resume Score")

        fig, ax = plt.subplots()
        ax.bar(["Score"], [score])
        ax.set_ylim(0, 100)
        st.pyplot(fig)

        # ---------------- SKILLS ----------------
        st.subheader("🟢 Skills Found")
        st.write(matched)

        st.subheader("🔴 Missing Skills")
        st.write(missing)

        # ---------------- REPORT ----------------
        report = f"""
RESUME ANALYSIS REPORT

Role: {role}
Score: {score}/100

Skills Found:
{matched}

Missing Skills:
{missing}
"""

        st.download_button(
            "📥 Download Report",
            report,
            file_name="resume_report.txt"
        )

        # ---------------- SESSION STORAGE ----------------
        st.session_state["role"] = role
        st.session_state["score"] = score
        st.session_state["matched"] = matched
        st.session_state["missing"] = missing

        # ---------------- NEXT PAGE ----------------
        if st.button("➡️ Next Page: Tips"):
            st.switch_page("pages/4_Resume_Tips.py")
