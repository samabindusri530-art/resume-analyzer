import streamlit as st
from analyzer import extract_text
from ai_engine import analyze_resume_ai

st.title("🤖 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    resume_text = extract_text(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.write(resume_text)

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing with AI..."):
            result = analyze_resume_ai(resume_text)

        st.subheader("AI Analysis Result")
        st.write(result)
