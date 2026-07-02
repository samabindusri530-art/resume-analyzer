import streamlit as st
import google.generativeai as genai

# Get API key from Streamlit secrets
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Use stable model
model = genai.GenerativeModel("gemini-1.5-flash")


def analyze_resume_ai(resume_text):

    prompt = f"""
You are an expert resume reviewer.

Analyze this resume and provide:

1. Resume score out of 10
2. Missing technical skills
3. 3 improvements needed
4. Suitable job roles

Resume:
{resume_text}
"""

    try:
        response = model.generate_content(prompt)

        # safety check
        if response and hasattr(response, "text"):
            return response.text
        else:
            return "No response received from Gemini."

    except Exception as e:
        return f"Gemini Error: {str(e)}"
