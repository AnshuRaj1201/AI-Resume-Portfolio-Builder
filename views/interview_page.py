import streamlit as st
from utils.prompts import interview_prompt
from utils.validators import validate_interview
from services.gemini_service import ask_gemini
from utils.pdf_generator import create_pdf

def show_interview_page():
    #page settings
    st.set_page_config(page_title="Interview Questions", page_icon="🎯", layout="wide")
    st.header("🎯 AI Interview Questions Generator")

    #User Information
    name = st.text_input("Enter Your Name")
    job_role = st.text_input("Target Job Role")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects (Optional)")
    experience = st.selectbox("Experience Level",
        [
            "Fresher",
            "Intern",
            "0-1 Years",
            "1-3 Years"
        ]
    )

    #Button
    if st.button("🚀 Generate Interview Questions"):

        #valid
        is_valid, message = validate_interview(name, job_role, skills)
        if not is_valid:
            st.error(message)
        else:
            prompt=interview_prompt(name, job_role, skills, projects, experience)
            interview=ask_gemini(prompt)
            st.session_state.interview=interview
            if st.session_state.interview:
                st.markdown(st.session_state.interview)
            pdf_file=create_pdf(interview)
        
            # Download 
            with open(pdf_file,"rb") as file:
                    st.download_button(
                    label="📥 Download Interview Questions",
                    data=file,
                    file_name="interview_questions.pdf",
                    mime="application/pdf"
                    )

    