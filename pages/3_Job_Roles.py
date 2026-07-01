import streamlit as st
from skills import job_roles

st.title("Job Role Skills")

for role, skills in job_roles.items():

    st.subheader(role)

    for skill in skills:
        st.write("-", skill)
