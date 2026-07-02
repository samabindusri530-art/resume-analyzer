import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_resume_ai(resume_text, role):

    prompt = f"""
Role: {role}

Resume:
{resume_text}

Give:
- Score (0-100)
- Skills found
- Missing skills
- Improvements
"""

    response = model.generate_content(prompt)
    return response.text
