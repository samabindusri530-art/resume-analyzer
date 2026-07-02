import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


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

    response = client.models.generate_content(
        model="models/gemini-1.5-flash",
        contents=prompt
    )

    return response.text
