import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


def analyze_resume_ai(resume_text, role):

    resume_text = resume_text[:8000]

    prompt = f"""
You are an expert resume analyzer.

Role: {role}

Resume:
{resume_text}

Return:
- Score (0-100)
- Skills found
- Missing skills
- Improvements
"""

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
