import streamlit as st

# ---------------- NAVIGATION ----------------
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

# ---------------- TITLE ----------------
st.title("🤖 AI Resume Tips")

# ---------------- CHECK RESUME ----------------
if "resume_text" not in st.session_state:
    st.warning("⚠ Please upload your resume in Resume Analyzer first")
    st.stop()

text = st.session_state["resume_text"].lower()

st.divider()

# ---------------- PERSONALIZED TIPS ----------------
st.subheader("📄 Personalized Tips")

if "project" not in text:
    st.warning("• Add at least 2–3 projects with description")

if "github" not in text:
    st.warning("• Add GitHub profile link")

if "internship" not in text:
    st.warning("• Add internship or real-world experience")

if "python" in text:
    st.success("• Strong Python skill detected 👍")

if "java" in text:
    st.success("• Java skill found 👍")

if "certificate" not in text and "certification" not in text:
    st.info("• Add certifications (NPTEL / Coursera / Udemy)")

if "achievement" not in text:
    st.info("• Add achievements section")

# ---------------- COMMON MISTAKES ----------------
st.divider()
st.subheader("❌ Common Mistakes")

st.error("• Too much text in resume")
st.error("• No project section")
st.error("• Missing GitHub link")
st.error("• Weak skills section")
st.error("• No achievements or certifications")

# ---------------- NEXT PAGE ----------------
st.divider()
st.subheader("🚀 Next Step")

st.write("Go to AI Career Advisor for job recommendations based on your resume.")

if st.button("➡ Go to AI Career Advisor"):
    st.switch_page("pages/5_AI_Career_Advisor.py")
