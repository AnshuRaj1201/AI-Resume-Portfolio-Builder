import streamlit as st
from utils.prompts import linkedin_prompt
from utils.validators import validate_linkedin
from services.gemini_service import ask_gemini
from utils.pdf_generator import create_pdf

def show_linkedin_page():
    #page settings
    st.set_page_config(page_title="LinkedIn Summary", page_icon="💼", layout="wide")
    st.header( "💼 LinkedIn Summary Generator")

    #User Information
    name = st.text_input("Enter Your Name")
    education = st.text_area("Education")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects (Optional")
    goals = st.text_input("Career Goals (Optional)")

    #Button
    if st.button("🚀 Generate LinkedIn Summary"):

        #valid
        is_valid, message = validate_linkedin(name, education, skills)
        if not is_valid:
            st.error(message)
        else:
            prompt=linkedin_prompt(name, education, skills, projects, goals)
            linkedin=ask_gemini(prompt)
            st.session_state.linkedin=linkedin
            if st.session_state.linkedin:
                st.markdown(st.session_state.linkedin)
            pdf_file=create_pdf(linkedin)
        
            # Download 
            with open(pdf_file,"rb") as file:
                    st.download_button(
                    label="📥 Download Summary",
                    data=file,
                    file_name="linkedin_summary.pdf",
                    mime="application/pdf"
                    )