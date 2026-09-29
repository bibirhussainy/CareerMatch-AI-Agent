import streamlit as st
from pypdf import PdfReader
from openai import OpenAI


# -----------------------------
# PAGE SETUP
# -----------------------------

st.set_page_config(
    page_title="AI Job Application Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Job Application Agent")

st.write(
    "Upload your CV and paste a job description. "
    "The AI agent will compare them and help you prepare a tailored application."
)


# -----------------------------
# UPLOAD CV
# -----------------------------

uploaded_cv = st.file_uploader(
    "📄 Upload your CV",
    type=["pdf"]
)


# -----------------------------
# JOB DESCRIPTION
# -----------------------------

job_description = st.text_area(
    "📋 Paste the Job Description",
    height=250,
    placeholder="Paste the full job description here..."
)


# -----------------------------
# READ THE CV
# -----------------------------

cv_text = ""

if uploaded_cv is not None:
    reader = PdfReader(uploaded_cv)

    for page in reader.pages:
        page_text = page.extract_text() or ""
        cv_text += page_text + "\n"

    st.success("CV uploaded and read successfully.")


# -----------------------------
# ANALYZE BUTTON
# -----------------------------

analyze_button = st.button("🚀 Analyze My Application")


# -----------------------------
# AI AGENT
# -----------------------------

if analyze_button:

    if uploaded_cv is None:
        st.warning("Please upload your CV first.")

    elif not job_description.strip():
        st.warning("Please paste a job description first.")

    else:

        try:
            client = OpenAI(
                api_key=st.secrets["OPENAI_API_KEY"]
            )

            with st.spinner("AI agent is analyzing your application..."):

                # STEP 1: Analyze the job
                job_analysis = client.responses.create(
                    model="gpt-5.6-luna",
                    instructions="""
                    You are a job application analysis assistant.

                    Analyze the job description and identify:
                    1. Main responsibilities
                    2. Required skills
                    3. Required experience
                    4. Required education or qualifications
                    5. Important keywords

                    Do not invent information.
                    """,
                    input=job_description
                )

                job_requirements = job_analysis.output_text


                # STEP 2: Compare CV with the job
                comparison = client.responses.create(
                    model="gpt-5.6-luna",
                    instructions="""
                    You are helping a person analyze their own job application.

                    Compare the candidate's CV with the job requirements.

                    Clearly identify:
                    1. Matching skills and experience
                    2. Requirements supported by evidence in the CV
                    3. Important gaps or missing requirements
                    4. Transferable skills that may be relevant

                    Never invent experience, education, skills, or qualifications.
                    Only use evidence that actually appears in the CV.
                    """,
                    input=f"""
                    CV:
                    {cv_text}

                    JOB REQUIREMENTS:
                    {job_requirements}
                    """
                )

                match_analysis = comparison.output_text


                # STEP 3: Create tailored application material
                application = client.responses.create(
                    model="gpt-5.6-luna",
                    instructions="""
                    You are a job application writing assistant.

                    Using only truthful information from the candidate's CV
                    and the job analysis, create:

                    1. A short professional profile tailored to the role
                    2. Five strong CV bullet points
                    3. A short tailored cover letter
                    4. Five likely interview questions
                    5. Practical suggestions for improving the application

                    Never invent qualifications, experience, achievements,
                    employers, dates, or technical skills.
                    """,
                    input=f"""
                    CV:
                    {cv_text}

                    JOB ANALYSIS:
                    {job_requirements}

                    CV AND JOB COMPARISON:
                    {match_analysis}
                    """
                )

                application_material = application.output_text


            # -----------------------------
            # SHOW RESULTS
            # -----------------------------

            st.success("Analysis complete!")

            st.subheader("🎯 Job Requirements")
            st.write(job_requirements)

            st.subheader("🔍 CV vs Job Analysis")
            st.write(match_analysis)

            st.subheader("✍️ Tailored Application")
            st.write(application_material)


        except Exception as error:
            st.error(f"Something went wrong: {error}")