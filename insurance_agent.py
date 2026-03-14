from groq import Groq
import datetime
import pytz

client = Groq(api_key="YOUR_API_KEY_HERE")
history = []

# ================================
# 12 INSURANCE TOOLS
# ================================

# Tool 1 — Life Insurance Calculator
def life_insurance(age, income, dependents):
    coverage = income * 10
    if age < 30:
        premium = coverage * 0.003
    elif age < 45:
        premium = coverage * 0.005
    else:
        premium = coverage * 0.008
    premium_monthly = round(premium / 12)
    return f"""
🛡️ Life Insurance:
Age:            {age} saal
Annual Income:  ₹{income}
Dependents:     {dependents}
Recommended:    ₹{coverage} coverage
Annual Premium: ₹{round(premium)}
Monthly:        ₹{premium_monthly}
Tip:            Term insurance — sabse sasta!"""

# Tool 2 — Health Insurance
def health_insurance(age, family_size, city_type):
    base = 10000
    if age > 45: base += 5000
    if family_size > 2: base += 3000 * (family_size - 2)
    if city_type == "metro": base += 5000
    return f"""
🏥 Health Insurance:
Age:            {age} saal
Family Size:    {family_size} members
City:           {city_type}
Annual Premium: ₹{base}
Monthly:        ₹{round(base/12)}
Coverage:       ₹5,00,000 minimum
Tip:            Ayushman Bharat FREE check karo!"""

# Tool 3 — Car Insurance
def car_insurance(car_value, car_age, claim_history):
    idv = car_value * (1 - 0.05 * car_age)
    premium = idv * 0.02
    if claim_history > 0:
        premium *= 1.25
    ncb = 0 if claim_history > 0 else 20
    return f"""
🚗 Car Insurance:
Car Value:      ₹{car_value}
Car Age:        {car_age} saal
IDV:            ₹{round(idv)}
Annual Premium: ₹{round(premium)}
Monthly:        ₹{round(premium/12)}
NCB Discount:   {ncb}%
Tip:            Claim mat karo NCB bachao!"""

# Tool 4 — Term Insurance
def term_insurance(age, coverage, years):
    if age < 30:
        rate = 0.0008
    elif age < 40:
        rate = 0.0012
    elif age < 50:
        rate = 0.002
    else:
        rate = 0.004
    annual = coverage * rate * years / years
    monthly = round(annual / 12)
    return f"""
📋 Term Insurance:
Age:            {age} saal
Coverage:       ₹{coverage}
Duration:       {years} saal
Annual Premium: ₹{round(annual)}
Monthly:        ₹{monthly}
Death Benefit:  ₹{coverage} (tax free!)
Tip:            Jitna jaldi lo — utna sasta!"""

# Tool 5 — Home Insurance
def home_insurance(property_value, property_type):
    rates = {
        "apartment": 0.001,
        "house": 0.0015,
        "villa": 0.002
    }
    rate = rates.get(property_type.lower(), 0.0015)
    annual = property_value * rate
    return f"""
🏠 Home Insurance:
Property Value: ₹{property_value}
Property Type:  {property_type}
Annual Premium: ₹{round(annual)}
Monthly:        ₹{round(annual/12)}
Covers:         Fire, Theft, Natural Disaster
Tip:            Home loan ke saath zarur lo!"""

# Tool 6 — Travel Insurance
def travel_insurance(destination, days, travelers):
    base_per_day = 50
    if destination == "international":
        base_per_day = 200
    total = base_per_day * days * travelers
    return f"""
✈️ Travel Insurance:
Destination:    {destination}
Duration:       {days} days
Travelers:      {travelers}
Total Premium:  ₹{total}
Per Person:     ₹{round(total/travelers)}
Covers:         Medical, Cancellation, Loss
Tip:            International travel pe zaruri!"""

# Tool 7 — Insurance Claim Guide
def claim_guide(insurance_type):
    guides = {
        "health": [
            "1. Hospital se cashless form lo",
            "2. Insurance company ko call karo",
            "3. Bills aur reports collect karo",
            "4. Claim form bharo",
            "5. 30 din mein settlement"
        ],
        "car": [
            "1. Police FIR file karo",
            "2. Insurance company ko inform karo",
            "3. Surveyor ka wait karo",
            "4. Repair estimate lo",
            "5. Claim form submit karo"
        ],
        "life": [
            "1. Death certificate lo",
            "2. Policy documents collect karo",
            "3. Nominee claim form bhare",
            "4. Bank details do",
            "5. 30-60 din mein payment"
        ],
        "home": [
            "1. Police complaint karo",
            "2. Photos lo damage ke",
            "3. Insurance company call karo",
            "4. Surveyor inspection",
            "5. Repair bills submit karo"
        ]
    }
    steps = guides.get(insurance_type.lower(),
        guides["health"])
    return f"""
📝 Claim Guide:
Insurance:      {insurance_type}
Steps:
{chr(10).join(steps)}
Helpline:       IRDAI: 155255
Tip:            Sab documents safe rakho!"""

# Tool 8 — Premium Calculator
def premium_calculator(insurance_type,
                       coverage_amount, age):
    rates = {
        "life": 0.005,
        "health": 0.02,
        "car": 0.025,
        "home": 0.001,
        "term": 0.001
    }
    base_rate = rates.get(insurance_type.lower(), 0.01)
    if age > 45:
        base_rate *= 1.5
    annual = coverage_amount * base_rate
    return f"""
💰 Premium Calculator:
Insurance Type: {insurance_type}
Coverage:       ₹{coverage_amount}
Your Age:       {age} saal
Annual Premium: ₹{round(annual)}
Monthly:        ₹{round(annual/12)}
Quarterly:      ₹{round(annual/4)}
Tip:            Annual pay karo — discount milta hai!"""

# Tool 9 — Insurance Comparison
def insurance_comparison(insurance_type):
    comparisons = {
        "term": {
            "LIC": "₹12,000/year — Most trusted",
            "HDFC Life": "₹10,000/year — Good service",
            "Max Life": "₹9,500/year — Best claim ratio",
            "ICICI Prudential": "₹10,500/year — Fast claims"
        },
        "health": {
            "Star Health": "₹8,000/year — Best network",
            "HDFC ERGO": "₹7,500/year — Good coverage",
            "Niva Bupa": "₹8,500/year — Day 1 coverage",
            "Aditya Birla": "₹9,000/year — Premium service"
        },
        "car": {
            "ICICI Lombard": "₹6,000/year — Fast claims",
            "Bajaj Allianz": "₹5,500/year — Wide network",
            "HDFC ERGO": "₹5,800/year — Good service",
            "New India": "₹5,200/year — Government backed"
        }
    }
    comp = comparisons.get(insurance_type.lower(),
        comparisons["health"])
    result = "\n".join([f"  {k}: {v}"
                        for k, v in comp.items()])
    return f"""
🔄 Insurance Comparison:
Type:           {insurance_type}
Top Options:
{result}
Tip:            Claim settlement ratio zarur dekho!
Website:        policybazaar.com pe compare karo!"""

# Tool 10 — IRDAI Complaint Guide
def irdai_complaint(complaint_type):
    return f"""
⚖️ IRDAI Complaint:
Complaint:      {complaint_type}
Step 1:         Company grievance cell mein complain
Step 2:         15 din mein response nahi → IRDAI
Step 3:         IRDAI Bima Bharosa portal
Step 4:         Ombudsman approach karo
IRDAI Helpline: 155255 (FREE)
Portal:         bimabharosa.irdai.gov.in
Email:          complaints@irdai.gov.in
Tip:            Policy number ready rakho!"""

# Tool 11 — Maturity Calculator
def maturity_calculator(policy_type,
                        annual_premium, years):
    if policy_type == "endowment":
        maturity = annual_premium * years * 2.5
    elif policy_type == "ulip":
        maturity = annual_premium * years * 3.5
    elif policy_type == "money_back":
        maturity = annual_premium * years * 2.0
    else:
        maturity = annual_premium * years * 2.0
    total_paid = annual_premium * years
    profit = maturity - total_paid
    return f"""
💎 Maturity Calculator:
Policy Type:    {policy_type}
Annual Premium: ₹{annual_premium}
Duration:       {years} saal
Total Paid:     ₹{total_paid}
Maturity Value: ₹{round(maturity)}
Profit:         ₹{round(profit)}
Tip:            Pure term + mutual fund better hai!"""

# Tool 12 — Tax Benefit Calculator
def insurance_tax_benefit(life_premium,
                           health_premium, age):
    life_deduction = min(life_premium, 150000)
    if age >= 60:
        health_deduction = min(health_premium, 50000)
    else:
        health_deduction = min(health_premium, 25000)
    total = life_deduction + health_deduction
    tax_saved = total * 0.30
    return f"""
💸 Tax Benefit:
Life Premium:   ₹{life_premium}
Health Premium: ₹{health_premium}
80C Deduction:  ₹{life_deduction}
80D Deduction:  ₹{health_deduction}
Total Saving:   ₹{total}
Tax Saved:      ₹{round(tax_saved)}
Tip:            Senior citizens ko zyada benefit!"""

# ================================
# AI INSURANCE CHATBOT
# ================================
def insurance_chatbot(sawaal):
    history.append({
        "role": "user",
        "content": f"Insurance expert ki tarah simple Hindi mein jawab do: {sawaal}"
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
def insurance_manager(sawaal):
    s = sawaal.lower()
    print(f"🛡️ Sawaal: {sawaal}")
    print("----")

    if "life" in s or "jeevan" in s:
        return life_insurance(30, 600000, 2)
    elif "health" in s or "medical" in s:
        return health_insurance(35, 4, "metro")
    elif "car" in s or "vehicle" in s:
        return car_insurance(800000, 3, 0)
    elif "term" in s:
        return term_insurance(30, 10000000, 30)
    elif "home" in s or "ghar" in s:
        return home_insurance(5000000, "apartment")
    elif "travel" in s or "trip" in s:
        return travel_insurance("international", 10, 2)
    elif "claim" in s:
        return claim_guide("health")
    elif "premium" in s:
        return premium_calculator("health", 500000, 35)
    elif "compare" in s:
        return insurance_comparison("term")
    elif "irdai" in s or "complaint" in s:
        return irdai_complaint("Claim rejection")
    elif "maturity" in s:
        return maturity_calculator("endowment", 50000, 20)
    elif "tax" in s:
        return insurance_tax_benefit(50000, 25000, 35)
    else:
        return insurance_chatbot(sawaal)

# ================================
# TEST KARO!
# ================================
print("=" * 45)
print("   🛡️  DEBRIS INSURANCE AGENT 🛡️")
print("=" * 45)

tests = [
    "Life insurance kitni leni chahiye?",
    "Health insurance kya le?",
    "Car insurance calculate karo",
    "Term insurance batao",
    "Travel insurance chahiye",
    "Insurance claim kaise kare?",
    "Insurance compare karo",
    "Tax benefit kitna milega?",
]

for sawaal in tests:
    print(insurance_manager(sawaal))
    print("=" * 45)
