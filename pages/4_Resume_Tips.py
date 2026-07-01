import streamlit as st

if st.button("Back to Home"):
    st.switch_page("app.py")

st.title("AI Resume Tips")

resume_type = st.selectbox(
    "Select Resume Type",
    ["Student", "Software Engineer", "Data Scientist"]
)

if st.button("Get AI Tips"):

    if resume_type == "Student":
        st.write("• Add academic projects")
        st.write("• Mention certifications")
        st.write("• Add GitHub profile")
        st.write("• Keep resume one page")

    elif resume_type == "Software Engineer":
        st.write("• Add DSA skills")
        st.write("• Mention backend/frontend skills")
        st.write("• Add internship experience")
        st.write("• Show coding profiles")

    elif resume_type == "Data Scientist":
        st.write("• Add machine learning projects")
        st.write("• Mention Python libraries")
        st.write("• Add Kaggle/GitHub links")
        st.write("• Show data visualization skills")
