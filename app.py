import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="DEBRIS AI PLATFORM",
    page_icon="🤖",
    layout="wide"
)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ================================
# HEADER
# ================================
st.title("🤖 DEBRIS AI PLATFORM")
st.markdown("### 10 Agents — 120 Tools — Aapka Complete AI Assistant!")
st.divider()

# ================================
# SIDEBAR — AGENT SELECTOR
# ================================
st.sidebar.title("🎯 Agent Chuniye")
agent = st.sidebar.selectbox(
    "Kaunsa Agent chahiye?",
    [
        "💰 Finance Agent",
        "🏥 Healthcare Agent",
        "🏪 Business Agent",
        "⚖️ Legal Agent",
        "🎓 Education Agent",
        "🏠 Real Estate Agent",
        "💹 Investment Agent",
        "✍️ Content & SEO Agent",
        "💻 Developer Agent",
        "🛡️ Insurance Agent"
    ]
)
st.sidebar.divider()
st.sidebar.success("Made by Debris AI 🚀")

# ================================
# AI CHAT FUNCTION
# ================================
def ai_chat(sawaal, agent_type):
    prompts = {
        "💰 Finance Agent": "Finance expert ki tarah Hindi mein jawab do",
        "🏥 Healthcare Agent": "Doctor ki tarah Hindi mein jawab do",
        "🏪 Business Agent": "Business expert ki tarah Hindi mein jawab do",
        "⚖️ Legal Agent": "Indian vakeel ki tarah Hindi mein jawab do",
        "🎓 Education Agent": "Teacher ki tarah Hindi mein jawab do",
        "🏠 Real Estate Agent": "Real estate expert ki tarah Hindi mein jawab do",
        "💹 Investment Agent": "Investment advisor ki tarah Hindi mein jawab do",
        "✍️ Content & SEO Agent": "Content expert ki tarah Hindi mein jawab do",
        "💻 Developer Agent": "Senior developer ki tarah Hindi mein jawab do",
        "🛡️ Insurance Agent": "Insurance expert ki tarah Hindi mein jawab do"
    }
    prompt = prompts.get(agent_type,
        "Expert ki tarah Hindi mein jawab do")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": f"{prompt}: {sawaal}"
        }]
    )
    return response.choices[0].message.content

# ================================
# FINANCE AGENT
# ================================
if agent == "💰 Finance Agent":
    st.header("💰 AI Finance Agent")
    st.markdown("*12 Finance Tools + AI Assistant*")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["EMI", "GST", "Tax", "AI Chat"])

    with tab1:
        st.subheader("📊 EMI Calculator")
        col1, col2, col3 = st.columns(3)
        with col1:
            loan = st.number_input("Loan (₹)",
                value=500000, step=10000)
        with col2:
            rate = st.number_input("Rate (%)",
                value=10.0, step=0.1)
        with col3:
            years = st.number_input("Years",
                value=5, step=1)
        if st.button("Calculate EMI 💸"):
            r = rate/100/12
            n = years*12
            emi = loan * r * (1+r)**n / ((1+r)**n - 1)
            st.success(f"Monthly EMI: ₹{round(emi)}")
            st.info(f"Total Payment: ₹{round(emi*n)}")
            st.warning(f"Total Interest: ₹{round(emi*n - loan)}")

    with tab2:
        st.subheader("🧾 GST Calculator")
        col1, col2 = st.columns(2)
        with col1:
            amount = st.number_input("Amount (₹)",
                value=1000, step=100)
        with col2:
            gst_rate = st.selectbox("GST Rate",
                [5, 12, 18, 28])
        if st.button("Calculate GST 🧾"):
            gst = amount * gst_rate/100
            st.success(f"GST Amount: ₹{round(gst)}")
            st.info(f"Total with GST: ₹{round(amount+gst)}")

    with tab3:
        st.subheader("💼 Tax Calculator")
        income = st.number_input("Annual Income (₹)",
            value=800000, step=10000)
        if st.button("Calculate Tax 💼"):
            if income <= 300000: tax = 0
            elif income <= 700000:
                tax = (income-300000)*0.05
            elif income <= 1000000:
                tax = 20000+(income-700000)*0.10
            else:
                tax = 50000+(income-1000000)*0.20
            st.success(f"Tax: ₹{round(tax)}")
            st.info(f"After Tax Income: ₹{round(income-tax)}")

    with tab4:
        st.subheader("🤖 AI Finance Assistant")
        sawaal = st.text_input(
            "Finance ka koi bhi sawaal poochho...")
        if st.button("Poochho 🤖"):
            if sawaal:
                with st.spinner("Jawab aa raha hai..."):
                    jawab = ai_chat(sawaal, agent)
                    st.success(jawab)

# ================================
# HEALTHCARE AGENT
# ================================
elif agent == "🏥 Healthcare Agent":
    st.header("🏥 AI Healthcare Agent")
    st.markdown("*12 Health Tools + AI Doctor*")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["BMI", "Water", "Calories", "AI Chat"])

    with tab1:
        st.subheader("💪 BMI Calculator")
        col1, col2 = st.columns(2)
        with col1:
            weight = st.number_input("Weight (kg)",
                value=70)
        with col2:
            height = st.number_input("Height (m)",
                value=1.70)
        if st.button("Calculate BMI 💪"):
            bmi = weight/(height**2)
            if bmi < 18.5: status = "Underweight ⚠️"
            elif bmi < 25: status = "Normal ✅"
            elif bmi < 30: status = "Overweight ⚠️"
            else: status = "Obese ❌"
            st.success(f"BMI: {round(bmi,1)}")
            st.info(f"Status: {status}")

    with tab2:
        st.subheader("💧 Water Intake")
        w = st.number_input("Weight (kg)",
            value=70, key="ww")
        if st.button("Calculate 💧"):
            water = w * 0.033
            st.success(f"Daily Water: {round(water,1)} liters")
            st.info(f"Glasses: {round(water/0.25)} glass/day")

    with tab3:
        st.subheader("🔥 Calorie Calculator")
        col1, col2 = st.columns(2)
        with col1:
            w2 = st.number_input("Weight (kg)",
                value=70, key="wc")
            h2 = st.number_input("Height (m)",
                value=1.70, key="hc")
        with col2:
            a2 = st.number_input("Age",
                value=25, key="ac")
            g2 = st.selectbox("Gender",
                ["Male", "Female"])
        if st.button("Calculate 🔥"):
            if g2 == "Male":
                bmr = 88.36+(13.4*w2)+(4.8*h2*100)-(5.7*a2)
            else:
                bmr = 447.6+(9.2*w2)+(3.1*h2*100)-(4.3*a2)
            st.success(f"Daily Calories: {round(bmr)}")
            st.info(f"Active Day: {round(bmr*1.5)}")

    with tab4:
        st.subheader("🤖 AI Doctor")
        sawaal = st.text_input(
            "Health ka koi bhi sawaal poochho...")
        if st.button("Poochho 🤖"):
            if sawaal:
                with st.spinner("Doctor jawab de raha hai..."):
                    jawab = ai_chat(sawaal, agent)
                    st.success(jawab)

# ================================
# ALL OTHER AGENTS
# ================================
else:
    st.header(agent)

    # Agent description
    descriptions = {
        "🏪 Business Agent": "Stock, Revenue, Profit, Salary aur business tools",
        "⚖️ Legal Agent": "Contract, Property, Labour Law aur legal guides",
        "🎓 Education Agent": "GPA, Scholarship, Career Guide aur study tools",
        "🏠 Real Estate Agent": "Property Price, EMI, Vastu aur real estate tools",
        "💹 Investment Agent": "SIP, FD, PPF, Gold aur investment calculators",
        "✍️ Content & SEO Agent": "Blog, SEO, Keywords aur content tools",
        "💻 Developer Agent": "Code, Git, Debug aur developer tools",
        "🛡️ Insurance Agent": "Life, Health, Car aur insurance calculators"
    }

    desc = descriptions.get(agent, "AI Agent")
    st.info(f"🛠️ Tools: {desc}")
    st.markdown("### 🤖 AI Assistant")

    sawaal = st.text_input(
        f"{agent} se kuch bhi poochho...")
    if st.button("Poochho 🤖", key="other"):
        if sawaal:
            with st.spinner("Jawab aa raha hai..."):
                jawab = ai_chat(sawaal, agent)
                st.success(jawab)

    st.divider()
    st.markdown(
        "💡 *Tip: Seedha sawaal poochho — AI best jawab dega!*")

# ================================
# FOOTER
# ================================
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**🤖 DEBRIS AI PLATFORM**")
with col2:
    st.markdown("**10 Agents | 120 Tools**")
with col3:
    st.markdown("**Made with ❤️ by Debris**")
