import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_resume_ai(resume_text, role):

    prompt = f"""
You are an expert resume analyzer.

User selected role: {role}

Analyze the resume and give:

1. Resume Score (0-100)
2. Skills Found
3. Missing Skills
4. Improvements
5. Job Fit Explanation

Resume:
{resume_text}
"""

    response = model.generate_content(prompt)
    return response.text
