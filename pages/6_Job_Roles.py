import streamlit as st

if st.button("Back to Home"):
    st.switch_page("app.py")

st.title("AI Job Role Recommendation")

skills = st.text_area(
    "Enter Your Skills",
    placeholder="Example: python, sql, html"
)

if st.button("Recommend Role"):

    skills = skills.lower()

    if "python" in skills and "sql" in skills:
        st.success("Recommended Role: Data Analyst")

    elif "html" in skills and "css" in skills:
        st.success("Recommended Role: Frontend Developer")

    elif "machine learning" in skills:
        st.success("Recommended Role: Data Scientist")

    elif "java" in skills:
        st.success("Recommended Role: Software Engineer")

    else:
        st.warning("Need more technical skills")
