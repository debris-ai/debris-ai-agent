from groq import Groq
import datetime
import pytz

client = Groq(api_key="YOUR_API_KEY_HERE")
history = []

# ================================
# 12 INVESTMENT TOOLS
# ================================

# Tool 1 — SIP Calculator
def sip_calculator(monthly_amount, years, expected_return):
    rate = expected_return / 100 / 12
    months = years * 12
    future_value = monthly_amount * ((1 + rate)**months - 1) / rate * (1 + rate)
    invested = monthly_amount * months
    profit = future_value - invested
    return f"""
📈 SIP Calculator:
Monthly SIP:    ₹{monthly_amount}
Duration:       {years} saal
Expected Return: {expected_return}% per year
Total Invested: ₹{round(invested)}
Future Value:   ₹{round(future_value)}
Profit:         ₹{round(profit)}
Wealth Ratio:   {round(future_value/invested, 1)}x"""

# Tool 2 — Lumpsum Calculator
def lumpsum_calculator(amount, years, expected_return):
    future_value = amount * (1 + expected_return/100) ** years
    profit = future_value - amount
    return f"""
💰 Lumpsum Calculator:
Investment:     ₹{amount}
Duration:       {years} saal
Expected Return: {expected_return}% per year
Future Value:   ₹{round(future_value)}
Profit:         ₹{round(profit)}
Wealth Ratio:   {round(future_value/amount, 1)}x"""

# Tool 3 — Stock Returns
def stock_returns(buy_price, current_price, shares, dividends):
    capital_gain = (current_price - buy_price) * shares
    total_investment = buy_price * shares
    roi = ((capital_gain + dividends) / total_investment) * 100
    return f"""
📊 Stock Returns:
Buy Price:      ₹{buy_price}
Current Price:  ₹{current_price}
Shares:         {shares}
Capital Gain:   ₹{round(capital_gain)}
Dividends:      ₹{dividends}
Total Return:   ₹{round(capital_gain + dividends)}
ROI:            {round(roi, 2)}%
Status:         {'Profit ✅' if roi > 0 else 'Loss ❌'}"""

# Tool 4 — Fixed Deposit
def fixed_deposit(principal, years, interest_rate):
    # Quarterly compounding
    amount = principal * (1 + interest_rate/100/4) ** (4*years)
    interest = amount - principal
    return f"""
🏦 Fixed Deposit:
Principal:      ₹{principal}
Duration:       {years} saal
Interest Rate:  {interest_rate}% per year
Maturity Amount: ₹{round(amount)}
Interest Earned: ₹{round(interest)}
Effective Yield: {round((amount/principal - 1)*100/years, 2)}% per year
Tax Note:       Interest pe TDS lagega!"""

# Tool 5 — PPF Calculator
def ppf_calculator(yearly_amount, years):
    rate = 7.1 / 100
    total = 0
    for year in range(1, years + 1):
        total = (total + yearly_amount) * (1 + rate)
    invested = yearly_amount * years
    profit = total - invested
    return f"""
🏛️ PPF Calculator:
Yearly Amount:  ₹{yearly_amount}
Duration:       {years} saal
Interest Rate:  7.1% (current)
Total Invested: ₹{invested}
Maturity Value: ₹{round(total)}
Total Profit:   ₹{round(profit)}
Tax Benefit:    Section 80C — ₹1.5L tak!
Note:           Lock-in 15 saal — safe investment!"""

# Tool 6 — Gold Investment
def gold_investment(grams, buy_price_per_gram, current_price):
    investment = grams * buy_price_per_gram
    current_value = grams * current_price
    profit = current_value - investment
    roi = (profit / investment) * 100
    return f"""
🥇 Gold Investment:
Quantity:       {grams} grams
Buy Price:      ₹{buy_price_per_gram}/gram
Current Price:  ₹{current_price}/gram
Investment:     ₹{investment}
Current Value:  ₹{current_value}
Profit/Loss:    ₹{round(profit)}
ROI:            {round(roi, 2)}%
Tip:            Digital Gold ya SGBs consider karo!"""

# Tool 7 — Risk Profile
def risk_profile(age, income, dependents, investment_goal):
    score = 0
    if age < 30: score += 3
    elif age < 45: score += 2
    else: score += 1
    if income > 1000000: score += 3
    elif income > 500000: score += 2
    else: score += 1
    if dependents == 0: score += 3
    elif dependents <= 2: score += 2
    else: score += 1
    if investment_goal == "growth": score += 3
    elif investment_goal == "balanced": score += 2
    else: score += 1
    if score >= 10:
        profile = "Aggressive 🔥 — 80% Equity, 20% Debt"
    elif score >= 7:
        profile = "Moderate ⚖️ — 60% Equity, 40% Debt"
    else:
        profile = "Conservative 🛡️ — 30% Equity, 70% Debt"
    return f"""
🎯 Risk Profile:
Age:            {age} saal
Income:         ₹{income}
Dependents:     {dependents}
Goal:           {investment_goal}
Risk Score:     {score}/12
Profile:        {profile}
Suggestion:     Financial advisor se milo!"""

# Tool 8 — Mutual Fund Returns
def mutual_fund_returns(invested, nav_buy, nav_current, units):
    current_value = nav_current * units
    profit = current_value - invested
    roi = (profit / invested) * 100
    return f"""
📑 Mutual Fund Returns:
Amount Invested: ₹{invested}
Buy NAV:        ₹{nav_buy}
Current NAV:    ₹{nav_current}
Units:          {units}
Current Value:  ₹{round(current_value)}
Profit/Loss:    ₹{round(profit)}
Returns:        {round(roi, 2)}%
Status:         {'Profit ✅' if roi > 0 else 'Loss ❌'}"""

# Tool 9 — Emergency Fund
def emergency_fund(monthly_expenses, months):
    required = monthly_expenses * months
    liquid = required * 0.5
    fd = required * 0.5
    return f"""
🆘 Emergency Fund:
Monthly Expenses: ₹{monthly_expenses}
Months Coverage: {months}
Required Fund:  ₹{required}
Keep in Savings: ₹{round(liquid)} (liquid)
Keep in FD:     ₹{round(fd)} (3-6 month FD)
Current Status: {'✅ Good' if months >= 6 else '⚠️ Increase karo!'}
Note:           6 mahine ka fund minimum zaroori!"""

# Tool 10 — Retirement Planner
def retirement_planner(current_age, retire_age,
                       monthly_expense, inflation):
    years_to_retire = retire_age - current_age
    years_in_retirement = 85 - retire_age
    future_monthly = monthly_expense * (
        (1 + inflation/100) ** years_to_retire)
    corpus_needed = future_monthly * 12 * years_in_retirement
    monthly_sip = corpus_needed / (
        ((1.12**years_to_retire - 1) / 0.12) * 12)
    return f"""
👴 Retirement Planner:
Current Age:    {current_age} saal
Retire At:      {retire_age} saal
Years Left:     {years_to_retire} saal
Monthly Expense: ₹{monthly_expense}
Future Expense: ₹{round(future_monthly)}/month
Corpus Needed:  ₹{round(corpus_needed)}
Monthly SIP:    ₹{round(monthly_sip)} abhi shuru karo!
Note:           Jitna jaldi shuru, utna acha!"""

# Tool 11 — Tax Saving Investments
def tax_saving(income, invested_80c, nps, health_insurance):
    deduction_80c = min(invested_80c, 150000)
    deduction_nps = min(nps, 50000)
    deduction_health = min(health_insurance, 25000)
    total_deduction = deduction_80c + deduction_nps + deduction_health
    taxable_income = max(0, income - total_deduction)
    tax_saved = total_deduction * 0.30
    return f"""
💸 Tax Saving Plan:
Income:         ₹{income}
80C Investment: ₹{deduction_80c}
NPS (80CCD):    ₹{deduction_nps}
Health Insurance: ₹{deduction_health}
Total Deduction: ₹{total_deduction}
Taxable Income: ₹{taxable_income}
Tax Saved:      ₹{round(tax_saved)}
Tip:            ELSS mutual funds — best 80C option!"""

# Tool 12 — Portfolio Tracker
def portfolio_tracker(stocks, mf, fd, gold, ppf):
    total = stocks + mf + fd + gold + ppf
    return f"""
📋 Portfolio Tracker:
Stocks:         ₹{stocks} ({round(stocks/total*100, 1)}%)
Mutual Funds:   ₹{mf} ({round(mf/total*100, 1)}%)
Fixed Deposit:  ₹{fd} ({round(fd/total*100, 1)}%)
Gold:           ₹{gold} ({round(gold/total*100, 1)}%)
PPF:            ₹{ppf} ({round(ppf/total*100, 1)}%)
Total Portfolio: ₹{total}
Diversification: {'Good ✅' if min(stocks,mf,fd,gold,ppf) > 0 else 'Improve karo ⚠️'}"""

# ================================
# AI INVESTMENT CHATBOT
# ================================
def investment_chatbot(sawaal):
    history.append({
        "role": "user",
        "content": f"Investment expert financial advisor ki tarah simple Hindi mein jawab do: {sawaal}"
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
def investment_manager(sawaal):
    s = sawaal.lower()
    print(f"💹 Sawaal: {sawaal}")
    print("----")

    if "sip" in s:
        return sip_calculator(5000, 10, 12)
    elif "lumpsum" in s or "lump sum" in s:
        return lumpsum_calculator(100000, 10, 12)
    elif "stock" in s or "share" in s:
        return stock_returns(100, 150, 100, 500)
    elif "fd" in s or "fixed deposit" in s:
        return fixed_deposit(100000, 3, 7.5)
    elif "ppf" in s:
        return ppf_calculator(150000, 15)
    elif "gold" in s or "sona" in s:
        return gold_investment(10, 5500, 7200)
    elif "risk" in s or "profile" in s:
        return risk_profile(28, 600000, 1, "growth")
    elif "mutual fund" in s or "mf" in s:
        return mutual_fund_returns(100000, 50, 75, 2000)
    elif "emergency" in s:
        return emergency_fund(30000, 6)
    elif "retire" in s or "retirement" in s:
        return retirement_planner(30, 60, 30000, 6)
    elif "tax saving" in s or "80c" in s:
        return tax_saving(800000, 150000, 50000, 25000)
    elif "portfolio" in s:
        return portfolio_tracker(200000, 150000,
                                100000, 50000, 100000)
    else:
        return investment_chatbot(sawaal)

# ================================
# TEST KARO!
# ================================
print("=" * 45)
print("   💹 DEBRIS INVESTMENT AGENT 💹")
print("=" * 45)

tests = [
    "SIP calculator",
    "Fixed deposit kya milega?",
    "PPF calculator",
    "Gold investment",
    "Retirement planning karo",
    "Tax saving kaise karu?",
    "Mera portfolio check karo",
]

for sawaal in tests:
    print(investment_manager(sawaal))
    print("=" * 45)
