import streamlit as st
from company_skills import company_roles

if st.button("Back to Home"):
    st.switch_page("app.py")

st.title("Company Specific Resume Check")

company = st.selectbox(
    "Select Company",
    list(company_roles.keys())
)

skills = st.text_area(
    "Enter Your Skills"
)

if st.button("Check Match"):

    required = company_roles[company]

    found = []

    for skill in required:

        if skill in skills.lower():
            found.append(skill)

    score = int((len(found) / len(required)) * 100)

    st.subheader("Match Score")
    st.write(str(score) + "%")

    st.subheader("Matched Skills")
    st.write(found)
