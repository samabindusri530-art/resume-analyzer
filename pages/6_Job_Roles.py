import streamlit as st

# ---------------- CHECK RESUME ----------------
if "resume_text" not in st.session_state:
    st.warning("⚠ Please upload your resume first on Home page")
    st.stop()

# ---------------- NAVIGATION ----------------
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅ Previous Page"):
        st.switch_page("pages/career_advisor.py")

with col2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

st.title("🎯 AI Job Role Recommendation")

st.write("Enter your skills or use resume-based analysis")

# ---------------- INPUT ----------------
skills_input = st.text_area(
    "Enter Your Skills",
    placeholder="Example: python, sql, html"
)

# ---------------- BUTTON ----------------
if st.button("🚀 Recommend Role"):

    skills = skills_input.lower()

    st.divider()

    # ---------------- DATA ANALYST ----------------
    if "python" in skills and "sql" in skills:

        st.success("🎯 Recommended Role: Data Analyst")

        st.subheader("🏢 Top Companies")
        st.write("""
        • Google  
        • Microsoft  
        • Amazon  
        """)

        st.subheader("📚 Skills to Improve")
        st.write("""
        • Pandas  
        • NumPy  
        • Power BI / Tableau  
        • Data Visualization  
        """)

    # ---------------- FRONTEND ----------------
    elif "html" in skills and "css" in skills:

        st.success("🎯 Recommended Role: Frontend Developer")

        st.subheader("🏢 Top Companies")
        st.write("""
        • Flipkart  
        • Infosys  
        • TCS  
        """)

        st.subheader("📚 Skills to Improve")
        st.write("""
        • JavaScript  
        • React  
        • APIs  
        • UI/UX Design  
        """)

    # ---------------- DATA SCIENTIST ----------------
    elif "machine learning" in skills:

        st.success("🎯 Recommended Role: Data Scientist")

        st.subheader("🏢 Top Companies")
        st.write("""
        • Google  
        • OpenAI  
        • NVIDIA  
        """)

        st.subheader("📚 Skills to Improve")
        st.write("""
        • TensorFlow  
        • PyTorch  
        • Deep Learning  
        • Model Deployment  
        """)

    # ---------------- SOFTWARE ENGINEER ----------------
    elif "java" in skills or "c++" in skills:

        st.success("🎯 Recommended Role: Software Engineer")

        st.subheader("🏢 Top Companies")
        st.write("""
        • Google  
        • Microsoft  
        • Adobe  
        """)

        st.subheader("📚 Skills to Improve")
        st.write("""
        • Data Structures  
        • Algorithms  
        • System Design  
        • Problem Solving  
        """)

    # ---------------- DEFAULT ----------------
    else:

        st.warning("⚠ Need more technical skills")

        st.subheader("📌 Suggested Learning Path")
        st.write("""
        • Python  
        • SQL  
        • Git & GitHub  
        • Web Development  
        • Data Structures  
        """)

# ---------------- FLOW BUTTON ----------------
st.divider()

st.write("👉 Continue learning path")

if st.button("🏠 Go to Dashboard"):
    st.switch_page("app.py")
