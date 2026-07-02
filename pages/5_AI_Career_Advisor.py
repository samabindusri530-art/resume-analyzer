import streamlit as st
from ai_engine import safe_call

st.title("🧠 AI Career Advisor")

resume_text = st.session_state.get("resume_text", "")

if resume_text:

    prompt = f"""
You are a career advisor.

Based on this resume:

1. Best job roles
2. Career path
3. Skills to learn
4. Roadmap (step by step)

Resume:
{resume_text}
"""

    result = safe_call([{"role": "user", "content": prompt}])

    st.write(result)

else:
    st.warning("Please upload resume first")
