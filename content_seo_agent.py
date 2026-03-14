from groq import Groq
import datetime
import pytz

client = Groq(api_key="YOUR_API_KEY_HERE")
history = []

# ================================
# 12 CONTENT & SEO TOOLS
# ================================

# Tool 1 — Blog Title Generator
def blog_title(topic, style):
    titles = {
        "howto": f"How to {topic} — Complete Guide 2025",
        "list": f"Top 10 {topic} Tips You Must Know",
        "question": f"What is {topic}? Everything You Need to Know",
        "power": f"{topic} — The Ultimate Secret Revealed!",
        "number": f"7 Proven Ways to Master {topic}"
    }
    title = titles.get(style.lower(),
        f"Complete Guide to {topic} — 2025")
    words = len(title.split())
    return f"""
✍️ Blog Title Generator:
Topic:          {topic}
Style:          {style}
Title:          {title}
Word Count:     {words} words
SEO Score:      {'Good ✅' if 6 <= words <= 12 else 'Optimize ⚠️'}
Tip:            60 characters se kam rakho!"""

# Tool 2 — SEO Keywords
def seo_keywords(topic, location):
    keywords = [
        f"{topic}",
        f"{topic} in {location}",
        f"best {topic}",
        f"{topic} guide",
        f"how to {topic}",
        f"{topic} tips",
        f"{topic} for beginners",
        f"free {topic}",
        f"{topic} online",
        f"{topic} 2025"
    ]
    return f"""
🔍 SEO Keywords:
Topic:          {topic}
Location:       {location}
Primary:        {keywords[0]}
Secondary:
  → {keywords[1]}
  → {keywords[2]}
  → {keywords[3]}
  → {keywords[4]}
Long Tail:
  → {keywords[5]}
  → {keywords[6]}
  → {keywords[7]}
Tip:            Primary keyword — title mein zarur!"""

# Tool 3 — Meta Description Writer
def meta_description(page_title, keyword):
    meta = f"Discover everything about {page_title}. Learn {keyword} with our complete guide. Get expert tips and tricks now!"
    chars = len(meta)
    return f"""
📝 Meta Description:
Page Title:     {page_title}
Keyword:        {keyword}
Meta:           {meta}
Characters:     {chars}/160
Status:         {'Perfect ✅' if 120 <= chars <= 160 else 'Adjust karo ⚠️'}
Tip:            Keyword first 100 chars mein rakhna!"""

# Tool 4 — Content Readability
def content_readability(word_count, paragraphs, images):
    avg_para = round(word_count / max(paragraphs, 1))
    read_time = round(word_count / 200)
    score = 0
    if 800 <= word_count <= 2000: score += 3
    elif word_count > 2000: score += 2
    else: score += 1
    if avg_para <= 100: score += 3
    else: score += 1
    if images >= 3: score += 3
    elif images >= 1: score += 2
    else: score += 0
    grade = "Excellent ✅" if score >= 8 else "Good ⚠️" if score >= 5 else "Improve ❌"
    return f"""
📖 Content Readability:
Word Count:     {word_count} words
Paragraphs:     {paragraphs}
Images:         {images}
Avg Para Size:  {avg_para} words
Read Time:      {read_time} minutes
SEO Grade:      {grade}
Tip:            1000+ words — best for SEO!"""

# Tool 5 — Social Media Post
def social_media_post(topic, platform):
    posts = {
        "instagram": f"🔥 {topic} ke baare mein yeh jaanna zaroori hai!\n\n✅ Point 1\n✅ Point 2\n✅ Point 3\n\n##{topic.replace(' ','_')} #trending #viral",
        "twitter": f"💡 {topic} — ek important thread!\n\n1/ Yeh bahut important hai...\n\n##{topic.replace(' ','_')}",
        "linkedin": f"Exciting update about {topic}!\n\nAs a professional, I believe {topic} is changing the industry.\n\nKey insights:\n• Point 1\n• Point 2\n• Point 3\n\n##{topic.replace(' ','_')} #professional",
        "facebook": f"📢 {topic} ke baare mein important information!\n\nAaj hum baat karenge {topic} ke baare mein...\n\nShare zarur karo! 🙏"
    }
    post = posts.get(platform.lower(),
        f"Check out this amazing content about {topic}!")
    return f"""
📱 Social Media Post:
Topic:          {topic}
Platform:       {platform}
Post:
{post}
Tip:            Post karte time best time dekho!"""

# Tool 6 — YouTube SEO
def youtube_seo(video_topic):
    title = f"How to {video_topic} — Complete Tutorial 2025"
    tags = [video_topic, f"{video_topic} tutorial",
            f"how to {video_topic}", f"{video_topic} guide",
            "hindi tutorial", "beginners guide"]
    description = f"""Learn everything about {video_topic} in this complete tutorial.

What you'll learn:
✅ Basics of {video_topic}
✅ Advanced tips
✅ Common mistakes

Timestamps:
0:00 - Introduction
2:00 - Main Content
8:00 - Tips & Tricks
10:00 - Summary"""
    return f"""
🎥 YouTube SEO:
Video Topic:    {video_topic}
Title:          {title}
Tags:           {', '.join(tags)}
Description Preview:
{description[:200]}...
Tip:            First 24 ghante mein engagement zaroori!"""

# Tool 7 — Blog Word Count Planner
def blog_planner(blog_type):
    plans = {
        "product review": {
            "words": "1500-2000",
            "sections": ["Introduction", "Features",
                         "Pros/Cons", "Comparison", "Verdict"],
            "images": "5-8"
        },
        "how to": {
            "words": "1000-1500",
            "sections": ["Introduction", "Requirements",
                         "Step by Step", "Tips", "Conclusion"],
            "images": "3-5"
        },
        "listicle": {
            "words": "800-1200",
            "sections": ["Introduction", "List Items",
                         "Details", "Summary"],
            "images": "2-4"
        },
        "guide": {
            "words": "2000-3000",
            "sections": ["Introduction", "Background",
                         "Main Content", "Examples",
                         "FAQ", "Conclusion"],
            "images": "6-10"
        }
    }
    plan = plans.get(blog_type.lower(), plans["how to"])
    return f"""
📋 Blog Planner:
Type:           {blog_type}
Word Count:     {plan['words']} words
Sections:       {' → '.join(plan['sections'])}
Images Needed:  {plan['images']}
Tip:            Har section mein keyword use karo!"""

# Tool 8 — Backlink Strategy
def backlink_strategy(website_type):
    strategies = {
        "blog": ["Guest posting", "Broken link building",
                 "Resource pages", "HARO"],
        "business": ["Local directories", "Chamber of commerce",
                     "Industry associations", "Press releases"],
        "ecommerce": ["Product reviews", "Influencer outreach",
                      "Supplier pages", "Comparison sites"]
    }
    tips = strategies.get(website_type.lower(),
        strategies["blog"])
    return f"""
🔗 Backlink Strategy:
Website Type:   {website_type}
Top Strategies:
  1. {tips[0]}
  2. {tips[1]}
  3. {tips[2]}
  4. {tips[3]}
Free Tools:     Ahrefs Free, Google Search Console
Time:           3-6 mahine mein results!
Goal:           Month mein 10+ quality backlinks!"""

# Tool 9 — Email Subject Line
def email_subject(purpose, audience):
    subjects = {
        "sale": f"🔥 Special Offer for {audience} — Today Only!",
        "newsletter": f"📧 This Week's Top Tips for {audience}",
        "welcome": f"Welcome to our community, {audience}! 🎉",
        "followup": f"Quick question for {audience}...",
        "announcement": f"Big news for {audience}! 📢"
    }
    subject = subjects.get(purpose.lower(),
        f"Important update for {audience}")
    open_rate = "25-35%" if len(subject) < 50 else "15-25%"
    return f"""
📧 Email Subject Line:
Purpose:        {purpose}
Audience:       {audience}
Subject:        {subject}
Length:         {len(subject)} chars
Est. Open Rate: {open_rate}
Tip:            Emoji use karo — 15% zyada opens!"""

# Tool 10 — Content Calendar
def content_calendar(platform, posts_per_week):
    india = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(india)
    days = ["Monday", "Wednesday", "Friday",
            "Tuesday", "Thursday", "Saturday", "Sunday"]
    selected_days = days[:posts_per_week]
    monthly = posts_per_week * 4
    return f"""
📅 Content Calendar:
Platform:       {platform}
Posts/Week:     {posts_per_week}
Best Days:      {', '.join(selected_days)}
Monthly Total:  {monthly} posts
Best Time:      7-9 AM ya 7-9 PM IST
Current Month:  {now.strftime('%B %Y')}
Tip:            Consistency sabse zaroori hai!"""

# Tool 11 — Hashtag Generator
def hashtag_generator(topic, platform):
    base_tags = [f"#{topic.replace(' ','')}", 
                 f"#{topic.replace(' ','')}tips",
                 f"#{topic.replace(' ','')}guide"]
    if platform == "instagram":
        count = 30
        extra = ["#viral", "#trending", "#explore",
                 "#instagood", "#reels", "#india",
                 "#indianblogger", "#contentcreator"]
    elif platform == "twitter":
        count = 3
        extra = ["#trending", "#india"]
    else:
        count = 5
        extra = ["#tips", "#guide", "#india"]
    all_tags = base_tags + extra
    return f"""
# Hashtag Generator:
Topic:          {topic}
Platform:       {platform}
Recommended:    {count} hashtags
Top Tags:       {' '.join(all_tags[:6])}
Tip:            Mix karo — big + small hashtags!"""

# Tool 12 — SEO Audit Checklist
def seo_audit(has_ssl, mobile_friendly,
              page_speed, has_sitemap):
    score = 0
    checks = []
    if has_ssl:
        score += 25
        checks.append("✅ SSL Certificate")
    else:
        checks.append("❌ SSL Certificate missing!")
    if mobile_friendly:
        score += 25
        checks.append("✅ Mobile Friendly")
    else:
        checks.append("❌ Mobile Friendly nahi!")
    if page_speed <= 3:
        score += 25
        checks.append("✅ Page Speed Good")
    else:
        checks.append("⚠️ Page Speed Slow!")
    if has_sitemap:
        score += 25
        checks.append("✅ Sitemap Present")
    else:
        checks.append("❌ Sitemap missing!")
    grade = "Excellent" if score >= 75 else "Average"
    return f"""
🔎 SEO Audit:
{chr(10).join(checks)}
SEO Score:      {score}/100
Grade:          {grade}
Tool:           Google Search Console use karo!"""

# ================================
# AI CONTENT CHATBOT
# ================================
def content_chatbot(sawaal):
    history.append({
        "role": "user",
        "content": f"Content writing aur SEO expert ki tarah simple Hindi mein jawab do: {sawaal}"
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
def content_manager(sawaal):
    s = sawaal.lower()
    print(f"✍️ Sawaal: {sawaal}")
    print("----")

    if "title" in s or "blog title" in s:
        return blog_title("AI Tools", "howto")
    elif "keyword" in s or "seo keyword" in s:
        return seo_keywords("AI Agent", "India")
    elif "meta" in s or "description" in s:
        return meta_description("AI Finance Agent", "AI tools")
    elif "readability" in s or "content check" in s:
        return content_readability(1200, 10, 5)
    elif "social" in s or "post" in s:
        return social_media_post("AI Tools", "instagram")
    elif "youtube" in s or "video" in s:
        return youtube_seo("Python Programming")
    elif "blog plan" in s or "planner" in s:
        return blog_planner("how to")
    elif "backlink" in s or "link" in s:
        return backlink_strategy("blog")
    elif "email" in s or "subject" in s:
        return email_subject("newsletter", "developers")
    elif "calendar" in s or "schedule" in s:
        return content_calendar("Instagram", 3)
    elif "hashtag" in s:
        return hashtag_generator("AI tools", "instagram")
    elif "audit" in s or "seo check" in s:
        return seo_audit(True, True, 2.5, True)
    else:
        return content_chatbot(sawaal)

# ================================
# TEST KARO!
# ================================
print("=" * 45)
print("   ✍️  DEBRIS CONTENT & SEO AGENT ✍️")
print("=" * 45)

tests = [
    "Blog title banao",
    "SEO keywords chahiye",
    "Meta description likho",
    "Social media post banao",
    "YouTube SEO karo",
    "Hashtag generator",
    "SEO audit karo",
]

for sawaal in tests:
    print(content_manager(sawaal))
    print("=" * 45)
