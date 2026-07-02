import streamlit as st
from nav import show_nav

# ---------------- NAVIGATION ----------------
show_nav()

# ---------------- TITLE ----------------
st.title("🤖 AI Career Advisor")

# ---------------- CHECK RESUME ----------------
if "resume_text" not in st.session_state:
    st.warning("⚠ Please upload your resume in Resume Analyzer first")
    st.stop()

text = st.session_state["resume_text"].lower()

st.divider()

# ---------------- SKILL EXTRACTION ----------------
st.subheader("📄 Detected Skills from Resume")

skills_detected = []

if "python" in text:
    skills_detected.append("Python")
if "sql" in text:
    skills_detected.append("SQL")
if "html" in text or "css" in text:
    skills_detected.append("HTML/CSS")
if "java" in text:
    skills_detected.append("Java")
if "machine learning" in text:
    skills_detected.append("Machine Learning")
if "data" in text:
    skills_detected.append("Data Handling")

st.write(skills_detected)

st.divider()

# ---------------- CAREER LOGIC ----------------
st.subheader("🎯 Best Career Recommendation")

skills = [s.lower() for s in skills_detected]

if "python" in skills and "sql" in skills:
    st.success("🎯 Best Career: Data Analyst / Data Scientist")

    st.write("🏢 Companies: Google, Microsoft, Amazon, IBM")
    st.info("📚 Learn: Pandas, NumPy, Power BI, Excel, Statistics")

elif "machine learning" in skills or ("python" in skills and "data handling" in skills):
    st.success("🎯 Best Career: AI / Machine Learning Engineer")

    st.write("🏢 Companies: OpenAI, Google DeepMind, NVIDIA")
    st.info("📚 Learn: TensorFlow, PyTorch, Deep Learning, NLP")

elif "html/css" in skills:
    st.success("🎯 Best Career: Frontend Developer")

    st.write("🏢 Companies: Flipkart, Infosys, TCS, Startups")
    st.info("📚 Learn: JavaScript, React, UI/UX, Responsive Design")

elif "java" in skills:
    st.success("🎯 Best Career: Software Engineer")

    st.write("🏢 Companies: Google, Microsoft, Adobe, Infosys")
    st.info("📚 Learn: DSA, System Design, Spring Boot")

elif "sql" in skills:
    st.success("🎯 Best Career: Database / Backend Analyst")

    st.write("🏢 Companies: Oracle, IBM, Accenture")
    st.info("📚 Learn: SQL Advanced, DBMS, Backend APIs")

else:
    st.warning("⚠ Not enough skills detected for strong career prediction")
    st.info("Try adding: Python, SQL, Java, Machine Learning, Projects")

# ---------------- NEXT PAGE FLOW ----------------
st.divider()

st.subheader("🚀 Next Step")

st.write("Go to Job Roles page to explore detailed job descriptions.")

if st.button("➡ Go to Job Roles"):
    st.switch_page("pages/6_Job_Roles.py")
