import streamlit as st
from nav import show_nav

show_nav()

st.title("💼 Job Role Recommendation (Resume Based)")

if "resume_text" not in st.session_state:
    st.warning("⚠ Upload resume first in Resume Analyzer")
    st.stop()

text = st.session_state["resume_text"].lower()

st.subheader("📄 Analyzing Resume Skills...")

if "python" in text and "sql" in text:
    st.success("🎯 Recommended Role: Data Analyst")

elif "html" in text and "css" in text:
    st.success("🎯 Recommended Role: Frontend Developer")

elif "machine learning" in text:
    st.success("🎯 Recommended Role: Data Scientist")

elif "java" in text:
    st.success("🎯 Recommended Role: Software Engineer")

else:
    st.warning("⚠ Need more technical skills in resume")
