from groq import Groq
import datetime
import pytz

client = Groq(api_key="YOUR_API_KEY_HERE")
history = []

# ================================
# 12 LEGAL TOOLS
# ================================

# Tool 1 — Contract Checker
def contract_checker(contract_type, amount):
    if amount > 1000000:
        stamp_duty = "High Stamp Duty Required ⚠️"
        registration = "Registration Zaruri ✅"
    else:
        stamp_duty = "Normal Stamp Duty"
        registration = "Optional"
    return f"""
📜 Contract Checker:
Contract Type:  {contract_type}
Amount:         ₹{amount}
Stamp Duty:     {stamp_duty}
Registration:   {registration}
Legal Advice:   Vakeel se zarur milo!"""

# Tool 2 — Business Registration
def business_registration(business_type):
    info = {
        "sole": {
            "name": "Sole Proprietorship",
            "cost": "₹0 - ₹500",
            "time": "1-3 din",
            "docs": "Aadhar, PAN, Address Proof"
        },
        "partnership": {
            "name": "Partnership Firm",
            "cost": "₹1000 - ₹3000",
            "time": "3-7 din",
            "docs": "Partnership Deed, PAN, Aadhar"
        },
        "pvt": {
            "name": "Private Limited Company",
            "cost": "₹6000 - ₹15000",
            "time": "7-15 din",
            "docs": "DIN, DSC, MOA, AOA"
        }
    }
    b = info.get(business_type.lower(), info["sole"])
    return f"""
🏢 Business Registration:
Type:           {b['name']}
Cost:           {b['cost']}
Time:           {b['time']}
Documents:      {b['docs']}
Note:           CA/CS se madad lo!"""

# Tool 3 — Labour Law Guide
def labour_law(employees):
    laws = []
    if employees >= 1:
        laws.append("✅ Minimum Wages Act lagu hoga")
    if employees >= 10:
        laws.append("✅ Factories Act lagu hoga")
    if employees >= 20:
        laws.append("✅ EPF (PF) dena hoga — 12%")
    if employees >= 10:
        laws.append("✅ ESIC dena hoga — 3.25%")
    if employees >= 100:
        laws.append("✅ Standing Orders Act")
    laws_str = "\n".join(laws)
    return f"""
💼 Labour Law Guide:
Employees:      {employees} log
Applicable Laws:
{laws_str}
Note:           Labour consultant lo!"""

# Tool 4 — Property Law
def property_law(property_type, value):
    stamp = value * 0.05
    registration = value * 0.01
    total = stamp + registration
    return f"""
🏠 Property Law:
Property Type:  {property_type}
Property Value: ₹{value}
Stamp Duty (5%): ₹{round(stamp)}
Registration (1%): ₹{round(registration)}
Total Cost:     ₹{round(total)}
Note:           Sub-Registrar office mein register karo!"""

# Tool 5 — Family Law Guide
def family_law(matter):
    guides = {
        "divorce": "Family Court mein petition file karo. Mutual consent: 6 months. Contested: 1-3 saal.",
        "marriage": "Marriage Certificate ke liye SDM office jaao. Documents: Aadhar, Photos, Witnesses.",
        "property": "Succession Certificate ya Will ke liye Civil Court mein apply karo.",
        "custody": "Family Court mein child custody ke liye apply karo. Child ka hित sabse zaroori."
    }
    guide = guides.get(matter.lower(), "Family Law vakeel se milo — free legal aid bhi milti hai!")
    return f"""
👨‍👩‍👧 Family Law Guide:
Matter:         {matter}
Guide:          {guide}
Helpline:       National Legal Aid: 15100"""

# Tool 6 — Traffic Violation
def traffic_violation(violation):
    fines = {
        "no helmet": ("No Helmet", "₹1000", "3 mahine"),
        "drunk driving": ("Drunk Driving", "₹10000", "6 mahine jail"),
        "red light": ("Red Light Jump", "₹5000", "Warning"),
        "speeding": ("Overspeeding", "₹2000", "₹4000 second time"),
        "no seatbelt": ("No Seatbelt", "₹1000", "Warning"),
        "mobile": ("Mobile While Driving", "₹5000", "License suspend")
    }
    v = fines.get(violation.lower(),
        ("Unknown Violation", "₹500+", "Varies"))
    return f"""
🚗 Traffic Violation:
Violation:      {v[0]}
Fine:           {v[1]}
Penalty:        {v[2]}
Note:           RTO se confirm karo!"""

# Tool 7 — Legal Fee Estimator
def legal_fee(case_type, complexity):
    base_fees = {
        "civil": 10000,
        "criminal": 15000,
        "property": 12000,
        "family": 8000,
        "consumer": 5000,
        "labour": 7000
    }
    multiplier = {"simple": 1, "medium": 2, "complex": 3}
    base = base_fees.get(case_type.lower(), 10000)
    mult = multiplier.get(complexity.lower(), 1)
    fee = base * mult
    return f"""
💰 Legal Fee Estimator:
Case Type:      {case_type}
Complexity:     {complexity}
Estimated Fee:  ₹{fee} - ₹{fee*2}
Note:           Pehle free consultation lo!
Free Legal Aid: ₹3 lakh se kam income pe"""

# Tool 8 — RTI Guide
def rti_guide(department):
    return f"""
📋 RTI Guide:
Department:     {department}
Application Fee: ₹10 (Postal Order/DD)
Time Limit:     30 din mein jawab milega
How to Apply:
  1. rtionline.gov.in pe jaao
  2. Department select karo
  3. Application likho
  4. ₹10 fee bharo
  5. Submit karo!
Note:           BPL card pe FREE hai!"""

# Tool 9 — Consumer Rights
def consumer_rights(complaint_type, amount):
    if amount <= 1000000:
        forum = "District Consumer Forum"
    elif amount <= 10000000:
        forum = "State Consumer Commission"
    else:
        forum = "National Consumer Commission"
    return f"""
🛡️ Consumer Rights:
Complaint:      {complaint_type}
Amount:         ₹{amount}
Go To:          {forum}
Time Limit:     2 saal mein complaint karo
Fee:            ₹100 - ₹500 only
Helpline:       1800-11-4000 (FREE)
Note:           Documents preserve karo!"""

# Tool 10 — Cheque Bounce
def cheque_bounce(amount, times):
    fine = min(amount * 2, 200000)
    jail = "2 saal tak jail ho sakti hai"
    if times > 1:
        severity = "Serious — Turant vakeel lo! 🔴"
    else:
        severity = "Warning — Notice bhejo ⚠️"
    return f"""
💳 Cheque Bounce Law:
Amount:         ₹{amount}
Times Bounced:  {times}
Max Fine:       ₹{fine}
Jail:           {jail}
Severity:       {severity}
Section:        NI Act Section 138
Action:         30 din mein legal notice bhejo!"""

# Tool 11 — Partnership Deed
def partnership_deed(partners, business):
    return f"""
🤝 Partnership Deed Info:
Partners:       {partners} log
Business:       {business}
Key Clauses:
  ✅ Profit/Loss sharing ratio
  ✅ Capital contribution
  ✅ Roles & responsibilities
  ✅ Dispute resolution
  ✅ Exit clause
Stamp Duty:     ₹500 - ₹1000
Registration:   Optional but recommended
Note:           CA/Vakeel se banwao!"""

# Tool 12 — Cyber Crime Guide
def cyber_crime(crime_type):
    guides = {
        "fraud": "Turant bank ko call karo! Cyber Crime Portal: cybercrime.gov.in",
        "hacking": "FIR darj karo — IT Act Section 66. Evidence preserve karo!",
        "harassment": "Cyber Crime Cell mein complaint karo. Screenshot lo!",
        "identity theft": "Bank + Police + UIDAI ko inform karo turant!",
        "fake news": "Press Council ya cyber cell mein report karo."
    }
    guide = guides.get(crime_type.lower(),
        "cybercrime.gov.in pe report karo ya 1930 pe call karo!")
    return f"""
📱 Cyber Crime Guide:
Crime Type:     {crime_type}
Action:         {guide}
Helpline:       1930 (Cyber Crime)
Portal:         cybercrime.gov.in
Note:           Evidence DELETE mat karo!"""

# ================================
# AI LEGAL CHATBOT
# ================================
def legal_chatbot(sawaal):
    history.append({
        "role": "user",
        "content": f"Indian law expert vakeel ki tarah simple Hindi mein jawab do: {sawaal}"
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
def legal_manager(sawaal):
    s = sawaal.lower()
    print(f"⚖️ Sawaal: {sawaal}")
    print("----")

    if "contract" in s or "agreement" in s:
        return contract_checker("Sale Agreement", 500000)
    elif "business register" in s or "registration" in s:
        return business_registration("sole")
    elif "labour" in s or "employee law" in s:
        return labour_law(25)
    elif "property" in s or "zameen" in s:
        return property_law("Residential", 5000000)
    elif "family" in s or "divorce" in s or "marriage" in s:
        return family_law("marriage")
    elif "traffic" in s or "challan" in s:
        return traffic_violation("no helmet")
    elif "legal fee" in s or "vakeel" in s:
        return legal_fee("civil", "medium")
    elif "rti" in s:
        return rti_guide("Municipal Corporation")
    elif "consumer" in s or "complaint" in s:
        return consumer_rights("Product Defect", 50000)
    elif "cheque" in s or "bounce" in s:
        return cheque_bounce(100000, 1)
    elif "partnership" in s:
        return partnership_deed(3, "Trading Business")
    elif "cyber" in s or "online fraud" in s:
        return cyber_crime("fraud")
    else:
        return legal_chatbot(sawaal)

# ================================
# TEST KARO!
# ================================
print("=" * 45)
print("   ⚖️  DEBRIS LEGAL AGENT ⚖️")
print("=" * 45)

tests = [
    "Contract check karo",
    "Business register kaise karo?",
    "Labour law kya hai?",
    "Property kharidni hai",
    "Traffic challan kya hai?",
    "RTI kaise karo?",
    "Consumer complaint karna hai",
]

for sawaal in tests:
    print(legal_manager(sawaal))
    print("=" * 45)
