from dotenv import load_dotenv
import os
import google.generativeai as genai

#Loading dotenv
load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

#model
model=genai.GenerativeModel("gemini-2.5-flash")

#input
def ask_gemini(prompt):
    response=model.generate_content(prompt)
    return response.text
