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

# ---------------- ROLE DETECTION ----------------
st.subheader("🎯 Recommended Career Opportunities")

# ---------------- DATA SCIENCE ----------------
if "python" in text and "sql" in text:

    st.success("📊 Data Analyst / Data Scientist Path")

    st.write("🏢 Companies: Google, Microsoft, Amazon, IBM, Deloitte")

    st.write("💼 Roles:")
    st.write("• Data Analyst (Entry Level)")
    st.write("• Business Analyst")
    st.write("• Junior Data Scientist")

    st.write("🚀 Internships:")
    st.write("• Data Analytics Intern")
    st.write("• Business Intelligence Intern")

    st.info("📚 Skills: Pandas, NumPy, Power BI, Excel, SQL Advanced")

    st.write("🌍 Career Growth:")
    st.write("Data Analyst → Data Scientist → Data Engineer")

# ---------------- AI/ML ----------------
elif "machine learning" in text:

    st.success("🤖 AI / ML Engineer Path")

    st.write("🏢 Companies: OpenAI, NVIDIA, Google DeepMind, Meta")

    st.write("💼 Roles:")
    st.write("• Machine Learning Engineer")
    st.write("• AI Research Assistant")

    st.write("🚀 Internships:")
    st.write("• AI Intern")
    st.write("• ML Intern")

    st.info("📚 Skills: TensorFlow, PyTorch, Deep Learning, NLP")

    st.write("🌍 Career Growth:")
    st.write("ML Engineer → AI Scientist → Research Scientist")

# ---------------- WEB DEV ----------------
elif "html" in text or "css" in text:

    st.success("🌐 Frontend Developer Path")

    st.write("🏢 Companies: Infosys, TCS, Flipkart, Amazon, Startups")

    st.write("💼 Roles:")
    st.write("• Frontend Developer")
    st.write("• UI Developer")

    st.write("🚀 Internships:")
    st.write("• Web Development Intern")

    st.info("📚 Skills: JavaScript, React, UI/UX, Tailwind CSS")

    st.write("🌍 Career Growth:")
    st.write("Frontend → Full Stack → Tech Lead")

# ---------------- JAVA ----------------
elif "java" in text:

    st.success("☕ Software Developer Path")

    st.write("🏢 Companies: Google, Microsoft, Adobe, Infosys")

    st.write("💼 Roles:")
    st.write("• Software Engineer")
    st.write("• Backend Developer")

    st.write("🚀 Internships:")
    st.write("• Software Development Intern")

    st.info("📚 Skills: DSA, Spring Boot, System Design")

    st.write("🌍 Career Growth:")
    st.write("Developer → Senior Engineer → Architect")

# ---------------- DEFAULT ----------------
else:

    st.warning("⚠ Limited skills detected")

    st.write("💡 Suggested Paths:")
    st.write("• Python Developer")
    st.write("• Web Development")
    st.write("• Data Analytics")

    st.write("🚀 Opportunities:")
    st.write("• Internship in IT companies")
    st.write("• Freelancing")
    st.write("• Open Source Contribution")

    st.info("📚 Learn: Python, SQL, HTML, Git, Projects")
