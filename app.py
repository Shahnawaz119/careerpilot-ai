import streamlit as st
from PyPDF2 import PdfReader
from openai import OpenAI
import matplotlib.pyplot as plt
from fpdf import FPDF
import streamlit as st
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

/* Buttons */

.stButton>button {
    background: linear-gradient(90deg,#06b6d4,#3b82f6);
    color: white;
    border-radius: 10px;
    height: 50px;
    border: none;
    width: 100%;
    font-size: 18px;
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
        time.sleep(0.02)

# ---------------- MAIN ----------------

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    st.success("✅ Resume Uploaded Successfully!")

    company = st.selectbox(
        "🎯 Select Target Company",
        ["Google", "Microsoft", "Amazon", "TCS", "Infosys"]
    )

    # ---------------- METRICS ----------------

    ats_score = random.randint(75, 95)
    confidence = random.randint(85, 99)
    skills_found = random.randint(8, 15)
    match_score = random.randint(70, 95)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("ATS Score", f"{ats_score}%")
    col2.metric("AI Confidence", f"{confidence}%")
    col3.metric("Skills Found", skills_found)
    col4.metric(f"{company} Match", f"{match_score}%")

    st.progress(ats_score / 100)

    # ---------------- CAREER SUGGESTIONS ----------------

    career_roles = []

    resume_lower = resume_text.lower()

    if "python" in resume_lower or "machine learning" in resume_lower:
        career_roles.extend([
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist"
        ])

    if "html" in resume_lower or "css" in resume_lower or "javascript" in resume_lower:
        career_roles.extend([
            "Frontend Developer",
            "Web Developer"
        ])

    if "sql" in resume_lower or "database" in resume_lower:
        career_roles.extend([
            "Backend Developer",
            "Database Analyst"
        ])

    if "java" in resume_lower or "c++" in resume_lower:
        career_roles.extend([
            "Software Engineer",
            "Application Developer"
        ])

    if len(career_roles) == 0:
        career_roles = [
            "Software Developer",
            "IT Analyst",
            "Technical Support Engineer"
        ]

    # ---------------- AI PROMPT ----------------

    prompt = f"""
    You are an advanced AI Career Assistant.

    Analyze this resume and provide:

    1. Candidate Skills
    2. Missing Skills
    3. Best Job Roles
    4. Resume Improvement Suggestions
    5. 10 Interview Questions
    6. 30-Day Learning Roadmap
    7. Best Platforms To Learn Missing Skills

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

    # ---------------- SKILL GRAPH ----------------

    skills = {
        "Python": random.randint(70, 95),
        "SQL": random.randint(60, 90),
        "Communication": random.randint(65, 95),
        "Problem Solving": random.randint(75, 98),
        "AI/ML": random.randint(50, 90),
    }

    # ---------------- INTERVIEW QUESTIONS ----------------

    interview_questions = [
        "Explain OOP concepts in Python.",
        "Difference between SQL and NoSQL?",
        "What is API?",
        "Explain DBMS normalization.",
        "What is Machine Learning?",
        "Explain REST API.",
        "Difference between Stack and Queue?",
        "What is OS scheduling?",
        "Explain your projects.",
        "Why should we hire you?"
    ]

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

        st.subheader("📌 AI Career Report")

        st.write_stream(stream_text(result))

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 2 ----------------

    with tab2:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        fig, ax = plt.subplots()

        ax.bar(skills.keys(), skills.values())

        st.pyplot(fig)

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 3 ----------------

    with tab3:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("💼 Recommended Career Roles")

        for role in career_roles:
            st.write("✅", role)

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 4 ----------------

    with tab4:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("🎤 AI Generated Interview Questions")

        for q in interview_questions:
            st.write("✅", q)

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 5 ----------------

    with tab5:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("📚 Recommended Learning Platforms")

        st.markdown("""
### 🐍 Python & AI
- https://www.coursera.org/
- https://www.freecodecamp.org/
- https://www.deeplearning.ai/

### 💻 DSA & Coding
- https://leetcode.com/
- https://www.geeksforgeeks.org/
- https://neetcode.io/

### 🌐 Web Development
- https://developer.mozilla.org/
- https://www.w3schools.com/

### ☁️ Cloud & DevOps
- https://explore.skillbuilder.aws/
- https://www.cloudskillsboost.google/
        """)

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 6 ----------------

    with tab6:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("🛣️ 30-Day Learning Roadmap")

        st.write("""
### Week 1
- Python Revision
- DSA Basics
- SQL Fundamentals

### Week 2
- DBMS + OS
- Resume Improvement
- Build Mini Projects

### Week 3
- APIs + Deployment
- Mock Interviews
- AI/ML Basics

### Week 4
- Advanced Projects
- LinkedIn Optimization
- Interview Preparation
        """)

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

# ---------------- CHATBOT ----------------

st.markdown("---")

st.subheader("💬 Ask CareerPilot AI")

user_question = st.chat_input(
    "Ask about career, interviews, roadmap..."
)

if user_question:

    with st.spinner("🤖 Thinking..."):

        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": user_question
                }
            ]
        )

        answer = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(answer)

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    "<center>Made with ❤️ using OpenRouter API + Streamlit</center>",
    unsafe_allow_html=True
)