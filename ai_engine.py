import streamlit as st
import google.generativeai as genai

# Read API key from Streamlit Secrets
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume_ai(resume_text):

    prompt = f"""
    Analyze the following resume.

    Give me:

    1. Resume score out of 10
    2. Missing technical skills
    3. Improvements needed
    4. Suitable career suggestions

    Resume:
    {resume_text}
    """

    try:
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error: {e}"
