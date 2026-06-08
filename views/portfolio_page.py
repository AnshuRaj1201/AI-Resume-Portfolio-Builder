import streamlit as st
from utils.prompts import portfolio_prompt
from utils.validators import validate_portfolio
from services.gemini_service import ask_gemini
from utils.pdf_generator import create_pdf

def show_portfolio_page():
    #page settings
    st.set_page_config(page_title="Portfolio Generator", page_icon="🌐", layout="wide")
    # Main heading
    st.header( "🌐 Portfolio Generator")

    #User Information
    name = st.text_input("Enter Your Name")
    email = st.text_input("Enter Your Email")
    education = st.text_area("Education")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects")
    achievements = st.text_area("Achievements (Optional)")
    linkedin = st.text_input("LinkedIn Profile")
    github = st.text_input("GitHub Profile")

    #Button
    if st.button("🚀 Generate Portfolio"):

        #valid
        is_valid, message = validate_portfolio(name, email, education, skills, projects)
        if not is_valid:
            st.error(message)
        else:
            prompt=portfolio_prompt(name, email, education, skills, projects, achievements, linkedin, github)
            portfolio=ask_gemini(prompt)
            st.session_state.portfolio=portfolio
            if st.session_state.portfolio:
                 st.markdown(st.session_state.portfolio)
            pdf_file=create_pdf(portfolio,"Modern")
        
            # Download 
            with open(pdf_file,"rb") as file:
                    st.download_button(
                    label="📥 Download Portfolio",
                    data=file,
                    file_name="portfolio.pdf",
                    mime="application/pdf"
                    )
                
    if st.button("🗑 Clear Portfolio"):
        st.session_state.portfolio = ""