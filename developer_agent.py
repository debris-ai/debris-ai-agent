from groq import Groq
import datetime
import pytz

client = Groq(api_key="YOUR_API_KEY_HERE")
history = []

# ================================
# 12 DEVELOPER TOOLS
# ================================

# Tool 1 — Code Complexity
def code_complexity(lines, functions, classes):
    complexity = "Simple" if lines < 100 else \
                 "Medium" if lines < 500 else "Complex"
    maintainability = round(100 - (lines/10) - (functions*2), 1)
    maintainability = max(0, min(100, maintainability))
    return f"""
💻 Code Complexity:
Lines of Code:  {lines}
Functions:      {functions}
Classes:        {classes}
Complexity:     {complexity}
Maintainability: {maintainability}/100
Tip:            Functions 20 lines se kam rakho!"""

# Tool 2 — API Response Time
def api_response(response_ms):
    if response_ms < 200:
        status = "Excellent ✅ — Fast!"
    elif response_ms < 500:
        status = "Good ✅ — Acceptable"
    elif response_ms < 1000:
        status = "Average ⚠️ — Optimize karo"
    else:
        status = "Slow ❌ — Turant fix karo!"
    return f"""
⚡ API Response Time:
Response Time:  {response_ms} ms
Status:         {status}
Target:         < 200ms
Tip:            Caching use karo speed ke liye!"""

# Tool 3 — Database Query
def database_query(rows, query_time_ms, has_index):
    efficiency = "Optimized ✅" if has_index else "Needs Index ⚠️"
    rows_per_ms = round(rows / max(query_time_ms, 1))
    return f"""
🗄️ Database Query:
Rows Fetched:   {rows}
Query Time:     {query_time_ms} ms
Has Index:      {'Yes ✅' if has_index else 'No ❌'}
Efficiency:     {efficiency}
Speed:          {rows_per_ms} rows/ms
Tip:            {'Index add karo!' if not has_index else 'Index sahi hai!'}"""

# Tool 4 — Git Commands Guide
def git_guide(action):
    commands = {
        "start": "git init → git add . → git commit -m 'first commit'",
        "save": "git add . → git commit -m 'your message'",
        "upload": "git push origin main",
        "download": "git pull origin main",
        "branch": "git checkout -b new-branch",
        "merge": "git merge branch-name",
        "status": "git status",
        "history": "git log --oneline"
    }
    cmd = commands.get(action.lower(),
        "git --help se commands dekho!")
    return f"""
📁 Git Guide:
Action:         {action}
Command:        {cmd}
Tip:            Har kaam ke baad commit karo!
Learn More:     learngitbranching.js.org"""

# Tool 5 — Bug Tracker
def bug_tracker(bug_type, severity):
    solutions = {
        "syntax": "Code carefully padho — missing bracket ya colon!",
        "logic": "Print statements se debug karo step by step!",
        "runtime": "Try-except use karo aur error message padho!",
        "import": "pip install command check karo!",
        "api": "API key aur endpoint URL verify karo!"
    }
    priorities = {
        "critical": "🔴 Abhi fix karo!",
        "high": "🟠 Aaj fix karo!",
        "medium": "🟡 Is hafte fix karo",
        "low": "🟢 Jab time mile"
    }
    solution = solutions.get(bug_type.lower(),
        "Error message carefully padho!")
    priority = priorities.get(severity.lower(),
        "🟡 Medium priority")
    return f"""
🐛 Bug Tracker:
Bug Type:       {bug_type}
Severity:       {severity}
Priority:       {priority}
Solution:       {solution}
Tool:           print() ya debugger use karo!"""

# Tool 6 — Code Review Checklist
def code_review(has_comments, has_tests,
                follows_naming, has_error_handling):
    score = 0
    checks = []
    if has_comments:
        score += 25
        checks.append("✅ Comments present")
    else:
        checks.append("❌ Comments missing!")
    if has_tests:
        score += 25
        checks.append("✅ Tests written")
    else:
        checks.append("❌ Tests missing!")
    if follows_naming:
        score += 25
        checks.append("✅ Naming convention sahi")
    else:
        checks.append("❌ Naming convention galat!")
    if has_error_handling:
        score += 25
        checks.append("✅ Error handling present")
    else:
        checks.append("❌ Error handling missing!")
    grade = "Excellent ✅" if score >= 75 else \
            "Good ⚠️" if score >= 50 else "Needs Work ❌"
    return f"""
✅ Code Review:
{chr(10).join(checks)}
Score:          {score}/100
Grade:          {grade}
Tip:            Tests likhna professional practice hai!"""

# Tool 7 — Tech Stack Advisor
def tech_stack(project_type):
    stacks = {
        "web": {
            "frontend": "React / HTML+CSS+JS",
            "backend": "Python Flask / Node.js",
            "database": "PostgreSQL / MongoDB",
            "hosting": "Vercel / Render"
        },
        "mobile": {
            "frontend": "React Native / Flutter",
            "backend": "Python FastAPI",
            "database": "Firebase / SQLite",
            "hosting": "Play Store / App Store"
        },
        "ai": {
            "frontend": "Streamlit / Gradio",
            "backend": "Python + Groq/OpenAI",
            "database": "Vector DB / SQLite",
            "hosting": "Streamlit Cloud / HuggingFace"
        },
        "data": {
            "frontend": "Tableau / PowerBI",
            "backend": "Python Pandas",
            "database": "MySQL / BigQuery",
            "hosting": "AWS / Google Cloud"
        }
    }
    stack = stacks.get(project_type.lower(),
        stacks["web"])
    return f"""
🛠️ Tech Stack:
Project Type:   {project_type}
Frontend:       {stack['frontend']}
Backend:        {stack['backend']}
Database:       {stack['database']}
Hosting:        {stack['hosting']}
Tip:            Simple shuru karo — baad mein scale karo!"""

# Tool 8 — Python Package Info
def python_package(package_name):
    packages = {
        "groq": "AI API calls ke liye — pip install groq",
        "streamlit": "Web apps ke liye — pip install streamlit",
        "pandas": "Data analysis ke liye — pip install pandas",
        "numpy": "Math calculations — pip install numpy",
        "requests": "HTTP calls — pip install requests",
        "flask": "Web server — pip install flask",
        "fastapi": "Fast API — pip install fastapi",
        "pytz": "Timezone — pip install pytz",
        "matplotlib": "Graphs — pip install matplotlib",
        "sklearn": "Machine Learning — pip install scikit-learn"
    }
    info = packages.get(package_name.lower(),
        f"pip install {package_name} — PyPI pe check karo!")
    return f"""
📦 Python Package:
Package:        {package_name}
Info:           {info}
Install:        pip install {package_name}
Docs:           pypi.org/project/{package_name}
Tip:            requirements.txt mein add karo!"""

# Tool 9 — Deployment Checklist
def deployment_checklist(platform):
    checklists = {
        "streamlit": [
            "✅ requirements.txt updated",
            "✅ API keys in Secrets",
            "✅ GitHub repo updated",
            "✅ app.py working locally",
            "✅ share.streamlit.io pe deploy"
        ],
        "heroku": [
            "✅ Procfile banao",
            "✅ requirements.txt",
            "✅ runtime.txt",
            "✅ Config vars set karo",
            "✅ git push heroku main"
        ],
        "github": [
            "✅ .gitignore mein .env add",
            "✅ README.md update",
            "✅ No API keys in code",
            "✅ git add . && commit",
            "✅ git push origin main"
        ]
    }
    steps = checklists.get(platform.lower(),
        checklists["github"])
    return f"""
🚀 Deployment Checklist:
Platform:       {platform}
Steps:
{chr(10).join(steps)}
Tip:            Deploy karne se pehle locally test karo!"""

# Tool 10 — Error Code Guide
def error_guide(error_code):
    errors = {
        "404": "Page not found — URL check karo!",
        "500": "Server error — backend code check karo!",
        "401": "Unauthorized — API key check karo!",
        "403": "Forbidden — permissions check karo!",
        "429": "Too many requests — rate limit hit!",
        "200": "Success! ✅ Sab sahi hai!",
        "201": "Created! ✅ Resource ban gaya!",
        "400": "Bad request — input data check karo!"
    }
    solution = errors.get(str(error_code),
        "Documentation mein error code search karo!")
    return f"""
🔴 Error Code Guide:
Error Code:     {error_code}
Meaning:        {solution}
Next Step:      Console logs check karo!
Help:           Stack Overflow pe search karo!"""

# Tool 11 — Code Performance
def code_performance(algorithm, data_size):
    complexities = {
        "linear search": ("O(n)", "Slow for large data"),
        "binary search": ("O(log n)", "Fast — sorted data chahiye"),
        "bubble sort": ("O(n²)", "Very slow — avoid!"),
        "merge sort": ("O(n log n)", "Good for large data"),
        "hash lookup": ("O(1)", "Fastest! — dictionary use karo"),
        "for loop": ("O(n)", "Simple — ok for small data")
    }
    comp = complexities.get(algorithm.lower(),
        ("O(?)", "Algorithm analyze karo"))
    time_est = data_size * 0.001
    return f"""
⚡ Code Performance:
Algorithm:      {algorithm}
Data Size:      {data_size} items
Complexity:     {comp[0]}
Assessment:     {comp[1]}
Est. Time:      {time_est}ms
Tip:            Dictionary use karo O(1) ke liye!"""

# Tool 12 — Learning Path
def learning_path(current_level, goal):
    paths = {
        "beginner_webdev": [
            "1. HTML/CSS basics",
            "2. JavaScript fundamentals",
            "3. Git & GitHub",
            "4. React basics",
            "5. Node.js/Python backend",
            "6. Deploy first project!"
        ],
        "beginner_ai": [
            "1. Python basics",
            "2. Libraries: NumPy, Pandas",
            "3. Machine Learning basics",
            "4. Deep Learning intro",
            "5. API integration (Groq!)",
            "6. Deploy AI app!"
        ],
        "intermediate_ai": [
            "1. Advanced Python",
            "2. LangChain / LlamaIndex",
            "3. Vector databases",
            "4. Fine-tuning models",
            "5. Production deployment",
            "6. Build AI product!"
        ]
    }
    key = f"{current_level}_{goal}"
    path = paths.get(key, paths["beginner_ai"])
    return f"""
🎓 Learning Path:
Level:          {current_level}
Goal:           {goal}
Your Roadmap:
{chr(10).join(path)}
Time:           6-12 mahine dedicated practice
Tip:            Roz 2 ghante practice karo!"""

# ================================
# AI DEVELOPER CHATBOT
# ================================
def developer_chatbot(sawaal):
    history.append({
        "role": "user",
        "content": f"Senior software developer ki tarah simple Hindi mein jawab do: {sawaal}"
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
def developer_manager(sawaal):
    s = sawaal.lower()
    print(f"💻 Sawaal: {sawaal}")
    print("----")

    if "complexity" in s or "code check" in s:
        return code_complexity(150, 10, 3)
    elif "api" in s or "response" in s:
        return api_response(150)
    elif "database" in s or "query" in s:
        return database_query(1000, 50, True)
    elif "git" in s:
        return git_guide("save")
    elif "bug" in s or "error fix" in s:
        return bug_tracker("syntax", "high")
    elif "review" in s or "code review" in s:
        return code_review(True, False, True, True)
    elif "tech stack" in s or "technology" in s:
        return tech_stack("ai")
    elif "package" in s or "library" in s:
        return python_package("groq")
    elif "deploy" in s or "deployment" in s:
        return deployment_checklist("streamlit")
    elif "error" in s or "http" in s:
        return error_guide(404)
    elif "performance" in s or "speed" in s:
        return code_performance("hash lookup", 10000)
    elif "learn" in s or "roadmap" in s:
        return learning_path("beginner", "ai")
    else:
        return developer_chatbot(sawaal)

# ================================
# TEST KARO!
# ================================
print("=" * 45)
print("   💻 DEBRIS DEVELOPER AGENT 💻")
print("=" * 45)

tests = [
    "Code complexity check karo",
    "API response time",
    "Git commands batao",
    "Bug fix karna hai",
    "Tech stack suggest karo",
    "Streamlit deploy karna hai",
    "Learning roadmap chahiye",
]

for sawaal in tests:
    print(developer_manager(sawaal))
    print("=" * 45)
