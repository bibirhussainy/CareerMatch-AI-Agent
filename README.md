# 🤖 CareerMatch AI Agent

CareerMatch AI is an AI-powered job application assistant that analyzes a candidate's CV against a job description and generates tailored application material.

Instead of simply answering questions, the application uses a multi-step AI workflow to understand the job requirements, compare them with evidence from the CV, identify relevant strengths and gaps, and prepare application content.

## 🚀 Features

- 📄 Upload a CV in PDF format
- 📋 Paste a full job description
- 🎯 Extract and understand key job requirements
- 🔍 Compare the CV with the role requirements
- ✅ Identify relevant skills and experience
- ⚠️ Highlight potential gaps without inventing experience
- ✍️ Generate tailored application material
- 💼 Produce CV improvement suggestions
- 🗣️ Generate interview preparation questions

## 🧠 How It Works

```text
CV PDF + Job Description
          ↓
     CV Text Extraction
          ↓
   Job Requirement Analysis
          ↓
    CV-to-Job Comparison
          ↓
 Tailored Application Generation
          ↓
      Streamlit Results
```

The application separates the task into multiple AI stages rather than using a single prompt.

### Stage 1 — Job Analysis

The AI analyzes the job description and identifies the important responsibilities, skills, qualifications, and requirements.

### Stage 2 — CV Analysis

The agent compares those requirements with information actually found in the uploaded CV. It identifies supporting experience as well as areas where evidence is missing.

### Stage 3 — Application Generation

Using the previous analysis, the agent generates tailored application material while being instructed not to invent qualifications or experience.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| OpenAI API | AI analysis and text generation |
| PyPDF | PDF CV text extraction |
| Git & GitHub | Version control and project hosting |

## 🔐 Security

The OpenAI API key is stored locally using Streamlit Secrets:

```text
.streamlit/secrets.toml
```

This file is excluded from Git using `.gitignore`, so API credentials are not committed to the public repository.

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/bibirhussainy/CareerMatch-AI-Agent.git
cd CareerMatch-AI-Agent
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create:

```text
.streamlit/secrets.toml
```

and add your OpenAI API key:

```toml
OPENAI_API_KEY = "your-api-key"
```

Run the application:

```bash
streamlit run app.py
```

## 🎯 Project Goal

This project was built as an AI engineering portfolio project to demonstrate:

- LLM API integration
- Multi-step AI workflows
- Prompt engineering
- PDF document processing
- Evidence-grounded CV analysis
- Streamlit application development
- Secure API-key management
- Git/GitHub version control
- Deployment-ready application development

## ⚠️ Current Limitations

- CV uploads currently support PDF files.
- Output quality depends on the information available in the CV and job description.
- AI-generated application material should be reviewed by the user before submission.
- The application does not make hiring decisions.

## 🔮 Future Improvements

- Support DOCX CV files
- Structured JSON outputs
- Export tailored application material
- Improved error handling
- Additional interview-preparation tools
- Application history and comparison features

## 🌐 Live Demo

🚀 [Try CareerMatch AI Agent](https://careermatch-ai-agent-aa4r3tbdrdygbz6sabyf4m.streamlit.app/)

## 🎥 Demo Video

A short project demonstration will be added here.

## 👩‍💻 Author

**Bibi Ruqaya Hussainy**

AI engineering portfolio project focused on practical LLM application development.

---

Built to demonstrate an end-to-end AI workflow from document processing and reasoning to application generation and deployment.
