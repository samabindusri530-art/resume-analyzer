import streamlit as st
import matplotlib.pyplot as plt
from analyzer import extract_text
from ai_engine import analyze_resume_ai
from skills import job_roles

st.title("📄 Resume Analyzer")

# ---------------- 1. UPLOAD PDF ----------------
uploaded_file = st.file_uploader("📤 Upload Resume PDF", type=["pdf"])

# ---------------- 2. SELECT ROLE ----------------
role = st.selectbox(
    "🎯 Select Job Role",
    list(job_roles.keys())
)

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    st.success("PDF Uploaded Successfully!")

    # ---------------- 3. ANALYZE BUTTON ----------------
    if st.button("🚀 Analyze Resume"):

        # AI OUTPUT
        result = analyze_resume_ai(resume_text, role)

        st.subheader("🤖 AI Analysis")
        st.write(result)

        # ---------------- 4. SKILLS LOGIC ----------------
        required_skills = set(job_roles[role])
        words = set(resume_text.lower().split())

        matched = list(required_skills & words)
        missing = list(required_skills - words)

        # ---------------- 5. RESUME SCORE ----------------
        score = int((len(matched) / len(required_skills)) * 100)

        st.subheader("📊 Resume Score")

        fig, ax = plt.subplots()
        ax.bar(["Score"], [score])
        ax.set_ylim(0, 100)
        st.pyplot(fig)

        # ---------------- 6. SKILLS FOUND ----------------
        st.subheader("🟢 Skills Found")
        st.write(matched)

        # ---------------- 7. MISSING SKILLS ----------------
        st.subheader("🔴 Missing Skills")
        st.write(missing)

        # ---------------- 8. DOWNLOAD REPORT ----------------
        report = f"""
RESUME ANALYSIS REPORT

Role: {role}

Score: {score}/100

Skills Found:
{matched}

Missing Skills:
{missing}

AI Feedback:
{result}
"""

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="resume_report.txt",
            mime="text/plain"
        )

        # ---------------- 9. STORE FOR NEXT PAGES ----------------
        st.session_state["result"] = result
        st.session_state["score"] = score
        st.session_state["matched"] = matched
        st.session_state["missing"] = missing
        st.session_state["role"] = role

        # ---------------- 10. NEXT PAGE FLOW ----------------
        if st.button("➡️ Next Page: Resume Tips"):
            st.switch_page("pages/4_Resume_Tips")
