import streamlit as st

def show_home_page():
    # Page settings
    st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")
    with st.container():
        st.title("🚀 AI Career Assistant")
        st.subheader("AI Resume & Portfolio Builder")

    st.write("""
        Generate Professional Resumes,
        Cover Letters, 
        Portfolios,
        LinkedIn Summaries,
        and interview preparation
        using Generative AI."""
    )
    st.divider()

    with st.expander("How to Use This App"):
        st.write("""
            Step 1:
            Choose Feature

            Step 2:
            Enter Details

            Step 3:
            Generate AI Content

            Step 4:
            Download PDF
            """
        )

    #Feature Section
    st.divider()
    st.header("✨ Features")

    col1, col2 = st.columns(2)
    with col1:
        st.success("📝 Resume Generator")
        st.success("📊 ATS Score Checker")
        st.success("🌐 Portfolio Generator")

    with col2:
        st.success("💼 LinkedIn Summary")
        st.success("💌 Cover Letter Generator")
        st.success("🎯 Interview Generator")

    #Tech Stack 
    st.divider()
    st.header("🛠 Technology Stack")
    st.markdown("""
        - Python

        - Streamlit

        - Gemini AI

        - FPDF

        - dotenv 
        """
    )

    #show matric
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("AI Features", 6)

    with col2:
        st.metric("PDF Export","Yes")

    with col3:
        st.metric("AI Model","Gemini")

    #Footer
    st.divider()
    st.caption("Built with ❤️ using Python and Generative AI")