import streamlit as st

# ---------------- CHECK RESUME EXISTS ----------------
if "resume_text" not in st.session_state:
    st.warning("⚠ Please upload your resume first on Home page")
    st.stop()

# ---------------- NAVIGATION (NO BACK TO HOME STYLE) ----------------
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅ Previous Page"):
        st.switch_page("pages/resume_analyzer.py")

with col2:
    if st.button("➡ Next Page"):
        st.switch_page("pages/suggestions.py")

st.title("🤖 AI Resume Tips")

st.write("Get personalized resume improvement tips based on your profile.")

# ---------------- RESUME TYPE ----------------
resume_type = st.selectbox(
    "Select Resume Type",
    ["Student", "Software Engineer", "Data Scientist"]
)

# ---------------- BUTTON ----------------
if st.button("✨ Get AI Tips"):

    st.divider()

    # ---------------- STUDENT ----------------
    if resume_type == "Student":
        st.subheader("🎓 Tips for Students")

        st.write("""
        • Add academic projects  
        • Mention certifications  
        • Add GitHub profile  
        • Keep resume one page  
        """)

    # ---------------- SOFTWARE ENGINEER ----------------
    elif resume_type == "Software Engineer":
        st.subheader("💻 Tips for Software Engineers")

        st.write("""
        • Add DSA skills  
        • Mention backend/frontend skills  
        • Add internship experience  
        • Show coding profiles  
        """)

    # ---------------- DATA SCIENTIST ----------------
    elif resume_type == "Data Scientist":
        st.subheader("📊 Tips for Data Scientists")

        st.write("""
        • Add machine learning projects  
        • Mention Python libraries  
        • Add Kaggle/GitHub links  
        • Show data visualization skills  
        """)

    st.divider()

    # ---------------- COMMON MISTAKES ----------------
    st.subheader("❌ Common Resume Mistakes")

    st.write("""
    ❌ Too much text  
    ❌ Missing projects  
    ❌ No GitHub / LinkedIn links  
    ❌ Weak skills section  
    ❌ No achievements section  
    ❌ Grammar or spelling mistakes  
    ❌ Unprofessional email address  
    """)

# ---------------- EXTRA FLOW BUTTON ----------------
st.divider()

st.write("👉 Continue improving your resume")

if st.button("➡ Go to Final Suggestions Page"):
    st.switch_page("pages/suggestions.py")
