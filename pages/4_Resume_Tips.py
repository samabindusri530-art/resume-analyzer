import streamlit as st
from nav import show_nav

show_nav()

st.title("🤖 AI Resume Tips (Based on Your Resume)")

if "resume_text" not in st.session_state:
    st.warning("⚠ Upload resume first in Resume Analyzer")
    st.stop()

text = st.session_state["resume_text"].lower()

st.subheader("📄 Personalized Tips")

if "project" not in text:
    st.warning("• Add more projects")

if "github" not in text:
    st.warning("• Add GitHub profile")

if "internship" not in text:
    st.warning("• Add internship experience")

if "python" in text:
    st.success("• Good Python skill detected 👍")

st.divider()

st.subheader("❌ Common Mistakes")
st.write("""
- Too much text  
- No projects  
- No GitHub  
- No achievements  
- Weak skills section  
""")
