import streamlit as st
from nav import show_nav

# ---------------- NAVIGATION ----------------
show_nav()

# ---------------- TITLE ----------------
st.title("📅 AI Career Planner")

# ---------------- CHECK RESUME ----------------
if "resume_text" not in st.session_state:
    st.warning("⚠ Please upload your resume first in Resume Analyzer")
    st.stop()

text = st.session_state["resume_text"].lower()

st.divider()

st.subheader("🎯 Personalized Learning Plan")

# ---------------- SKILL BASED LOGIC ----------------
skills = []

if "python" in text:
    skills.append("Python")
if "sql" in text:
    skills.append("SQL")
if "java" in text:
    skills.append("Java")
if "html" in text or "css" in text:
    skills.append("Web Development")
if "machine learning" in text:
    skills.append("Machine Learning")

st.write("📄 Detected Skills:", skills)

st.divider()

# ---------------- PLAN GENERATION ----------------

st.subheader("📌 What You Should Do Next")

if "Python" in skills and "SQL" in skills:

    st.success("📊 Data Analyst / Data Scientist Track Plan")

    st.write("1️⃣ Strengthen Python (Pandas, NumPy)")
    st.write("2️⃣ Practice SQL queries daily")
    st.write("3️⃣ Learn Data Visualization (Power BI / Tableau)")
    st.write("4️⃣ Build 2 projects (Sales analysis, dashboard)")
    st.write("5️⃣ Upload projects on GitHub")

elif "Machine Learning" in skills:

    st.success("🤖 AI / ML Engineer Track Plan")

    st.write("1️⃣ Improve Python for ML")
    st.write("2️⃣ Learn ML algorithms (Regression, Classification)")
    st.write("3️⃣ Practice datasets (Kaggle)")
    st.write("4️⃣ Build ML project (Prediction system)")
    st.write("5️⃣ Learn TensorFlow / PyTorch basics")

elif "Web Development" in skills:

    st.success("🌐 Frontend Developer Track Plan")

    st.write("1️⃣ Master HTML + CSS")
    st.write("2️⃣ Learn JavaScript deeply")
    st.write("3️⃣ Learn React framework")
    st.write("4️⃣ Build portfolio website")
    st.write("5️⃣ Deploy projects on GitHub / Netlify")

elif "Java" in skills:

    st.success("☕ Software Developer Track Plan")

    st.write("1️⃣ Strengthen Java basics")
    st.write("2️⃣ Practice DSA daily")
    st.write("3️⃣ Learn problem solving (LeetCode)")
    st.write("4️⃣ Build backend project")
    st.write("5️⃣ Learn Spring Boot basics")

else:

    st.warning("⚠ Beginner Level Plan")

    st.write("1️⃣ Learn Python basics")
    st.write("2️⃣ Learn HTML + CSS")
    st.write("3️⃣ Learn SQL basics")
    st.write("4️⃣ Build 1 simple project")
    st.write("5️⃣ Practice daily coding")

# ---------------- FINAL ADVICE ----------------
st.divider()

st.subheader("🚀 Important Advice")

st.info("""
✔ Focus on projects more than theory  
✔ Practice daily for consistency  
✔ Build GitHub portfolio  
✔ Apply for internships while learning  
""")
