import streamlit as st
from utils.resume_generator import welcome
from services.gemini_service import ask_gemini
from utils.prompts import resume_prompt
from utils.pdf_generator import create_pdf
from utils.validators import validate_resume


def show_resume_page():
    #page settings
    st.set_page_config(page_title="Resume Generator", page_icon="📝", layout="wide")
    st.header( "📝 Resume Generator")
    #Description
    st.write("Generate ATS-friendly resumes.")
    
    #User Information
    name = st.text_input("Enter Your Name")
    email = st.text_input("Enter Your Email")
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL")
    education = st.text_area("Education")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    
    template = st.selectbox(
        "Choose Resume Template",
        ["Classic", "Modern","Minimal"]
    )

    #Button
    if st.button("🚀 Generate AI Resume"):

        #valid
        is_valid, message = validate_resume(name, email, education, skills, projects)
        if not is_valid:
            st.error(message)
        else:
            prompt=resume_prompt(name, email, phone, linkedin, github, education, skills, projects)
            st.write(welcome(name))
            resume=ask_gemini(prompt)
            # save file in sessions
            st.session_state.resume = resume
            st.session_state.template=template

            if st.session_state.resume:
                st.markdown(st.session_state.resume)
            pdf_file=create_pdf(resume, template, email, phone, linkedin, github)

            #save in session
            st.session_state.email = email
            st.session_state.phone = phone
            st.session_state.linkedin = linkedin
            st.session_state.github = github
        
            # Download 
            with open(pdf_file,"rb") as file:
                    st.download_button(
                    label="📥 Download Resume",
                    data=file,
                    file_name="resume.pdf",
                    mime="application/pdf"
                    )
    
    if st.button("🗑 Clear Resume"):
        st.session_state.resume = ""