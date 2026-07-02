import requests
import streamlit as st

# Read token from Streamlit Secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

# Hugging Face model
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def analyze_resume(resume_text):

    prompt = f"""
    Analyze this resume and provide:

    1. Resume score out of 10
    2. Missing skills
    3. Improvements needed
    4. Career suggestions

    Resume:
    {resume_text}
    """

    payload = {
        "inputs": prompt
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=payload
    )

    return response.json()
