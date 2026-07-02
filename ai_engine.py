import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ✅ FIXED MODEL NAME
model = genai.GenerativeModel("models/gemini-1.5-flash")


def analyze_resume_ai(resume_text, role):

    prompt = f"""
You are a professional resume analyzer AI.

Role selected: {role}

Resume:
{resume_text}

Give:
1. Score (0-100)
2. Skills Found
3. Missing Skills
4. Improvements
"""

    response = model.generate_content(prompt)
    return response.text
