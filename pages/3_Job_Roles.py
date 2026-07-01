import streamlit as st
from skills import job_roles

# Back button
if st.button("Back to Home"):
    st.switch_page("app.py")

st.title("Job Role Skills")

for role, skills in job_roles.items():

    st.subheader(role)

    for skill in skills:
        st.write("-", skill)
