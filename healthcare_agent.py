from groq import Groq
import datetime
import pytz

client = Groq(api_key="YOUR_API_KEY_HERE")
history = []

# ================================
# 12 HEALTHCARE TOOLS
# ================================

# Tool 1 — BMI Calculator
def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status = "Underweight — Thoda aur khao!"
    elif bmi < 25:
        status = "Normal — Bilkul fit ho!"
    elif bmi < 30:
        status = "Overweight — Exercise shuru karo!"
    else:
        status = "Obese — Doctor se milo!"
    return f"""
💪 BMI Calculator:
Weight:     {weight} kg
Height:     {height} m
BMI:        {round(bmi, 1)}
Status:     {status}"""

# Tool 2 — Calorie Calculator
def calorie_calculator(weight, height, age, gender):
    if gender == "male":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age)
    return f"""
🔥 Calorie Calculator:
Weight:         {weight} kg
Height:         {height} m
Age:            {age} saal
Daily Calories: {round(bmr)} calories
Active Day:     {round(bmr * 1.5)} calories"""

# Tool 3 — Water Intake
def water_intake(weight):
    water = weight * 0.033
    glasses = round(water / 0.25)
    return f"""
💧 Water Intake Calculator:
Weight:         {weight} kg
Daily Water:    {round(water, 1)} liters
Glasses:        {glasses} glass/din"""

# Tool 4 — Heart Rate
def heart_rate(age):
    max_hr = 220 - age
    min_hr = round(max_hr * 0.5)
    max_exercise = round(max_hr * 0.85)
    return f"""
❤️ Heart Rate Calculator:
Age:            {age} saal
Max Heart Rate: {max_hr} bpm
Exercise Zone:  {min_hr} - {max_exercise} bpm
Rest Zone:      60 - 100 bpm"""

# Tool 5 — Blood Pressure ✅ FIXED!
def blood_pressure(systolic, diastolic):
    if systolic <= 120 and diastolic <= 80:
        status = "Normal ✅ — Bilkul sahi!"
    elif systolic < 130 and diastolic < 80:
        status = "Elevated ⚠️ — Thoda dhyan do!"
    elif systolic < 140 or diastolic < 90:
        status = "High Stage 1 🔴 — Doctor se milo!"
    else:
        status = "High Stage 2 🚨 — Turant doctor!"
    return f"""
🩸 Blood Pressure:
Reading:    {systolic}/{diastolic} mmHg
Status:     {status}"""

# Tool 6 — Sleep Calculator
def sleep_calculator(age):
    if age <= 12:
        needed = "9-12 ghante"
    elif age <= 18:
        needed = "8-10 ghante"
    elif age <= 60:
        needed = "7-9 ghante"
    else:
        needed = "7-8 ghante"
    return f"""
😴 Sleep Calculator:
Age:            {age} saal
Needed Sleep:   {needed}
Best Bedtime:   10 PM - 11 PM
Wake Up:        6 AM - 7 AM"""

# Tool 7 — Exercise Calories
def exercise_calories(weight, minutes, exercise):
    mets = {"walking": 3.5, "running": 8.0,
            "cycling": 6.0, "swimming": 7.0,
            "yoga": 2.5}
    met = mets.get(exercise.lower(), 4.0)
    calories = (met * weight * minutes) / 60
    return f"""
🏃 Exercise Calories:
Exercise:       {exercise}
Weight:         {weight} kg
Time:           {minutes} minutes
Calories Burned: {round(calories)} cal"""

# Tool 8 — Ideal Weight
def ideal_weight(height, gender):
    height_cm = height * 100
    if gender == "male":
        ideal = 50 + 0.91 * (height_cm - 152.4)
    else:
        ideal = 45.5 + 0.91 * (height_cm - 152.4)
    return f"""
🍎 Ideal Weight:
Height:         {height} m
Gender:         {gender}
Ideal Weight:   {round(ideal)} kg
Healthy Range:  {round(ideal-5)} - {round(ideal+5)} kg"""

# Tool 9 — Diabetes Risk
def diabetes_risk(age, bmi, family_history):
    risk = 0
    if age > 45: risk += 2
    if bmi > 25: risk += 2
    if family_history: risk += 3
    if risk <= 2:
        level = "Low Risk ✅"
    elif risk <= 4:
        level = "Medium Risk ⚠️"
    else:
        level = "High Risk 🔴 — Doctor se milo!"
    return f"""
🧬 Diabetes Risk:
Age:            {age} saal
BMI:            {bmi}
Family History: {'Haan' if family_history else 'Nahi'}
Risk Level:     {level}"""

# Tool 10 — Pregnancy Week
def pregnancy_week(lmp_days_ago):
    weeks = lmp_days_ago // 7
    days = lmp_days_ago % 7
    trimester = 1 if weeks < 13 else (2 if weeks < 27 else 3)
    remaining = 40 - weeks
    return f"""
🤰 Pregnancy Calculator:
Current Week:   {weeks} weeks {days} days
Trimester:      {trimester}
Weeks Left:     {remaining} weeks"""

# Tool 11 — Lung Capacity
def lung_capacity(height, age, gender):
    if gender == "male":
        fvc = (0.0576 * height * 100) - (0.0269 * age) - 4.34
    else:
        fvc = (0.0443 * height * 100) - (0.0260 * age) - 2.89
    return f"""
🫁 Lung Capacity:
Height:         {height} m
Age:            {age} saal
Lung Capacity:  {round(fvc, 1)} liters
Status:         {'Normal ✅' if fvc > 3 else 'Low ⚠️'}"""

# Tool 12 — Medicine Reminder
def medicine_reminder(medicine, times):
    india = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(india)
    return f"""
💊 Medicine Reminder:
Medicine:   {medicine}
Times/Day:  {times}
Reminder:   Har {24//times} ghante mein lo
Next Dose:  {now.strftime('%I:%M %p')} ke baad
Note:       Doctor ki salah zarur lo!"""

# ================================
# AI HEALTH CHATBOT
# ================================
def health_chatbot(sawaal):
    history.append({
        "role": "user",
        "content": f"Health expert doctor ki tarah Hindi mein jawab do: {sawaal}"
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
def health_manager(sawaal):
    s = sawaal.lower()
    if "bmi" in s:
        return bmi_calculator(70, 1.70)
    elif "calorie" in s or "calories" in s:
        return calorie_calculator(70, 1.70, 25, "male")
    elif "water" in s or "paani" in s:
        return water_intake(70)
    elif "heart" in s or "dil" in s:
        return heart_rate(25)
    elif "blood pressure" in s or "bp" in s:
        return blood_pressure(120, 80)
    elif "sleep" in s or "neend" in s:
        return sleep_calculator(25)
    elif "exercise" in s or "workout" in s:
        return exercise_calories(70, 30, "walking")
    elif "ideal weight" in s or "weight" in s:
        return ideal_weight(1.70, "male")
    elif "diabetes" in s:
        return diabetes_risk(35, 24, False)
    elif "pregnancy" in s or "pregnant" in s:
        return pregnancy_week(70)
    elif "lung" in s:
        return lung_capacity(1.70, 25, "male")
    elif "medicine" in s or "dawai" in s:
        return medicine_reminder("Paracetamol", 3)
    else:
        return health_chatbot(sawaal)
