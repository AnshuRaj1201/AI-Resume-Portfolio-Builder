<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=28&pause=1000&color=6C63FF&center=true&vCenter=true&width=700&lines=AI+Resume+%26+Portfolio+Builder;Powered+by+Google+Gemini+AI;Generate+%7C+Optimize+%7C+Get+Hired" alt="Typing SVG" />

<br/>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/FPDF-00897B?style=for-the-badge&logo=adobeacrobatreader&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  <a href="[YOUR_STREAMLIT_APP_LINK](https://ai-resume-portfolio-builder-ashish.streamlit.app/)">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit" height="35"/>
  </a>
</p>

<h3>
  🤖 An intelligent, AI-powered web application that generates<br/>
  professional resumes, cover letters, portfolios & ATS reports<br/>
  in seconds — tailored specifically for students and freshers.
</h3>

<br/>

> **🌐 Live App:** [Click here to try it now →](YOUR_STREAMLIT_APP_LINK)
> 
> Deployed on **Streamlit Community Cloud** — free, fast, no setup needed.

</div>

---

## 📸 Preview

<div align="center">

| Resume Generator | ATS Checker | Cover Letter |
|:---:|:---:|:---:|
| ![Resume](https://via.placeholder.com/280x180/6C63FF/ffffff?text=Resume+Generator) | ![ATS](https://via.placeholder.com/280x180/FF4B4B/ffffff?text=ATS+Checker) | ![Cover](https://via.placeholder.com/280x180/00897B/ffffff?text=Cover+Letter) |

> 💡 Replace the placeholders above with actual screenshots of your app for maximum impact.

</div>

---

## 🎯 Problem Statement

Most students and freshers struggle to present themselves professionally when applying for jobs and internships. The traditional approach is painful:

| ❌ Old Way | ✅ With This App |
|---|---|
| Hours spent formatting manually | Resume generated in **seconds** |
| Generic templates for everyone | **AI-tailored** to your skills & role |
| No idea if it passes ATS filters | **ATS score + fix suggestions** included |
| Expensive resume writing services | **Completely free** to use |
| No portfolio without a website | **Portfolio structure** auto-generated |

---

## ✨ Features

<details open>
<summary><b>📄 AI Resume Generator</b></summary>
<br/>

Generate a complete, ATS-friendly resume from your details in one click.

- **3 Professional Templates** — Classic, Modern, Minimal
- **AI-Written Content** — Summary, bullet points, skills sections crafted by Gemini
- **PDF Download** — Instantly downloadable, ready to submit
- **Input:** Name, Education, Skills, Projects, Contact, LinkedIn, GitHub

</details>

<details>
<summary><b>📊 ATS Resume Checker</b></summary>
<br/>

Upload your existing resume and get a full ATS compatibility analysis.

- **ATS Score** out of 100
- **Keyword Gap Analysis** — what's missing for your target role
- **Strengths & Weaknesses** breakdown
- **Actionable Improvement Suggestions**
- **Supports:** PDF, DOCX, TXT uploads

</details>

<details>
<summary><b>📋 AI Cover Letter Generator</b></summary>
<br/>

Personalized cover letters tailored to the specific job role.

- Role-specific tone and language
- Highlights your most relevant skills and projects
- Professional formatting, ready to copy or download as PDF

</details>

<details>
<summary><b>🌐 AI Portfolio Generator</b></summary>
<br/>

Generate a structured professional portfolio covering:

- **About Me** section
- **Skills** showcase
- **Projects** with descriptions
- **Education** timeline
- **Contact Information**

Perfect for students, developers, and freelancers building their online presence.

</details>

<details>
<summary><b>🎯 AI Interview Question Generator</b></summary>
<br/>

Prepare smarter with AI-generated interview questions based on your own resume.

- Questions tailored to your **skills and projects**
- Covers **technical and behavioral** rounds
- Domain-specific question sets

</details>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│                    User Input                        │
│     (Name, Skills, Education, Projects, Role)        │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│              Streamlit Frontend                      │
│          Multi-page interactive UI                   │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│           Prompt Engineering Layer                   │
│   Structured prompts with role, tone & format rules  │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│             Google Gemini API                        │
│         AI content generation engine                 │
└──────────────────────┬──────────────────────────────┘
                       │
              ┌────────┴────────┐
              ▼                 ▼
┌─────────────────┐   ┌─────────────────────────────┐
│  PDF Generator  │   │      ATS Analysis Engine     │
│  (FPDF + rules) │   │  (Score + keyword matching)  │
└────────┬────────┘   └──────────────┬──────────────┘
         │                           │
         └────────────┬──────────────┘
                      ▼
            ┌──────────────────┐
            │  Download / View │
            └──────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | Streamlit | Interactive multi-page web UI |
| **Backend** | Python 3.10+ | Core application logic |
| **AI Engine** | Google Gemini API | Content generation & analysis |
| **PDF Export** | FPDF | Resume & report PDF generation |
| **Resume Parsing** | PyPDF2, python-docx | ATS checker file uploads |
| **Config** | python-dotenv | Secure API key management |
| **Version Control** | Git + GitHub | Source code management |
| **Deployment** | Streamlit Community Cloud | Live hosting |

---

## 📂 Project Structure

```
AI-Resume-Portfolio-Builder/
│
├── 📄 app.py                    # Main entry point, page routing
├── 📋 requirements.txt          # Python dependencies
├── 📖 README.md                 # You are here
├── 🔒 .gitignore                # Ignores .env, __pycache__, etc.
│
├── 📁 views/                    # UI pages (one file per feature)
│   ├── resume_page.py           # Resume generator page
│   ├── ats_page.py              # ATS checker page
│   ├── cover_letter_page.py     # Cover letter generator page
│   └── portfolio_page.py        # Portfolio generator page
│
├── 📁 utils/                    # Core business logic
│   ├── gemini_api.py            # Gemini API wrapper
│   ├── prompts.py               # All prompt templates
│   ├── pdf_generator.py         # PDF creation engine
│   ├── validators.py            # Input validation helpers
│   └── file_extractors.py       # PDF/DOCX/TXT text extraction
│
└── 📁 assets/                   # Static files, images, icons
```

---

## ⚡ Quick Start

### Prerequisites

- Python 3.10 or higher
- A Google Gemini API key ([Get one free here](https://makersuite.google.com/app/apikey))

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/ashishraj-hub/AI-Resume-Portfolio-Builder.git

# 2. Navigate into the project
cd AI-Resume-Portfolio-Builder

# 3. Create a virtual environment
python -m venv venv

# 4. Activate the environment
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Set up your API key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# 7. Run the app
streamlit run app.py
```

Open your browser and go to `http://localhost:8501` 🎉

---

## 🌐 Deployment

This project is **live** on Streamlit Community Cloud.

**🔗 Live URL:** [YOUR_STREAMLIT_APP_LINK](YOUR_STREAMLIT_APP_LINK)

To deploy your own fork:

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add `GEMINI_API_KEY` under **App Settings → Secrets**
5. Click **Deploy** — your app is live in minutes

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> ⚠️ **Never commit your `.env` file to GitHub.** It is already listed in `.gitignore`.
> 
> For Streamlit Cloud deployment, add the key under **App Settings → Secrets** in the dashboard.

---

## 🎯 Use Cases

```
👨‍🎓  Final-year students       →  Internship & campus placement resumes
👩‍💼  Freshers (0–1 yr exp)     →  First job application documents
💻  Developers & coders        →  GitHub portfolio + tech resumes
🏫  College placement cells    →  Bulk resume preparation tool
🎓  Career guidance platforms  →  Resume optimization at scale
📊  Self-assessment            →  ATS scoring + interview prep
```

---

## 🔮 Roadmap

- [x] AI Resume Generator (3 templates)
- [x] ATS Resume Checker
- [x] AI Cover Letter Generator
- [x] AI Portfolio Generator
- [x] Interview Question Generator
- [x] PDF Export for all documents
- [x] Streamlit Cloud Deployment
- [ ] Multi-language Resume Generation
- [ ] LinkedIn Profile Import
- [ ] Portfolio Website Export (HTML)
- [ ] Resume Keyword Optimizer
- [ ] Recruiter Dashboard
- [ ] Resume Version History
- [ ] AI Career Path Recommendations
- [ ] Dark Mode UI

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork this repository
# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Commit your changes
git commit -m "Add: your feature description"

# 4. Push to your fork
git push origin feature/your-feature-name

# 5. Open a Pull Request
```

Please make sure your code follows the existing structure and includes clear comments.

---

## 👨‍💻 Author

<div align="center">

<img src="https://github.com/ashishraj-hub.png" width="100" style="border-radius:50%"/>

### Ashish Raj
**AI & Machine Learning Developer**

[![GitHub](https://img.shields.io/badge/GitHub-ashishraj--hub-181717?style=for-the-badge&logo=github)](https://github.com/ashishraj-hub)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/ashiah-raj-ashishraj)

</div>

---

## ⭐ Support This Project

If this project helped you or you found it interesting:

- 🌟 **Star** this repository — it helps others discover it
- 🍴 **Fork** it to build your own version
- 📢 **Share** it with classmates and batchmates
- 🐛 **Report bugs** or suggest features via [Issues](https://github.com/ashishraj-hub/AI-Resume-Portfolio-Builder/issues)

---

## 📜 License

This project is built for **educational, learning, and portfolio purposes**.
Feel free to use, modify, and build on it with attribution.

---

<div align="center">

**Made with ❤️ by [Ashish Raj](https://github.com/ashishraj-hub)**

*Helping students get hired, one resume at a time.*

<img src="https://komarev.com/ghpvc/?username=ashishraj-hub&label=Profile+Views&color=6C63FF&style=flat" alt="Profile Views"/>

</div>
