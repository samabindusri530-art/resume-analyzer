import streamlit as st
from analyzer import extract_text
from ai_engine import analyze_resume_ai, resume_chatbot

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer + ChatGPT Assistant")

uploaded_file = st.file_uploader("Upload Resume PDF")
job_role = st.text_input("Enter Job Role")

# store chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if uploaded_file:
    resume_text = extract_text(uploaded_file)

    st.success("Resume Loaded Successfully")

    # ---------------- ANALYZE BUTTON ----------------
    if st.button("Analyze Resume"):
        result = analyze_resume_ai(resume_text, job_role)
        st.subheader("📊 AI Analysis")
        st.write(result)

    # ---------------- CHATBOT ----------------
    st.subheader("💬 Chat with AI Resume Assistant")

    user_input = st.chat_input("Ask anything about your resume...")

    if user_input:
        response = resume_chatbot(resume_text, user_input, job_role)

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("AI", response))

    # display chat
    for role, msg in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"🧑‍💻 **You:** {msg}")
        else:
            st.markdown(f"🤖 **AI:** {msg}")
