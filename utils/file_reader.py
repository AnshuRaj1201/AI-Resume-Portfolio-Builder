from pypdf import PdfReader
from docx import Document

def extract_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_docx_text(uploaded_file):
    document = Document(uploaded_file)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_txt_text(uploaded_file):
    return uploaded_file.read().decode("utf-8")

