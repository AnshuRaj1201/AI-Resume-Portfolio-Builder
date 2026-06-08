
def resume_prompt(name, email, phone, linkedin, github,
                  education, skills, projects, target_role=""):
 
    target_line = f"Target Role: {target_role}" if target_role else ""
 
    prompt = f"""
You are an expert ATS-friendly resume writer specialising in tech resumes for students and fresh graduates.
 
Your task is to generate a complete, professional resume in clean Markdown format using ONLY the student data provided below.
 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STUDENT DATA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name        : {name}
Email       : {email}
Phone       : {phone}
LinkedIn    : {linkedin}
GitHub      : {github}
{target_line}
 
Education:
{education}
 
Skills:
{skills}
 
Projects:
{projects}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 
OUTPUT FORMAT RULES — follow these exactly, no exceptions:
 
1. START with the student's name as a level-1 heading:
   # {name}
 
2. IMMEDIATELY after the name, write a blank line, then the SUMMARY section.
   DO NOT include a "Contact Information" section, contact bullets, or any
   repetition of email / phone / LinkedIn / GitHub — these are already printed
   by the system. Including them causes duplicate rendering bugs.
 
3. OUTPUT the sections in this EXACT order — no reordering, no skipping:
   a) # Name                  ← already done in rule 1
   b) ## Summary              ← 3–5 sentence professional paragraph
   c) ## Skills               ← grouped bullet list by category
   d) ## Projects             ← each project as ### sub-heading + bullets
   e) ## Education            ← degree, university, year, CGPA if provided
   f) ## Certifications       ← only if any certifications exist in the data
   g) ## Achievements         ← only if any achievements exist in the data
 
4. HEADINGS must use exactly ## for sections and ### for project names.
   Never use bold text (**text**) as a substitute for a heading.
 
5. BULLETS must use "- " (hyphen space) at the start of every bullet line.
   Never use "* " or numbers for bullets.
 
6. NEVER output --- (horizontal rules) anywhere in the response.
   The PDF renderer draws its own dividers; markdown rules create duplicates.
 
7. SUMMARY section:
   - 3 to 5 sentences only
   - Mention the degree, top technical skills, and target role if provided
   - Do not use "I" — write in third-person professional tone
 
8. SKILLS section format:
   - Group skills by category (e.g., AI & ML, Programming Languages, Tools)
   - Each category on its own bullet: "- Category Name: skill1, skill2, skill3"
   - Do not use sub-bullets
 
9. PROJECTS section format — for EACH project write:
   ### Project Name
   - One-line description of what the project does and the problem it solves.
   - Key technical implementation detail (algorithm, library, model used).
   - Measurable outcome or impact if known (accuracy %, users, performance).
   Use exactly 2–3 bullets per project. Be specific, not generic.
 
10. EDUCATION section format:
    - Degree name and field of study
    - University / Institution name
    - Year of graduation or expected graduation
    - CGPA or percentage if provided
    One bullet per item. Do not combine into a single line.
 
11. LANGUAGE: Use plain English only. No emojis, no special symbols,
    no Unicode characters, no smart quotes (" "), no em-dashes (—).
    Use only: letters, numbers, commas, periods, colons, hyphens, parentheses.
 
12. LENGTH: Aim for content that fills 1 to 2 pages when rendered as a PDF.
    Do not pad with filler sentences. Every bullet must add real value.
 
BEGIN the resume now. Output only the Markdown resume — no preamble,
no explanation, no commentary before or after the resume content.
"""
    return prompt.strip()
 
 
# ─────────────────────────────────────────────────────────────────────────────
# Quick test — prints the prompt so you can inspect it
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    sample = resume_prompt(
        name        = "Ashish Raj",
        email       = "ashishrajara16@gmail.com",
        phone       = "7070707480",
        linkedin    = "linkedin.com/in/ashiah-raj-ashishraj",
        github      = "github.com/ashishraj",
        education   = "B.Tech in Computer Science Engineering, Bhabha University, 2025, CGPA 8.2",
        skills      = "Python, C, Machine Learning, NLP, OpenCV, TensorFlow, Streamlit, FastAPI",
        projects    = """
1. Study Bot - NLP chatbot for study assistance using Gemini API and LangChain
2. Fitness Buddy - ML-powered fitness tracker app with Streamlit UI
3. Water Classifier - ML model to classify water quality, 94% accuracy
4. Movie Recommendation System - Collaborative filtering engine on 10k movie dataset
5. AI Resume & Portfolio Builder - Generative AI tool for resume and portfolio generation
""",
        target_role = "AI/ML Engineer Intern"
    )
    print(sample)

def cover_letter_prompt(name,job_role,company,skills,experience):
    prompt = f"""
    You are an expert HR manager.
    Write a professional cover letter.
    Candidate Name:
    {name}
    Job Role:
    {job_role}
    Company:
    {company}
    Skills:
    {skills}
    Experience:
    {experience}
    Requirements:
    Keep it professional.
    Keep it ATS friendly.
    Improve wording.
    Do not create fake achievements.
    End politely.
    """
    return prompt

def portfolio_prompt(name, email, education, skills, projects, achievements, linkedin, github):
    prompt = f"""
        You are an expert portfolio writer.
        Create a professional developer portfolio.
        Candidate Name:
        {name}
        Email:
        {email}
        Education:
        {education}
        Skills:
        {skills}
        Projects:
        {projects}
        Achievements:
        {achievements}
        LinkedIn:
        {linkedin}
        GitHub:
        {github}
        Requirements:
        Use Markdown.
        Use # for title.
        Use ## for sections.
        Use bullet points.
        Improve wording.
        Keep it professional.
        Do not invent fake information.
        """
    return prompt

def linkedin_prompt(name, education, skills, projects, goals):
    prompt = f"""
        You are an expert LinkedIn profile writer.
        Create a professional LinkedIn profile.
        Candidate Name:
        {name}
        Education:
        {education}
        Skills:
        {skills}
        Projects:
        {projects}
        Career Goals:
        {goals}
        Requirements:
        Generate:
        1. LinkedIn Headline
        2. About Section
        3. Top Skills
        4. Professional Bio
        Use Markdown formatting.
        Use # for main heading.
        Use ## for sections.
        Keep it professional.
        Do not invent fake information.
        """
    return prompt


def interview_prompt(name, job_role, skills, projects, experience):
    prompt = f"""
        You are an expert technical interviewer.
        Generate interview preparation material.
        Candidate Name:
        {name}
        Target Job Role:
        {job_role}
        Skills:
        {skills}
        Projects:
        {projects}
        Experience Level:
        {experience}
        Requirements:
        Generate:
        # HR Questions
        # Technical Questions
        # Project Based Questions
        # Suggested Preparation Tips
        Use Markdown.
        Use ## for sections.
        Use bullet points.
        Do not invent fake work experience.
        """
    return prompt

def ats_prompt(resume):
    prompt = f"""
        You are an ATS Resume Analyzer.
        Analyze this resume.
        Resume:
        {resume}
        Generate:
        1. ATS Score out of 100
        2. Keyword Analysis
        3. Formatting Review
        4. Missing Skills
        5. Project Quality
        6. Education Review
        7. Action Plan
        8. Final Recommendation 
        Use Markdown.
        Be realistic.
        Do not invent fake information.
        """
    return prompt