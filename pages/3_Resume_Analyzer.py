import streamlit as st
import google.generativeai as genai

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_resume_ai(resume_text):

    prompt = f"""
Analyze this resume.

Give:
1. Resume score out of 10
2. Missing technical skills
3. Improvements needed
4. Suitable job roles

Resume:
{resume_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"
