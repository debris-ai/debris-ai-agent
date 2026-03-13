from groq import Groq
import datetime
import pytz

client = Groq(api_key="YOUR_API_KEY_HERE")
history = []

# ================================
# 12 BUSINESS TOOLS
# ================================

# Tool 1 — Stock Management
def stock_management(product, quantity, price):
    total_value = quantity * price
    reorder = "Haan ⚠️" if quantity < 10 else "Nahi ✅"
    return f"""
📦 Stock Management:
Product:        {product}
Quantity:       {quantity} units
Price/Unit:     ₹{price}
Total Value:    ₹{total_value}
Reorder Needed: {reorder}"""

# Tool 2 — Revenue Calculator
def revenue_calculator(units_sold, price_per_unit):
    revenue = units_sold * price_per_unit
    return f"""
💰 Revenue Calculator:
Units Sold:     {units_sold}
Price/Unit:     ₹{price_per_unit}
Total Revenue:  ₹{revenue}"""

# Tool 3 — Profit Margin
def profit_margin(revenue, cost):
    profit = revenue - cost
    margin = (profit / revenue) * 100
    return f"""
📊 Profit Margin:
Revenue:        ₹{revenue}
Total Cost:     ₹{cost}
Profit:         ₹{profit}
Margin:         {round(margin, 2)}%
Status:         {'Good ✅' if margin > 20 else 'Low ⚠️'}"""

# Tool 4 — Employee Salary
def employee_salary(basic, hra_percent, da_percent):
    hra = (basic * hra_percent) / 100
    da = (basic * da_percent) / 100
    gross = basic + hra + da
    pf = basic * 0.12
    net = gross - pf
    return f"""
👥 Employee Salary:
Basic:          ₹{basic}
HRA ({hra_percent}%):      ₹{round(hra)}
DA ({da_percent}%):       ₹{round(da)}
Gross Salary:   ₹{round(gross)}
PF Deduction:   ₹{round(pf)}
Net Salary:     ₹{round(net)}"""

# Tool 5 — Sales Target
def sales_target(target, achieved):
    percentage = (achieved / target) * 100
    remaining = target - achieved
    status = "✅ Target Poora!" if achieved >= target else f"⚠️ ₹{remaining} baaki!"
    return f"""
📈 Sales Target:
Target:         ₹{target}
Achieved:       ₹{achieved}
Completion:     {round(percentage, 1)}%
Status:         {status}"""

# Tool 6 — Expense Tracker
def expense_tracker(rent, salary, utilities, marketing, other):
    total = rent + salary + utilities + marketing + other
    return f"""
💸 Monthly Expenses:
Rent:           ₹{rent}
Salary:         ₹{salary}
Utilities:      ₹{utilities}
Marketing:      ₹{marketing}
Other:          ₹{other}
Total:          ₹{total}"""

# Tool 7 — Break Even
def break_even(fixed_cost, selling_price, variable_cost):
    contribution = selling_price - variable_cost
    units = fixed_cost / contribution
    revenue = units * selling_price
    return f"""
🎯 Break Even:
Fixed Cost:     ₹{fixed_cost}
Selling Price:  ₹{selling_price}
Variable Cost:  ₹{variable_cost}
Break Even:     {round(units)} units
BE Revenue:     ₹{round(revenue)}"""

# Tool 8 — ROI Calculator
def roi_calculator(investment, returns):
    roi = ((returns - investment) / investment) * 100
    profit = returns - investment
    return f"""
📉 ROI Calculator:
Investment:     ₹{investment}
Returns:        ₹{returns}
Profit:         ₹{profit}
ROI:            {round(roi, 2)}%
Status:         {'Profitable ✅' if roi > 0 else 'Loss ❌'}"""

# Tool 9 — Product Pricing
def product_pricing(cost, margin_percent):
    margin = (cost * margin_percent) / 100
    selling_price = cost + margin
    mrp = selling_price * 1.1
    return f"""
🏷️ Product Pricing:
Cost Price:     ₹{cost}
Margin ({margin_percent}%):   ₹{round(margin)}
Selling Price:  ₹{round(selling_price)}
MRP:            ₹{round(mrp)}"""

# Tool 10 — Cash Flow
def cash_flow(opening, income, expenses):
    closing = opening + income - expenses
    status = "Positive ✅" if closing > 0 else "Negative ❌ — Dhyan do!"
    return f"""
💼 Cash Flow:
Opening:        ₹{opening}
Income:         ₹{income}
Expenses:       ₹{expenses}
Closing:        ₹{closing}
Status:         {status}"""

# Tool 11 — Commission Calculator
def commission_calculator(sales, commission_rate):
    commission = (sales * commission_rate) / 100
    net = sales - commission
    return f"""
🤝 Commission:
Total Sales:    ₹{sales}
Rate:           {commission_rate}%
Commission:     ₹{round(commission)}
Net Amount:     ₹{round(net)}"""

# Tool 12 — Business Tax
def business_tax(annual_profit):
    if annual_profit <= 1000000:
        tax_rate = 25
    else:
        tax_rate = 30
    tax = (annual_profit * tax_rate) / 100
    net = annual_profit - tax
    return f"""
📋 Business Tax:
Annual Profit:  ₹{annual_profit}
Tax Rate:       {tax_rate}%
Tax Amount:     ₹{round(tax)}
Net Profit:     ₹{round(net)}"""

# ================================
# AI BUSINESS CHATBOT
# ================================
def business_chatbot(sawaal):
    history.append({
        "role": "user",
        "content": f"Business expert ki tarah Hindi mein jawab do: {sawaal}"
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
def business_manager(sawaal):
    s = sawaal.lower()
    print(f"👨‍💼 Sawaal: {sawaal}")
    print("----")

    if "stock" in s or "inventory" in s:
        return stock_management("Product A", 15, 500)
    elif "revenue" in s or "kamai" in s:
        return revenue_calculator(100, 500)
    elif "margin" in s or "profit margin" in s:
        return profit_margin(50000, 35000)
    elif "salary" in s or "employee" in s:
        return employee_salary(25000, 40, 20)
    elif "target" in s or "sales" in s:
        return sales_target(100000, 75000)
    elif "expense" in s or "kharcha" in s:
        return expense_tracker(10000, 50000, 5000, 8000, 3000)
    elif "break even" in s:
        return break_even(100000, 500, 200)
    elif "roi" in s or "return" in s:
        return roi_calculator(100000, 150000)
    elif "pricing" in s or "price" in s:
        return product_pricing(1000, 30)
    elif "cash flow" in s or "cash" in s:
        return cash_flow(50000, 100000, 80000)
    elif "commission" in s:
        return commission_calculator(100000, 5)
    elif "tax" in s or "business tax" in s:
        return business_tax(1000000)
    else:
        return business_chatbot(sawaal)

# ================================
# TEST KARO!
# ================================
print("=" * 45)
print("   🏪 DEBRIS BUSINESS AGENT 🏪")
print("=" * 45)

tests = [
    "Stock kitna hai?",
    "Revenue kitni hai?",
    "Profit margin kya hai?",
    "Employee salary calculate karo",
    "Sales target kya hai?",
    "Monthly expense kitna hai?",
    "ROI kya hai?",
]

for sawaal in tests:
    print(business_manager(sawaal))
    print("=" * 45)
