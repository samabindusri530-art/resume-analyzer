import streamlit as st
from nav import show_nav

show_nav()

st.title("🤖 AI Career Advisor (Resume Based)")

if "resume_text" not in st.session_state:
    st.warning("⚠ Please upload resume first in Resume Analyzer")
    st.stop()

text = st.session_state["resume_text"].lower()

st.subheader("📄 Detected Skills from Resume")

skills_detected = []

if "python" in text:
    skills_detected.append("Python")
if "sql" in text:
    skills_detected.append("SQL")
if "html" in text:
    skills_detected.append("HTML/CSS")
if "java" in text:
    skills_detected.append("Java")
if "machine learning" in text:
    skills_detected.append("Machine Learning")

st.write(skills_detected)

st.divider()

# ---------------- CAREER LOGIC ----------------
if "python" in text and "sql" in text:
    st.success("🎯 Best Career: Data Analyst / Data Scientist")

    st.write("• Google, Microsoft, Amazon")
    st.write("• Learn Pandas, NumPy, Power BI")

elif "html" in text and "css" in text:
    st.success("🎯 Best Career: Frontend Developer")

    st.write("• Flipkart, Infosys, TCS")
    st.write("• Learn React, JS, UI/UX")

elif "java" in text:
    st.success("🎯 Best Career: Software Engineer")

    st.write("• Google, Microsoft, Adobe")
    st.write("• DSA, System Design")

elif "machine learning" in text:
    st.success("🎯 Best Career: AI/ML Engineer")

    st.write("• OpenAI, NVIDIA, Google DeepMind")
    st.write("• TensorFlow, PyTorch")

else:
    st.warning("⚠ Add more technical skills to get better career suggestions")
