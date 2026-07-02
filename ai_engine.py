from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def analyze_resume_ai(resume_text, role):

    resume_text = resume_text[:8000]

    prompt = f"""
You are an expert resume analyzer and recruiter.

Role: {role}

Resume:
{resume_text}

Return clearly:

1. Resume Score (0-100)
2. Skills Found
3. Missing Skills
4. Improvements
5. Career Advice
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def resume_chatbot(resume_text, message, role):

    prompt = f"""
You are a friendly AI Resume Chat Assistant.

Rules:
- Help improve resume
- Act like a career coach
- Be short and clear

Role: {role}

Resume:
{resume_text}

User Question:
{message}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
