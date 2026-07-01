import streamlit as st

# Back button
if st.button("Back to Home"):
    st.switch_page("app.py")

st.title("AI Resume Tips")

resume_type = st.selectbox(
    "Select Resume Type",
    ["Student", "Software Engineer", "Data Scientist"]
)

if st.button("Get AI Tips"):

    # Student Resume Tips
    if resume_type == "Student":
        st.subheader("Tips for Students")

        st.write("• Add academic projects")
        st.write("• Mention certifications")
        st.write("• Add GitHub profile")
        st.write("• Keep resume one page")

    # Software Engineer Resume Tips
    elif resume_type == "Software Engineer":
        st.subheader("Tips for Software Engineers")

        st.write("• Add DSA skills")
        st.write("• Mention backend/frontend skills")
        st.write("• Add internship experience")
        st.write("• Show coding profiles")

    # Data Scientist Resume Tips
    elif resume_type == "Data Scientist":
        st.subheader("Tips for Data Scientists")

        st.write("• Add machine learning projects")
        st.write("• Mention Python libraries")
        st.write("• Add Kaggle/GitHub links")
        st.write("• Show data visualization skills")

    # Common mistakes for everyone
    st.subheader("Common Resume Mistakes")

    st.write("❌ Too much text")
    st.write("❌ Missing projects")
    st.write("❌ No GitHub / LinkedIn links")
    st.write("❌ Weak skills section")
    st.write("❌ No achievements section")
    st.write("❌ Grammar or spelling mistakes")
    st.write("❌ Unprofessional email address")
