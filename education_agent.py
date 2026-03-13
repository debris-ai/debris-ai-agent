from groq import Groq
import datetime
import pytz

client = Groq(api_key="YOUR_API_KEY_HERE")
history = []

# ================================
# 12 EDUCATION TOOLS
# ================================

# Tool 1 — GPA Calculator
def gpa_calculator(marks_list):
    avg = sum(marks_list) / len(marks_list)
    if avg >= 90:
        grade = "A+ — Outstanding!"
    elif avg >= 80:
        grade = "A — Excellent!"
    elif avg >= 70:
        grade = "B — Good!"
    elif avg >= 60:
        grade = "C — Average"
    elif avg >= 50:
        grade = "D — Pass"
    else:
        grade = "F — Fail"
    gpa = round(avg / 10, 2)
    return f"""
📊 GPA Calculator:
Marks:          {marks_list}
Average:        {round(avg, 1)}%
Grade:          {grade}
GPA (10 point): {gpa}"""

# Tool 2 — Study Time Planner
def study_planner(subjects, hours_per_day):
    per_subject = round(hours_per_day / subjects, 1)
    weekly = hours_per_day * 7
    monthly = hours_per_day * 30
    return f"""
📚 Study Time Planner:
Subjects:       {subjects}
Daily Hours:    {hours_per_day} ghante
Per Subject:    {per_subject} ghante/din
Weekly Total:   {weekly} ghante
Monthly Total:  {monthly} ghante
Tip:            Pomodoro try karo — 25 min study, 5 min break!"""

# Tool 3 — Exam Preparation
def exam_prep(days_left, topics):
    topics_per_day = round(topics / days_left, 1)
    return f"""
✏️ Exam Preparation:
Days Left:      {days_left} din
Total Topics:   {topics}
Topics/Day:     {topics_per_day}
Revision Days:  Last 3 din revision ke liye rakho
Tip:            Subah padhna sabse acha hai!"""

# Tool 4 — Scholarship Finder
def scholarship_finder(income, marks, category):
    scholarships = []
    if income <= 250000:
        scholarships.append("✅ NSP — National Scholarship Portal")
    if marks >= 75:
        scholarships.append("✅ Merit Scholarship — State Board")
    if category in ["sc", "st"]:
        scholarships.append("✅ SC/ST Pre/Post Matric Scholarship")
    if category == "obc":
        scholarships.append("✅ OBC Scholarship — NSP")
    if income <= 600000:
        scholarships.append("✅ Central Sector Scholarship")
    if not scholarships:
        scholarships.append("⚠️ scholarships.gov.in pe check karo")
    return f"""
🎓 Scholarship Finder:
Income:         ₹{income}
Marks:          {marks}%
Category:       {category.upper()}
Available:
""" + "\n".join(scholarships)

# Tool 5 — Fee Calculator
def fee_calculator(tuition, hostel, books, other):
    total = tuition + hostel + books + other
    monthly = round(total / 12)
    return f"""
💰 Education Fee:
Tuition Fee:    ₹{tuition}
Hostel:         ₹{hostel}
Books:          ₹{books}
Other:          ₹{other}
Total/Year:     ₹{total}
Monthly:        ₹{monthly}
Loan Needed:    {'Haan ⚠️' if total > 100000 else 'Nahi ✅'}"""

# Tool 6 — Career Guide
def career_guide(interest):
    careers = {
        "science": "Doctor, Engineer, Scientist, Researcher — NEET/JEE taiyaar karo!",
        "commerce": "CA, CS, MBA, Banking — CPT/Foundation se shuru karo!",
        "arts": "IAS, Lawyer, Journalist, Teacher — UPSC/Graduation pe focus karo!",
        "computer": "Software Engineer, AI Developer, Data Scientist — Coding seekho!",
        "sports": "Cricketer, Athlete, Coach — SAI academy join karo!",
        "fashion": "Fashion Designer, Stylist — NIFT entrance exam do!"
    }
    guide = careers.get(interest.lower(),
        "Apne passion ko career banao! Counselor se milo.")
    return f"""
🎯 Career Guide:
Interest:       {interest}
Career Path:    {guide}
Helpline:       Career Counseling: 1800-111-416"""

# Tool 7 — Entrance Exam Info
def entrance_exam(exam):
    exams = {
        "jee": ("JEE Main/Advanced", "April/May", "PCM 75% zaroori", "NTA website"),
        "neet": ("NEET UG", "May", "PCB 50% zaroori", "neet.nta.nic.in"),
        "upsc": ("UPSC Civil Services", "June", "Graduation zaroori", "upsc.gov.in"),
        "cat": ("CAT", "November", "Graduation 50%", "iimcat.ac.in"),
        "clat": ("CLAT Law", "May", "12th 45%", "consortiumofnlus.ac.in"),
        "nda": ("NDA", "April/September", "12th PCM", "upsc.gov.in")
    }
    e = exams.get(exam.lower(),
        ("Unknown Exam", "N/A", "Check official site", "google.com"))
    return f"""
📝 Entrance Exam:
Exam:           {e[0]}
Month:          {e[1]}
Eligibility:    {e[2]}
Website:        {e[3]}
Tip:            2 saal pehle taiyaari shuru karo!"""

# Tool 8 — Assignment Deadline
def assignment_deadline(subject, days_left, pages):
    pages_per_day = round(pages / max(days_left, 1))
    india = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(india)
    deadline = now + datetime.timedelta(days=days_left)
    return f"""
📋 Assignment Tracker:
Subject:        {subject}
Days Left:      {days_left} din
Total Pages:    {pages}
Pages/Day:      {pages_per_day}
Deadline:       {deadline.strftime('%d %B %Y')}
Status:         {'Urgent! 🔴' if days_left <= 3 else 'On Track ✅'}"""

# Tool 9 — Learning Style
def learning_style(style):
    styles = {
        "visual": "📊 Visual Learner — Diagrams, Charts, Mind Maps use karo!",
        "audio": "🎧 Audio Learner — Lectures suno, khud bold awaaz mein padho!",
        "reading": "📖 Reading Learner — Notes likho, books padho, summaries banao!",
        "kinesthetic": "🤸 Kinesthetic — Experiments karo, practice problems solve karo!"
    }
    tip = styles.get(style.lower(), "Mixed learning style — sab try karo!")
    return f"""
🧠 Learning Style:
Style:          {style}
Best Method:    {tip}
Study App:      Khan Academy, YouTube, Coursera
Tip:            Apni style ke according padho — zyada yaad rahega!"""

# Tool 10 — Student Loan
def student_loan(course_fee, duration_years):
    loan = course_fee
    interest = loan * 0.085 * duration_years
    total = loan + interest
    emi = round(total / (duration_years * 12))
    return f"""
🏦 Student Loan:
Course Fee:     ₹{course_fee}
Duration:       {duration_years} saal
Interest (8.5%): ₹{round(interest)}
Total Amount:   ₹{round(total)}
Monthly EMI:    ₹{emi}
Moratorium:     Course + 1 saal baad EMI shuru
Note:           Bank se best rate compare karo!"""

# Tool 11 — Typing Speed
def typing_speed(words_typed, minutes):
    wpm = round(words_typed / minutes)
    if wpm < 20:
        level = "Beginner — Practice karo!"
    elif wpm < 40:
        level = "Average — Acha hai!"
    elif wpm < 60:
        level = "Good — Keep it up!"
    else:
        level = "Expert — Zabardast!"
    return f"""
⌨️ Typing Speed:
Words Typed:    {words_typed}
Time:           {minutes} minutes
Speed:          {wpm} WPM
Level:          {level}
Practice:       typing.com ya 10fastfingers.com"""

# Tool 12 — Online Course Finder
def course_finder(topic, budget):
    if budget == 0:
        courses = f"FREE courses on: Khan Academy, Coursera (audit), YouTube, NPTEL"
    elif budget <= 1000:
        courses = f"Udemy (sale mein ₹399-699), Coursera, edX"
    else:
        courses = f"Coursera Certificate, Google Career Certificates, Simplilearn"
    return f"""
💻 Online Course:
Topic:          {topic}
Budget:         ₹{budget}
Best Platforms: {courses}
Tip:            Udemy pe sale hoti hai — wait karo!
Certificate:    LinkedIn pe add karo!"""

# ================================
# AI EDUCATION CHATBOT
# ================================
def education_chatbot(sawaal):
    history.append({
        "role": "user",
        "content": f"Education expert teacher ki tarah simple Hindi mein jawab do: {sawaal}"
    })
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history
    )
    jawab = response.choices[0].message.content
    history.append({
        "role": "assistant",
        "content": jawab
    })
    return jawab

# ================================
# MANAGER AGENT
# ================================
def education_manager(sawaal):
    s = sawaal.lower()
    print(f"🎓 Sawaal: {sawaal}")
    print("----")

    if "gpa" in s or "marks" in s or "grade" in s:
        return gpa_calculator([85, 90, 78, 92, 88])
    elif "study" in s or "time table" in s:
        return study_planner(6, 8)
    elif "exam" in s and "prep" in s:
        return exam_prep(30, 20)
    elif "scholarship" in s or "scholarship" in s:
        return scholarship_finder(300000, 80, "general")
    elif "fee" in s or "fees" in s:
        return fee_calculator(80000, 60000, 10000, 5000)
    elif "career" in s:
        return career_guide("computer")
    elif "entrance" in s or "jee" in s or "neet" in s:
        return entrance_exam("jee")
    elif "assignment" in s:
        return assignment_deadline("Math", 5, 20)
    elif "learning" in s or "style" in s:
        return learning_style("visual")
    elif "loan" in s:
        return student_loan(500000, 4)
    elif "typing" in s:
        return typing_speed(200, 5)
    elif "course" in s or "online" in s:
        return course_finder("Python", 0)
    else:
        return education_chatbot(sawaal)

# ================================
# TEST KARO!
# ================================
print("=" * 45)
print("   🎓 DEBRIS EDUCATION AGENT 🎓")
print("=" * 45)

tests = [
    "Mera GPA kya hai?",
    "Study time table banao",
    "Scholarship kaise milegi?",
    "Career guide chahiye",
    "JEE exam kab hai?",
    "Online course chahiye",
    "Student loan kitna hoga?",
]

for sawaal in tests:
    print(education_manager(sawaal))
    print("=" * 45)
