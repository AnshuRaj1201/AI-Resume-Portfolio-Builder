import streamlit as st
from views.resume_page import show_resume_page
from views.cover_letter_page import show_cover_letter_page
from views.portfolio_page import show_portfolio_page
from views.linkedin_page import show_linkedin_page
from views.interview_page import show_interview_page
from views.home_page import show_home_page
from views.ats_page import show_ats_page

# Page settings
st.set_page_config(page_title="AI Resume Builder", page_icon="🤖", layout="wide")


st.sidebar.title("🧠AI Career Assistant")

menu = st.sidebar.selectbox(
    "Choose Feature",
    [   "🏠 Home",
        "📝 Resume Generator",
        "📊 ATS Score Checker",
        "💌 Cover Letter Generator",
        "🌐 Portfolio Generator",
        "💼 LinkedIn Summary",
        "🎯 Interview Questions"
    ]
)

if menu == "🏠 Home":
    show_home_page()
elif menu == "📝 Resume Generator":
    show_resume_page()
elif menu == "📊 ATS Score Checker":
    show_ats_page()
elif menu == "💌 Cover Letter Generator":
    show_cover_letter_page()
elif menu == "🌐 Portfolio Generator":
    show_portfolio_page()
elif menu == "💼 LinkedIn Summary":
    show_linkedin_page()
elif menu == "🎯 Interview Questions":
    show_interview_page()

if "resume" not in st.session_state:
    st.session_state.resume = ""

if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = ""

if "portfolio" not in st.session_state:
    st.session_state.portfolio = ""

if "linkedin" not in st.session_state:
    st.session_state.linkedin = ""

if "interview" not in st.session_state:
    st.session_state.interview = ""

if "ats" not in st.session_state:
    st.session_state.ats = ""

if "template" not in st.session_state:
    st.session_state.template = "Classic"

if "email" not in st.session_state:
    st.session_state.email = ""

if "phone" not in st.session_state:
    st.session_state.phone = ""

if "linkedin" not in st.session_state:
    st.session_state.linkedin = ""

if "github" not in st.session_state:
    st.session_state.github = ""