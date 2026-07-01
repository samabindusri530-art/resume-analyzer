import streamlit as st

# ---------------- CHECK RESUME ----------------
if "resume_text" not in st.session_state:
    st.warning("⚠ Please upload your resume first on Home page")
    st.stop()

# ---------------- NAVIGATION ----------------
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅ Previous Page"):
        st.switch_page("pages/ai_tips.py")

with col2:
    if st.button("➡ Next Page"):
        st.switch_page("app.py")

st.title("🤖 AI Career Advisor")

st.write("Get career suggestions based on your skills or resume")

# ---------------- INPUT ----------------
skills_input = st.text_area(
    "Enter Your Skills",
    placeholder="Example: python, sql, html, css"
)

# ---------------- BUTTON ----------------
if st.button("🔍 Analyze Career Path"):

    skills = skills_input.lower()

    st.divider()

    # ---------------- DATA SCIENCE ----------------
    if "python" in skills and "sql" in skills:

        st.success("🎯 Best Career Path: Data Analyst / Data Scientist")

        st.subheader("🏢 Recommended Companies")
        st.write("""
        • Google  
        • Microsoft  
        • Amazon  
        """)

        st.subheader("📚 Skills To Improve")
        st.write("""
        • Pandas  
        • NumPy  
        • Machine Learning  
        • Data Visualization  
        """)

    # ---------------- FRONTEND ----------------
    elif "html" in skills and "css" in skills:

        st.success("🎯 Best Career Path: Frontend Developer")

        st.subheader("🏢 Recommended Companies")
        st.write("""
        • Flipkart  
        • Infosys  
        • TCS  
        """)

        st.subheader("📚 Skills To Improve")
        st.write("""
        • JavaScript  
        • React  
        • APIs  
        • UI/UX Design  
        """)

    # ---------------- SOFTWARE ENGINEER ----------------
    elif "java" in skills or "c++" in skills:

        st.success("🎯 Best Career Path: Software Engineer")

        st.subheader("🏢 Recommended Companies")
        st.write("""
        • Google  
        • Microsoft  
        • Adobe  
        """)

        st.subheader("📚 Skills To Improve")
        st.write("""
        • Data Structures  
        • Algorithms  
        • System Design  
        • Problem Solving  
        """)

    # ---------------- AI / ML ----------------
    elif "machine learning" in skills or "deep learning" in skills:

        st.success("🎯 Best Career Path: AI / ML Engineer")

        st.subheader("🏢 Recommended Companies")
        st.write("""
        • OpenAI  
        • NVIDIA  
        • Google DeepMind  
        """)

        st.subheader("📚 Skills To Improve")
        st.write("""
        • TensorFlow  
        • PyTorch  
        • Neural Networks  
        • Model Deployment  
        """)

    # ---------------- DEFAULT ----------------
    else:

        st.warning("⚠ Need more technical skills")

        st.subheader("📌 Suggested Skills To Learn")
        st.write("""
        • Python  
        • SQL  
        • Git & GitHub  
        • Data Structures  
        • Web Development  
        """)

# ---------------- FLOW BUTTON ----------------
st.divider()

st.write("👉 Continue your career journey")

if st.button("➡ Go to Home / Dashboard"):
    st.switch_page("app.py")
