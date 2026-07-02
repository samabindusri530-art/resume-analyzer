import streamlit as st
from ai_engine import analyze_resume_ai

st.title("💡 Resume Tips & Mistakes")

resume_text = st.session_state.get("resume_text", "")
job_role = st.session_state.get("job_role", "General")

if resume_text:

    prompt = f"""
Analyze this resume and give:

1. Resume Improvement Tips
2. Common Mistakes in Resume
3. Formatting Issues
4. What to fix first

Resume:
{resume_text}
"""

    from ai_engine import safe_call

    result = safe_call([{"role": "user", "content": prompt}])

    st.write(result)

else:
    st.warning("Please upload resume in previous page")

# ---------------- NEXT PAGE ----------------
if st.button("Next ➡ Career Advisor"):
    st.switch_page("pages/5_AI_Career_Advisor.py")
