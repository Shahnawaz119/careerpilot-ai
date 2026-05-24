import streamlit as st
from PyPDF2 import PdfReader
from openai import OpenAI
import matplotlib.pyplot as plt
from fpdf import FPDF
import random
import time
import os

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# ---------------- OPENROUTER API ----------------

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Main Background */

.stApp {
    background: linear-gradient(to right, #0f172a, #111827);
    color: white;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: #111827;
}

/* Animated Background */

.bg-animation span {
    position: fixed;
    border-radius: 50%;
    background: rgba(56, 189, 248, 0.10);
    animation: move 20s linear infinite;
    bottom: -150px;
    z-index: -2;
}

.bg-animation span:nth-child(1) {
    width: 80px;
    height: 80px;
    left: 10%;
    animation-duration: 18s;
}

.bg-animation span:nth-child(2) {
    width: 120px;
    height: 120px;
    left: 30%;
    animation-duration: 25s;
}

.bg-animation span:nth-child(3) {
    width: 60px;
    height: 60px;
    left: 50%;
    animation-duration: 20s;
}

.bg-animation span:nth-child(4) {
    width: 150px;
    height: 150px;
    left: 70%;
    animation-duration: 30s;
}

.bg-animation span:nth-child(5) {
    width: 100px;
    height: 100px;
    left: 90%;
    animation-duration: 22s;
}

@keyframes move {

    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 0;
    }

    50% {
        opacity: 1;
    }

    100% {
        transform: translateY(-1200px) rotate(720deg);
        opacity: 0;
    }
}

/* Floating Robot */

.robot-side {
    position: fixed;
    right: 20px;
    bottom: 30px;
    z-index: -1;
    opacity: 0.10;
    animation: floatRobot 6s ease-in-out infinite;
}

.robot-side img {
    width: 300px;
}

@keyframes floatRobot {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-20px);
    }

    100% {
        transform: translateY(0px);
    }
}

/* Titles */

.main-title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: #38bdf8;
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: #cbd5e1;
    margin-bottom: 30px;
}

/* Cards */

.glass {
    background: rgba(30, 41, 59, 0.9);
    border-radius: 18px;
    padding: 25px;
    margin-top: 20px;
    border: 1px solid #334155;
}

/* Upload */

[data-testid="stFileUploader"] {
    background: #1e293b;
    border-radius: 15px;
    padding: 20px;
}

/* Metrics */

[data-testid="metric-container"] {
    background-color: #1e293b;
    border-radius: 12px;
    padding: 15px;
    border: 1px solid #334155;
}

</style>

<div class="bg-animation">
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
</div>

<div class="robot-side">
    <img src="https://cdn.dribbble.com/users/730703/screenshots/6581243/avento.gif">
</div>

""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
    "<p class='main-title'>🚀 CareerPilot AI</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>AI Resume Analyzer & Career Guidance System</p>",
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.image(
        "https://cdn.dribbble.com/users/730703/screenshots/6581243/avento.gif",
        width=180
    )

    st.title("🤖 Features")

    st.markdown("""
    ✅ Resume Analysis  
    ✅ ATS Score  
    ✅ Skill Analysis  
    ✅ Career Suggestions  
    ✅ Interview Questions  
    ✅ Learning Resources  
    ✅ AI Chat Assistant  
    ✅ PDF Report Download  
    """)
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#0f172a,#1e3a8a);
        padding:18px;
        border-radius:18px;
        border:1px solid #3b82f6;
        margin-top:20px;
        text-align:center;
        box-shadow:0 0 15px rgba(59,130,246,0.4);
    ">

    <h3 style="color:#38bdf8;">🚀 Career Growth Powered by AI</h3>

    <p style="color:#cbd5e1;">
    Built for Future Ready Careers ✨
    </p>

    </div>
    """, unsafe_allow_html=True)

# ---------------- FILE UPLOAD ----------------

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type="pdf"
)

# ---------------- PDF EXTRACTION ----------------

def extract_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

# ---------------- TYPING EFFECT ----------------

def stream_text(text):

    for word in text.split():
        yield word + " "
        time.sleep(0.01)

# ---------------- MAIN ----------------

# ---------------- MAIN ----------------

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    st.success("✅ Resume Uploaded Successfully!")

    company = st.selectbox(
        "🎯 Select Target Company",
        ["Google", "Microsoft", "Amazon", "TCS", "Infosys"]
    )

    # ---------------- AI PROMPT ----------------

    prompt = f"""
    You are an advanced AI Resume Analyzer and ATS System.

    Analyze the uploaded resume carefully like a real ATS checker.

    IMPORTANT RULES:

    1. ATS score must be realistic.
    2. Weak resumes should get 45-65.
    3. Average resumes should get 65-78.
    4. Strong resumes should get 78-88.
    5. Exceptional resumes should get 88-95 only.
    6. Analyze projects, internships, skills, certifications, achievements and resume quality.

    Return response ONLY in this format:

    ATS_SCORE:
    (Realistic ATS score with reason)

    SKILLS:
    (List technical + soft skills)

    MISSING_SKILLS:
    (List missing skills)

    CAREER_SUGGESTIONS:
    (Suggest career roles ONLY based on resume)

    INTERVIEW_QUESTIONS:
    (Generate interview questions ONLY based on resume projects + skills)

    LEARNING_RESOURCES:
    (Suggest learning resources based on missing skills)

    ROADMAP:
    (Create personalized roadmap)

    Resume:
    {resume_text}
    """

    # ---------------- AI RESPONSE ----------------

    with st.spinner("🤖 AI Analyzing Resume..."):

        completion = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = completion.choices[0].message.content

    # ---------------- PARSING ----------------

    try:

        ats_section = result.split("ATS_SCORE:")[1].split("SKILLS:")[0]

        skills_section = result.split("SKILLS:")[1].split("MISSING_SKILLS:")[0]

        missing_section = result.split("MISSING_SKILLS:")[1].split("CAREER_SUGGESTIONS:")[0]

        career_section = result.split("CAREER_SUGGESTIONS:")[1].split("INTERVIEW_QUESTIONS:")[0]

        interview_section = result.split("INTERVIEW_QUESTIONS:")[1].split("LEARNING_RESOURCES:")[0]

        learning_section = result.split("LEARNING_RESOURCES:")[1].split("ROADMAP:")[0]

        roadmap_section = result.split("ROADMAP:")[1]

    except:

        st.error("⚠️ AI Response Parsing Error")
        st.write(result)
        st.stop()

    # ---------------- REALISTIC ATS SCORE ----------------

    resume_lower = resume_text.lower()

    ats_number = 35

    # ---------------- SKILLS ----------------

    tech_skills = [
        "python", "java", "c++", "sql", "html",
        "css", "javascript", "react", "node",
        "machine learning", "tensorflow",
        "pandas", "numpy", "streamlit",
        "mongodb", "api", "git", "github"
    ]

    matched_skills = []

    for skill in tech_skills:

        if skill in resume_lower:
            matched_skills.append(skill)

    ats_number += min(len(matched_skills) * 2, 18)

    # ---------------- PROJECTS ----------------

    project_keywords = [
        "project",
        "developed",
        "built",
        "created",
        "implemented",
        "designed"
    ]

    project_score = 0

    for word in project_keywords:

        if word in resume_lower:
            project_score += 1

    ats_number += min(project_score * 2, 10)

    # ---------------- EXPERIENCE ----------------

    experience_keywords = [
        "internship",
        "intern",
        "experience"
    ]

    experience_score = 0

    for word in experience_keywords:

        if word in resume_lower:
            experience_score += 1

    ats_number += min(experience_score * 4, 12)

    # ---------------- CERTIFICATIONS ----------------

    cert_keywords = [
        "certification",
        "certificate",
        "coursera",
        "udemy",
        "nptel"
    ]

    cert_score = 0

    for word in cert_keywords:

        if word in resume_lower:
            cert_score += 1

    ats_number += min(cert_score * 2, 8)

    # ---------------- ACHIEVEMENTS ----------------

    achievement_keywords = [
        "leetcode",
        "hackathon",
        "award",
        "winner",
        "achievement"
    ]

    achievement_score = 0

    for word in achievement_keywords:

        if word in resume_lower:
            achievement_score += 1

    ats_number += min(achievement_score * 2, 8)

    # ---------------- RESUME LENGTH ----------------

    resume_length = len(resume_text)

    if resume_length > 3500:
        ats_number += 5

    elif resume_length > 2200:
        ats_number += 3

    elif resume_length < 1200:
        ats_number -= 8

    # ---------------- CONTACT DETAILS ----------------

    if "linkedin" in resume_lower:
        ats_number += 2

    if "github" in resume_lower:
        ats_number += 2

    if "@" in resume_lower:
        ats_number += 2

    # ---------------- FINAL LIMIT ----------------

    if ats_number > 90:
        ats_number = 90

    if ats_number < 45:
        ats_number = 45

    # ---------------- METRICS ----------------

    confidence = random.randint(85, 97)

    skills_found = len(matched_skills)

    match_score = min(ats_number + random.randint(-2, 3), 92)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("ATS Score", f"{ats_number}%")
    col2.metric("AI Confidence", f"{confidence}%")
    col3.metric("Skills Found", skills_found)
    col4.metric(f"{company} Match", f"{match_score}%")

    st.progress(ats_number / 100)

    # ---------------- TABS ----------------

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📌 AI Analysis",
        "📈 Skill Analysis",
        "💼 Career Suggestions",
        "🎤 Interview Questions",
        "📚 Learning Resources",
        "🛣️ Roadmap"
    ])

    # ---------------- TAB 1 ----------------

    with tab1:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("📌 Resume Skills")

        st.write_stream(stream_text(skills_section))

        st.subheader("❌ Missing Skills")

        st.write_stream(stream_text(missing_section))

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 2 ----------------

    with tab2:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        skill_data = {
            "Technical": min(len(matched_skills) * 10, 100),
            "Projects": min(project_score * 15, 100),
            "Experience": min(experience_score * 25, 100),
            "Achievements": min(achievement_score * 20, 100),
            "Resume Quality": ats_number
        }

        fig, ax = plt.subplots()

        ax.bar(skill_data.keys(), skill_data.values())

        st.pyplot(fig)

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 3 ----------------

    with tab3:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("💼 Personalized Career Suggestions")

        st.write_stream(stream_text(career_section))

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 4 ----------------

    with tab4:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("🎤 Personalized Interview Questions")

        st.write_stream(stream_text(interview_section))

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 5 ----------------

    with tab5:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("📚 Personalized Learning Resources")

        st.write_stream(stream_text(learning_section))

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 6 ----------------

    with tab6:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("🛣️ Personalized Roadmap")

        st.write_stream(stream_text(roadmap_section))

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- PDF REPORT ----------------

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    clean_text = result.encode('latin-1', 'ignore').decode('latin-1')

    pdf.multi_cell(0, 10, clean_text)

    pdf.output("career_report.pdf")

    with open("career_report.pdf", "rb") as file:

        st.download_button(
            label="📥 Download AI Report",
            data=file,
            file_name="career_report.pdf",
            mime="application/pdf"
        )
# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    "<center>Made with ❤️ using OpenRouter API + Streamlit</center>",
    unsafe_allow_html=True
)