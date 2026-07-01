import streamlit as st
from nav import show_nav

# ---------------- NAVIGATION ----------------
show_nav()

# ---------------- TITLE ----------------
st.title("🤖 AI Career Planner")

st.write("Ask anything like: *How to prepare for Data Analyst in 1 month?*")

# ---------------- CHECK RESUME ----------------
if "resume_text" not in st.session_state:
    st.warning("⚠ Please upload your resume first in Resume Analyzer")
    st.stop()

resume = st.session_state["resume_text"].lower()

st.divider()

# ---------------- USER INPUT ----------------
query = st.text_input("💬 Ask your AI Career Planner")

# ---------------- RESPONSE ----------------
if query:

    st.info("🧠 AI is analyzing your resume and generating plan...")

    st.divider()

    st.subheader("🎯 Personalized AI Plan")

    st.write(f"""
Based on your resume and your query:

**"{query}"**

---

## 📌 Step 1: Skill Analysis
Your resume indicates exposure to:
- {", ".join(set(resume.split()[:15]))} ...

---

## 📌 Step 2: What You Should Focus On
- Strengthen core technical skills
- Build real-world projects (very important)
- Improve problem-solving ability
- Learn industry tools based on target role

---

## 📌 Step 3: Learning Strategy
- Learn by doing (projects > theory)
- Practice daily coding / tools
- Follow structured learning + practice mix
- Focus on one career path first

---

## 📌 Step 4: Project Strategy
- Build 2–3 strong projects
- Upload on GitHub
- Add them to resume
- Make them interview-ready

---

## 📌 Step 5: Job Preparation
- Practice interview questions
- Improve communication skills
- Apply for internships early
- Build LinkedIn profile

---

## 🚀 Final Advice
Consistency for 30–60 days = job ready candidate
""")

# ---------------- EXTRA HELP ----------------
st.divider()

st.subheader("💡 Quick Suggestions")

st.write("""
• Keep learning daily (1–2 hours is enough)  
• Focus on projects instead of only courses  
• Improve resume every 2 weeks  
• Apply while learning  
""")
