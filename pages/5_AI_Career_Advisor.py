import streamlit as st

# Back button
if st.button("Back to Home"):
    st.switch_page("app.py")

st.title("AI Career Advisor")

st.write("Enter your skills and get career suggestions")

skills = st.text_area(
    "Enter Your Skills",
    placeholder="Example: python, sql, html, css"
)

if st.button("Analyze Career Path"):

    skills = skills.lower()

    # Data Science / Analyst
    if "python" in skills and "sql" in skills:

        st.success("Best Career Path: Data Analyst / Data Scientist")

        st.subheader("Recommended Companies")
        st.write("• Google")
        st.write("• Microsoft")
        st.write("• Amazon")

        st.subheader("Skills To Improve")
        st.write("• Pandas")
        st.write("• NumPy")
        st.write("• Machine Learning")
        st.write("• Data Visualization")

    # Frontend Developer
    elif "html" in skills and "css" in skills:

        st.success("Best Career Path: Frontend Developer")

        st.subheader("Recommended Companies")
        st.write("• Flipkart")
        st.write("• Infosys")
        st.write("• TCS")

        st.subheader("Skills To Improve")
        st.write("• JavaScript")
        st.write("• React")
        st.write("• APIs")
        st.write("• UI/UX Design")

    # Software Engineer
    elif "java" in skills or "c++" in skills:

        st.success("Best Career Path: Software Engineer")

        st.subheader("Recommended Companies")
        st.write("• Google")
        st.write("• Microsoft")
        st.write("• Adobe")

        st.subheader("Skills To Improve")
        st.write("• Data Structures")
        st.write("• Algorithms")
        st.write("• System Design")
        st.write("• Problem Solving")

    # AI/ML Engineer
    elif "machine learning" in skills or "deep learning" in skills:

        st.success("Best Career Path: AI / ML Engineer")

        st.subheader("Recommended Companies")
        st.write("• OpenAI")
        st.write("• NVIDIA")
        st.write("• Google DeepMind")

        st.subheader("Skills To Improve")
        st.write("• TensorFlow")
        st.write("• PyTorch")
        st.write("• Neural Networks")
        st.write("• Model Deployment")

    else:

        st.warning("Need more technical skills")

        st.subheader("Suggested Skills To Learn")
        st.write("• Python")
        st.write("• SQL")
        st.write("• Git & GitHub")
        st.write("• Data Structures")
        st.write("• Web Development")
