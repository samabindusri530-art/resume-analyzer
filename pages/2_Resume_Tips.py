import streamlit as st

# Back button
if st.button("Back to Home"):
    st.switch_page("app.py")

st.title("Resume Improvement Tips")

tips = [

    "Add Projects Section",

    "Mention Technical Skills",

    "Add Certifications",

    "Keep Resume One Page",

    "Add GitHub Profile",

    "Use Professional Email",

    "Mention Achievements"

]

for tip in tips:
    st.write("•", tip)
