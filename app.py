import streamlit as st
from groq import Groq
import datetime
import pytz

# Page setup
st.set_page_config(
    page_title="Debris AI Agent",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("💰 DEBRIS AI FINANCE AGENT")
st.write("Aapka Personal AI Finance Assistant!")
st.divider()

# API Key
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

history = []

# ================================
# 12 FINANCE TOOLS
# ================================
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    total = p + si
    return f"💰 Simple Interest\nPrincipal: ₹{p}\nRate: {r}%\nTime: {t} saal\nInterest: ₹{si}\nTotal: ₹{total}"

def compound_interest(p, r, t):
    ci = p * (1 + r/100) ** t
    interest = ci - p
    return f"📈 Compound Interest\nPrincipal: ₹{p}\nRate: {r}%\nTime: {t} saal\nInterest: ₹{round(interest,2)}\nTotal: ₹{round(ci,2)}"

def emi_calculator(p, r, t):
    r_monthly = r / (12 * 100)
    n = t * 12
    emi = (p * r_monthly * (1 + r_monthly)**n) / ((1 + r_monthly)**n - 1)
    return f"💸 EMI Calculator\nLoan: ₹{p}\nRate: {r}%\nTime: {t} saal\nEMI: ₹{round(emi,2)}/month\nTotal: ₹{round(emi*n,2)}"

def profit_loss(cp, sp):
    if sp > cp:
        profit = sp - cp
        percent = (profit/cp)*100
        return f"💹 Profit\nCost: ₹{cp}\nSell: ₹{sp}\nProfit: ₹{profit}\nProfit%: {round(percent,2)}%"
    else:
        loss = cp - sp
        percent = (loss/cp)*100
        return f"📉 Loss\nCost: ₹{cp}\nSell: ₹{sp}\nLoss: ₹{loss}\nLoss%: {round(percent,2)}%"

def gst_calculator(price, gst_rate):
    gst_amount = (price * gst_rate) / 100
    total = price + gst_amount
    return f"🏦 GST Calculator\nPrice: ₹{price}\nGST: {gst_rate}%\nGST Amount: ₹{gst_amount}\nTotal: ₹{total}"

def discount_calculator(price, discount):
    discount_amount = (price * discount) / 100
    final_price = price - discount_amount
    return f"💳 Discount\nOriginal: ₹{price}\nDiscount: {discount}%\nYou Save: ₹{discount_amount}\nFinal: ₹{final_price}"

def tax_calculator(income):
    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = (income - 300000) * 0.05
    elif income <= 900000:
        tax = 15000 + (income - 600000) * 0.10
    else:
        tax = 45000 + (income - 900000) * 0.15
    return f"💼 Tax Calculator\nIncome: ₹{income}\nTax: ₹{round(tax,2)}\nAfter Tax: ₹{round(income-tax,2)}"

def loan_eligibility(salary):
    max_emi = salary * 0.40
    max_loan = max_emi * 12 * 20
    return f"🏠 Loan Eligibility\nSalary: ₹{salary}\nMax EMI: ₹{max_emi}\nMax Loan: ₹{max_loan}"

def finance_chatbot(sawaal):
    history.append({"role": "user", "content": sawaal})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history
    )
    jawab = response.choices[0].message.content
    history.append({"role": "assistant", "content": jawab})
    return jawab

def finance_manager(sawaal):
    s = sawaal.lower()
    if "simple interest" in s:
        return simple_interest(10000, 5, 2)
    elif "compound" in s:
        return compound_interest(10000, 8, 5)
    elif "emi" in s:
        return emi_calculator(500000, 10, 5)
    elif "profit" in s or "loss" in s:
        return profit_loss(1000, 1200)
    elif "gst" in s:
        return gst_calculator(1000, 18)
    elif "discount" in s:
        return discount_calculator(2000, 20)
    elif "tax" in s:
        return tax_calculator(800000)
    elif "loan" in s:
        return loan_eligibility(50000)
    else:
        return finance_chatbot(sawaal)

# ================================
# CHAT UI
# ================================
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

sawaal = st.chat_input("Apna sawaal likhiye...")

if sawaal:
    with st.chat_message("user"):
        st.write(sawaal)
    st.session_state.messages.append({
        "role": "user",
        "content": sawaal
    })

    with st.chat_message("assistant"):
        jawab = finance_manager(sawaal)
        st.write(jawab)
    st.session_state.messages.append({
        "role": "assistant",
        "content": jawab
    })
