import streamlit as st
from utils.prompts import ats_prompt
from utils.validators import validate_ats
from services.gemini_service import ask_gemini
from utils.pdf_generator import create_pdf
from utils.file_reader import (
    extract_pdf_text,
    extract_docx_text,
    extract_txt_text
)

def show_ats_page():
    #page settings
    st.set_page_config(page_title="ATS Score Checker", page_icon="📊", layout="wide")

    uploaded_file = None
    resume_text = ""

    st.header( "📊 ATS Resume Score Checker")
    option = st.radio("Choose Resume Source",
                [
                    "Generated Resume",
                    "Upload Resume"
                ])
    if option == "Generated Resume":
        resume_text = st.session_state.get("resume","")

    else:
        uploaded_file = st.file_uploader("Upload Resume",type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        extension = uploaded_file.name.split(".")[-1]
        if extension == "pdf":
            resume_text = extract_pdf_text(uploaded_file)

        elif extension == "docx":
            resume_text = extract_docx_text(uploaded_file)

        else:
            resume_text = extract_txt_text(uploaded_file)

    # score Button
    if st.button("🚀 Check ATS Score"):
        is_valid, message = validate_ats(resume_text)
        if not is_valid:
            st.error(message)

        else:
            prompt = ats_prompt(resume_text)
            ats_result=ask_gemini(prompt)
            st.session_state.ats=ats_result
            if st.session_state.ats:
                st.markdown(st.session_state.ats)

            pdf_file=create_pdf(st.session_state.ats, "Minimal")
        
            # Download 
            with open(pdf_file,"rb") as file:
                    st.download_button(
                    label="📥 Download ATS Report",
                    data=file,
                    file_name="ats_report.pdf",
                    mime="application/pdf"
                    )