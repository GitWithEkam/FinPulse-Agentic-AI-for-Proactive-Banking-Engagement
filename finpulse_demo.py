# finpulse_demo.py
# ---------------------------------------------------------------------------
# FinPulse — Autonomous Agentic AI Money Buddy  ("Pulse")
# ---------------------------------------------------------------------------
# Main Streamlit application. Ties together every feature we discussed:
#   • Event Detector          • Smart Silence (anti-spam filter)
#   • Churn-Prediction ML      • Pulse Agent (personalized one-tap actions)
#   • Money Health Score       • What-If Simulator
#   • Weekly Money Story       • Voice / Language (simulated)
#
# Run:  streamlit run finpulse_demo.py
# ---------------------------------------------------------------------------

from datetime import datetime

import pandas as pd
import streamlit as st

from churn_model import train_churn_model, predict_churn
from pulse_agent import detect_events, smart_silence_filter, pulse_agent

# ===========================================================================
# PAGE CONFIG
# ===========================================================================
st.set_page_config(
    page_title="FinPulse — Agentic AI Money Buddy",
    page_icon="🏦",
    layout="wide",
)

st.title("🏦 FinPulse — Your Autonomous AI Money Buddy, *Pulse*")
st.caption("Not spam. A smart advisor that acts only when it truly helps you.")


# ===========================================================================
# LOAD THE ML MODEL ONCE (cached so it doesn't retrain on every click)
# ===========================================================================
@st.cache_resource
def load_model():
    return train_churn_model()

churn_model, model_acc, model_features = load_model()


# ===========================================================================
# MOCK CUSTOMER DATA  (in production this comes from the bank's core systems)
# ===========================================================================
def default_customer():
    return {
        "name": "Ekamnoor",
        "balance": 84_000,
        "idle_amount": 50_000,
        "idle_months": 3,
        "savings_account": False,
        "language": "English",
        "money_health_score": 68,
        # Fields used by the churn model:
        "last_login_days_ago": 2,
        "monthly_transactions": 6,
        "avg_balance": 84_000,
        "products_used": 2,
        "ignored_notifications": 12,
    }

transactions = pd.DataFrame([
    {"date": "2026-06-01", "type": "Salary Credit",  "amount": 75_000, "category": "Income"},
    {"date": "2026-06-03", "type": "Shopping",       "amount": 18_000, "category": "Spend"},
    {"date": "2026-06-05", "type": "Dining",         "amount":  9_000, "category": "Spend"},
    {"date": "2026-06-07", "type": "EMI Due (10th)", "amount": 12_000, "category": "Bill"},
])


# ===========================================================================
# SIDEBAR — make the demo interactive for judges
# ===========================================================================
st.sidebar.header("⚙️ Customer Controls (Demo)")
st.sidebar.caption("Tweak these live to show Pulse reacting in real time.")

customer = default_customer()
customer["name"] = st.sidebar.text_input("Customer name", customer["name"])
customer["language"] = st.sidebar.selectbox(
    "Language", ["English", "Hindi", "Punjabi", "Tamil"]
)
customer["idle_amount"] = st.sidebar.slider(
    "Idle money (₹)", 0, 200_000, customer["idle_amount"], step=5_000
)
customer["idle_months"] = st.sidebar.slider("Idle months", 0, 12, customer["idle_months"])
customer["last_login_days_ago"] = st.sidebar.slider(
    "Days since last login", 0, 90, customer["last_login_days_ago"]
)
customer["ignored_notifications"] = st.sidebar.slider(
    "Ignored notifications", 0, 20, customer["ignored_notifications"]
)
customer["savings_account"] = st.sidebar.checkbox(
    "Has savings/investment plan", customer["savings_account"]
)


# ===========================================================================
# TOP ROW — Transactions + Money Health Score
# ===========================================================================
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Customer Transaction Feed")
    st.dataframe(transactions, use_container_width=True, hide_index=True)

with col2:
    st.subheader("💯 Money Health Score")
    st.progress(customer["money_health_score"] / 100)
    st.metric("Pulse Score", f"{customer['money_health_score']}/100", "+4 this week 🔥")
    st.caption("Gamified — improves as the customer builds good habits.")


# ===========================================================================
# CHURN PREDICTION  — the ML brain behind Smart Silence
# ===========================================================================
st.divider()
st.subheader("📉 Churn Prediction — the Smart Silence Brain (ML)")

risk_pct, risk_label = predict_churn(churn_model, customer, model_features)

c1, c2, c3 = st.columns(3)
c1.metric("Churn Risk", f"{risk_pct}%", risk_label)
c2.metric("Model Accuracy", f"{model_acc*100:.1f}%")
c3.metric("Last Login", f"{customer['last_login_days_ago']} days ago")

if risk_pct > 60:
    st.error("⚠️ Customer is drifting away! Pulse launches a high-priority, "
             "personalized re-engagement journey.")
elif risk_pct > 30:
    st.warning("🟡 Engagement slipping. Pulse sends a gentle, value-first nudge — never spam.")
else:
    st.success("✅ Healthy & engaged. Pulse stays mostly silent (Smart Silence) to avoid annoyance.")


# ===========================================================================
# PULSE AGENT — autonomous, acts WITHOUT being asked
# ===========================================================================
st.divider()
st.subheader("🤖 Pulse — Autonomous Actions (acts on its own)")

if st.button("▶ Run Pulse Agent", type="primary"):
    with st.spinner("Pulse is monitoring & thinking..."):
        all_events = detect_events(transactions, customer)
        kept, skipped = smart_silence_filter(all_events, risk_pct)
        messages = pulse_agent(kept, customer)

    # --- Show everything Pulse noticed ---
    st.markdown("**🔍 Events Detected:**")
    for e in all_events:
        st.info(f"[{e['priority'].upper()}] {e['text']}")

    # --- Smart Silence transparency ---
    st.markdown(f"**🤫 Smart Silence:** kept {len(kept)}, "
                f"skipped {len(skipped)} irrelevant message(s).")
    for e in skipped:
        st.caption(f"   ⏭️ Skipped: {e['text']}")

    # --- Personalized one-tap actions ---
    st.markdown("**📩 Personalized One-Tap Actions:**")
    if not messages:
        st.success("Pulse decided to stay completely silent right now. "
                   "Nothing useful to say = no notification. 🤫")
    for m in messages:
        if m["action"]:
            with st.container(border=True):
                st.write(m["message"])
                st.button(f"👆 {m['action']}", key=m["message"][:24])
        else:
            st.success(m["message"])  # LLM block

    st.caption(f"Generated at {datetime.now().strftime('%H:%M:%S')} — Pulse acted on its own.")


# ===========================================================================
# WHAT-IF SIMULATOR
# ===========================================================================
st.divider()
st.subheader("🤔 What-If Money Simulator")

question = st.text_input(
    "Ask Pulse anything",
    "Can I afford a ₹50,000 vacation next month?",
)
if st.button("Simulate"):
    st.success(
        "✅ Yes — but it will delay your savings goal by ~2 months.\n\n"
        "💡 Smarter option: skip dining out for 3 weeks and you can afford it "
        "with **zero** impact on your goals. Want me to build that plan?"
    )
    st.button("👆 Yes, plan it")


# ===========================================================================
# WEEKLY MONEY STORY  (Spotify-Wrapped style recap)
# ===========================================================================
st.divider()
st.subheader("📅 Weekly Money Story")

with st.expander("Open your Sunday recap 🎁"):
    total_spend = int(transactions.loc[transactions.category == "Spend", "amount"].sum())
    st.markdown(f"""
    **Hey {customer['name']}, here's your week in money 👇**

    - 💸 You spent **₹{total_spend:,}** — mostly on Shopping & Dining
    - 💰 You still have **₹{customer['idle_amount']:,}** sitting idle (let's grow it!)
    - 🏆 Your Money Health Score rose **+4** to **{customer['money_health_score']}/100**
    - 🎯 One tip: automate a small ₹2,000/month investment to hit your goal faster

    *Tap below to act on this week's #1 tip:*
    """)
    st.button("👆 Automate ₹2,000/month")


# ===========================================================================
# FOOTER
# ===========================================================================
st.divider()
st.caption(
    f"🌐 Language: {customer['language']}  •  🎙️ Voice input ready (Whisper)  •  "
    "🔒 RBI-aligned & DPDP 2023 compliant  •  Built for SBI Hackathon @ GFF 2026"
)
