import streamlit as st
from services.gemini_service import  ask_gemini
from utils.prompts import cover_letter_prompt
from utils.pdf_generator import create_pdf
from utils.validators import validate_cover_letter

def show_cover_letter_page():
    #page settings
    st.set_page_config(page_title="Cover Letter", page_icon="💌", layout="wide")
    st.header( "💌 Cover Letter Generator")
    #Description
    st.write("Generate ATS-friendly Covers.")

    #User Information
    name = st.text_input("Enter Your Name")
    job_role = st.text_input("Job Role")
    company = st.text_input("Company Name")
    skills = st.text_area("Skills")
    experience = st.text_area("Experience")

    #Generate button
    if st.button("🚀 Generate Cover Letter"):
        is_valid, message=validate_cover_letter(name, job_role, company)
        if not is_valid:
            st.error(message)
        else:
            prompt=cover_letter_prompt(name, job_role, company, skills, experience)
            cover_letter=ask_gemini(prompt)
            st.session_state.cover_letter=cover_letter
            if st.session_state.cover_letter:
                st.markdown(st.session_state.cover_letter)
            pdf_file=create_pdf(st.session_state.cover_letter,"Minimal")

            with open(pdf_file, "rb") as file:
                st.download_button("📥 Download Cover Letter", 
                                   data=file, 
                                   file_name="cover_letter.pdf", 
                                   mime="application/pdf"
                                   )