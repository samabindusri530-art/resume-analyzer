import streamlit as st
from nav import show_nav

# ---------------- NAVIGATION ----------------
show_nav()

# ---------------- TITLE ----------------
st.title("💼 Job Role Recommendations")

# ---------------- CHECK RESUME ----------------
if "resume_text" not in st.session_state:
    st.warning("⚠ Please upload your resume first in Resume Analyzer")
    st.stop()

text = st.session_state["resume_text"].lower()

st.divider()

st.subheader("🎯 Recommended Career Paths")

# ---------------- DATA ANALYST PATH ----------------
if "python" in text and "sql" in text:

    st.success("📊 Data Analyst / Data Scientist Path")

    st.write("🏢 Top Companies:")
    st.write("• Google • Microsoft • Amazon • IBM • Deloitte")

    st.write("💼 Job Roles:")
    st.write("• Data Analyst (Entry Level)")
    st.write("• Business Analyst")
    st.write("• Junior Data Scientist")
    st.write("• BI Developer")

    st.write("🚀 Internship Roles:")
    st.write("• Data Analytics Intern")
    st.write("• Business Intelligence Intern")

    st.info("📚 Skills to Learn:")
    st.write("Pandas, NumPy, Power BI, Excel, SQL Advanced, Statistics")

    st.write("📈 Career Growth:")
    st.write("Data Analyst → Data Scientist → Data Engineer")

# ---------------- AI / ML PATH ----------------
elif "machine learning" in text:

    st.success("🤖 AI / ML Engineer Path")

    st.write("🏢 Top Companies:")
    st.write("• OpenAI • Google DeepMind • NVIDIA • Meta")

    st.write("💼 Job Roles:")
    st.write("• Machine Learning Engineer")
    st.write("• AI Research Assistant")
    st.write("• Data Scientist")

    st.write("🚀 Internship Roles:")
    st.write("• AI Intern")
    st.write("• ML Intern")

    st.info("📚 Skills to Learn:")
    st.write("TensorFlow, PyTorch, Deep Learning, NLP, Python Advanced")

    st.write("📈 Career Growth:")
    st.write("ML Engineer → AI Scientist → Research Scientist")

# ---------------- WEB DEV PATH ----------------
elif "html" in text or "css" in text:

    st.success("🌐 Frontend Developer Path")

    st.write("🏢 Top Companies:")
    st.write("• Infosys • TCS • Flipkart • Amazon • Startups")

    st.write("💼 Job Roles:")
    st.write("• Frontend Developer")
    st.write("• UI Developer")
    st.write("• Web Designer")

    st.write("🚀 Internship Roles:")
    st.write("• Web Development Intern")
    st.write("• UI/UX Intern")

    st.info("📚 Skills to Learn:")
    st.write("JavaScript, React, Tailwind CSS, UI/UX Design")

    st.write("📈 Career Growth:")
    st.write("Frontend Developer → Full Stack Developer → Tech Lead")

# ---------------- JAVA PATH ----------------
elif "java" in text:

    st.success("☕ Software Developer Path")

    st.write("🏢 Top Companies:")
    st.write("• Google • Microsoft • Adobe • Infosys • Wipro")

    st.write("💼 Job Roles:")
    st.write("• Software Engineer")
    st.write("• Backend Developer")
    st.write("• Java Developer")

    st.write("🚀 Internship Roles:")
    st.write("• Software Development Intern")
    st.write("• Backend Intern")

    st.info("📚 Skills to Learn:")
    st.write("DSA, System Design, Spring Boot, SQL")

    st.write("📈 Career Growth:")
    st.write("Developer → Senior Engineer → Software Architect")

# ---------------- DEFAULT PATH ----------------
else:

    st.warning("⚠ Limited skills detected")

    st.write("💡 Suggested Career Paths:")
    st.write("• Python Developer")
    st.write("• Web Developer")
    st.write("• Data Analyst (Beginner Level)")

    st.write("🚀 Opportunities:")
    st.write("• Internship in IT companies")
    st.write("• Freelancing projects")
    st.write("• Open Source contribution")

    st.info("📚 Learn: Python, SQL, HTML, Git, Projects")

# ---------------- NEXT FLOW (AI PLANNER) ----------------
st.divider()

st.subheader("📅 Next Step")

st.write("Go to AI Planner to create your personalized learning roadmap.")

if st.button("➡ Go to AI Planner"):
    st.switch_page("pages/7_AI_Planner.py")
