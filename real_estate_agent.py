from groq import Groq
import datetime
import pytz

client = Groq(api_key="YOUR_API_KEY_HERE")
history = []

# ================================
# 12 REAL ESTATE TOOLS
# ================================

# Tool 1 — Property Price Calculator
def property_price(area_sqft, price_per_sqft):
    total = area_sqft * price_per_sqft
    registration = total * 0.01
    stamp_duty = total * 0.05
    total_cost = total + registration + stamp_duty
    return f"""
🏠 Property Price:
Area:           {area_sqft} sqft
Rate:           ₹{price_per_sqft}/sqft
Property Value: ₹{total}
Stamp Duty (5%): ₹{round(stamp_duty)}
Registration (1%): ₹{round(registration)}
Total Cost:     ₹{round(total_cost)}"""

# Tool 2 — Home Loan EMI
def home_loan_emi(loan_amount, years):
    rate = 8.5 / 100 / 12
    months = years * 12
    emi = loan_amount * rate * (1 + rate)**months
    emi = emi / ((1 + rate)**months - 1)
    total = emi * months
    interest = total - loan_amount
    return f"""
🏦 Home Loan EMI:
Loan Amount:    ₹{loan_amount}
Duration:       {years} saal
Interest Rate:  8.5% per year
Monthly EMI:    ₹{round(emi)}
Total Payment:  ₹{round(total)}
Total Interest: ₹{round(interest)}"""

# Tool 3 — Rent vs Buy
def rent_vs_buy(monthly_rent, property_price_val, years):
    total_rent = monthly_rent * 12 * years
    loan = property_price_val * 0.8
    rate = 8.5 / 100 / 12
    months = years * 12
    emi = loan * rate * (1+rate)**months / ((1+rate)**months - 1)
    total_emi = emi * months
    appreciation = property_price_val * (1.07 ** years)
    profit = appreciation - total_emi - (property_price_val * 0.2)
    return f"""
🤔 Rent vs Buy:
Monthly Rent:   ₹{monthly_rent}
Total Rent ({years}yr): ₹{round(total_rent)}
Property Price: ₹{property_price_val}
Total EMI:      ₹{round(total_emi)}
Future Value:   ₹{round(appreciation)}
Buying Profit:  ₹{round(profit)}
Decision:       {'Buy karo! ✅' if profit > total_rent else 'Abhi rent karo ⚠️'}"""

# Tool 4 — Rental Yield
def rental_yield(property_value, monthly_rent):
    annual_rent = monthly_rent * 12
    gross_yield = (annual_rent / property_value) * 100
    net_yield = gross_yield - 1.5
    return f"""
💰 Rental Yield:
Property Value: ₹{property_value}
Monthly Rent:   ₹{monthly_rent}
Annual Rent:    ₹{annual_rent}
Gross Yield:    {round(gross_yield, 2)}%
Net Yield:      {round(net_yield, 2)}%
Status:         {'Good Investment ✅' if gross_yield > 3 else 'Low Yield ⚠️'}"""

# Tool 5 — Property Tax
def property_tax(property_value, city_type):
    rates = {
        "metro": 0.15,
        "city": 0.10,
        "town": 0.07
    }
    rate = rates.get(city_type.lower(), 0.10)
    annual_tax = property_value * rate / 100
    monthly = annual_tax / 12
    return f"""
🏛️ Property Tax:
Property Value: ₹{property_value}
City Type:      {city_type}
Annual Tax:     ₹{round(annual_tax)}
Monthly:        ₹{round(monthly)}
Note:           Municipal office mein bharo!"""

# Tool 6 — Plot Area Converter
def area_converter(value, from_unit):
    conversions = {
        "sqft": {"sqm": 0.0929, "yard": 0.111, "acre": 0.0000229, "sqft": 1},
        "sqm": {"sqft": 10.764, "yard": 1.196, "acre": 0.000247, "sqm": 1},
        "yard": {"sqft": 9, "sqm": 0.836, "acre": 0.000207, "yard": 1},
        "acre": {"sqft": 43560, "sqm": 4047, "yard": 4840, "acre": 1}
    }
    conv = conversions.get(from_unit.lower(), conversions["sqft"])
    return f"""
📐 Area Converter:
Input:          {value} {from_unit}
In Sq. Feet:    {round(value * conv.get('sqft', 1))} sqft
In Sq. Meter:   {round(value * conv.get('sqm', 1))} sqm
In Sq. Yard:    {round(value * conv.get('yard', 1))} sqyard
In Acre:        {round(value * conv.get('acre', 1), 4)} acre"""

# Tool 7 — Construction Cost
def construction_cost(area_sqft, quality):
    rates = {
        "basic": 1500,
        "standard": 2000,
        "premium": 2500,
        "luxury": 3500
    }
    rate = rates.get(quality.lower(), 2000)
    total = area_sqft * rate
    interior = total * 0.25
    total_with_interior = total + interior
    return f"""
🏗️ Construction Cost:
Area:           {area_sqft} sqft
Quality:        {quality}
Rate:           ₹{rate}/sqft
Base Cost:      ₹{total}
Interior (25%): ₹{round(interior)}
Total Cost:     ₹{round(total_with_interior)}
Timeline:       {round(area_sqft/300)} mahine"""

# Tool 8 — Down Payment Planner
def down_payment(property_value, savings_per_month):
    down = property_value * 0.20
    months = down / savings_per_month
    years = round(months / 12, 1)
    india = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(india)
    target_year = now.year + int(years)
    return f"""
💳 Down Payment Planner:
Property Value: ₹{property_value}
Down Payment:   ₹{round(down)} (20%)
Monthly Saving: ₹{savings_per_month}
Time Needed:    {years} saal
Target Year:    {target_year}
Tip:            SIP mein invest karo — jaldi hoga!"""

# Tool 9 — Vastu Checker
def vastu_checker(direction):
    vastu = {
        "north": "✅ North — Dhan aur prosperity ke liye shubh! Main door yahan best.",
        "south": "⚠️ South — Vastu anusar achha nahi. Expert se poochho.",
        "east": "✅ East — Swasthya aur sunrise ke liye best direction!",
        "west": "✅ West — Career aur growth ke liye achha.",
        "northeast": "✅ Northeast — Ishaan kona — sabse shubh! Puja room yahan.",
        "northwest": "⚠️ Northwest — Vayu kona — sochke lo.",
        "southeast": "⚠️ Southeast — Agni kona — kitchen ke liye sahi.",
        "southwest": "✅ Southwest — Nairutya — master bedroom ke liye best."
    }
    tip = vastu.get(direction.lower(),
        "Vastu expert se consultation lo!")
    return f"""
🧭 Vastu Checker:
Direction:      {direction}
Vastu Guide:    {tip}
Note:           Vastu ek guide hai — final decision aapka!"""

# Tool 10 — Property Investment ROI
def property_roi(purchase_price, current_value, years, rental_income_yearly):
    capital_gain = current_value - purchase_price
    total_rental = rental_income_yearly * years
    total_return = capital_gain + total_rental
    roi = (total_return / purchase_price) * 100
    cagr = ((current_value / purchase_price) ** (1/years) - 1) * 100
    return f"""
📈 Property ROI:
Purchase Price: ₹{purchase_price}
Current Value:  ₹{current_value}
Capital Gain:   ₹{capital_gain}
Rental Income:  ₹{total_rental}
Total Return:   ₹{total_return}
ROI:            {round(roi, 1)}%
CAGR:           {round(cagr, 1)}%
Status:         {'Excellent ✅' if cagr > 8 else 'Average ⚠️'}"""

# Tool 11 — Society Maintenance
def society_maintenance(flat_area, rate_per_sqft):
    monthly = flat_area * rate_per_sqft
    annual = monthly * 12
    return f"""
🏢 Society Maintenance:
Flat Area:      {flat_area} sqft
Rate:           ₹{rate_per_sqft}/sqft
Monthly:        ₹{monthly}
Annual:         ₹{annual}
Sinking Fund:   ₹{round(monthly * 0.1)}/month extra
Note:           Society AGM mein rate decide hota hai!"""

# Tool 12 — RERA Check Guide
def rera_check(state):
    websites = {
        "maharashtra": "maharera.mahaonline.gov.in",
        "delhi": "rera.delhi.gov.in",
        "up": "up-rera.in",
        "karnataka": "rera.karnataka.gov.in",
        "gujarat": "gujrera.gujarat.gov.in",
        "rajasthan": "rera.rajasthan.gov.in"
    }
    site = websites.get(state.lower(), "rera.gov.in")
    return f"""
📋 RERA Check:
State:          {state}
RERA Website:   {site}
What to Check:
  ✅ Project Registration Number
  ✅ Builder Registration
  ✅ Project Completion Date
  ✅ Complaints History
Note:           RERA registered project hi lo!
Helpline:       1800-11-RERA"""

# ================================
# AI REAL ESTATE CHATBOT
# ================================
def realestate_chatbot(sawaal):
    history.append({
        "role": "user",
        "content": f"Real estate expert ki tarah simple Hindi mein jawab do: {sawaal}"
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
def realestate_manager(sawaal):
    s = sawaal.lower()
    print(f"🏠 Sawaal: {sawaal}")
    print("----")

    if "price" in s or "kimat" in s or "property value" in s:
        return property_price(1000, 5000)
    elif "emi" in s or "loan" in s:
        return home_loan_emi(5000000, 20)
    elif "rent vs buy" in s or "kharidna" in s:
        return rent_vs_buy(20000, 5000000, 10)
    elif "rental yield" in s or "yield" in s:
        return rental_yield(5000000, 20000)
    elif "property tax" in s or "tax" in s:
        return property_tax(5000000, "metro")
    elif "area" in s or "convert" in s:
        return area_converter(1000, "sqft")
    elif "construction" in s or "banwana" in s:
        return construction_cost(1000, "standard")
    elif "down payment" in s or "downpayment" in s:
        return down_payment(5000000, 25000)
    elif "vastu" in s:
        return vastu_checker("north")
    elif "roi" in s or "return" in s:
        return property_roi(3000000, 5000000, 5, 180000)
    elif "maintenance" in s or "society" in s:
        return society_maintenance(1000, 3)
    elif "rera" in s:
        return rera_check("maharashtra")
    else:
        return realestate_chatbot(sawaal)

# ================================
# TEST KARO!
# ================================
print("=" * 45)
print("   🏠 DEBRIS REAL ESTATE AGENT 🏠")
print("=" * 45)

tests = [
    "Property price kya hai?",
    "Home loan EMI kitni hogi?",
    "Rental yield kya hai?",
    "Construction cost kitna hoga?",
    "Down payment kaise karu?",
    "Vastu check karo",
    "Property ROI kya hai?",
]

for sawaal in tests:
    print(realestate_manager(sawaal))
    print("=" * 45)
