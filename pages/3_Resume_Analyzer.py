import streamlit as st
import matplotlib.pyplot as plt
from analyzer import extract_text
from ai_engine import analyze_resume_ai
from skills import job_roles

st.title("📄 Resume Analyzer")

role = st.selectbox(
    "Select Job Role",
    list(job_roles.keys())
)

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    st.subheader("Extracted Text")
    st.write(resume_text)

    if st.button("Analyze Resume 🤖"):

        result = analyze_resume_ai(resume_text, role)

        st.subheader("AI Result")
        st.write(result)

        # ---------------- SCORE (basic example)
        score = 80

        st.subheader("📊 Resume Score")

        fig, ax = plt.subplots()
        ax.bar(["Score"], [score])
        ax.set_ylim(0, 100)
        st.pyplot(fig)

        # ---------------- SKILLS
        required = set(job_roles[role])
        found = set(resume_text.split())

        matched = list(required & found)
        missing = list(required - found)

        st.subheader("🟢 Skills Found")
        st.write(matched)

        st.subheader("🔴 Missing Skills")
        st.write(missing)

        # Save for next pages
        st.session_state["result"] = result
        st.session_state["score"] = score
        st.session_state["matched"] = matched
        st.session_state["missing"] = missing

        if st.button("➡️ Next: Resume Tips"):
            st.switch_page("pages/4_Resume_Tips")
