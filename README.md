# 🏦 FinPulse — An Autonomous Agentic AI for Proactive Banking Engagement

> **Banking that acts before you ask.**
> Replacing impersonal banking spam with a personal AI money buddy.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)](https://streamlit.io/)
[![ML](https://img.shields.io/badge/ML-scikit--learn-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Problem

Banks today "engage" customers by blasting the **same generic notifications to millions** —
*"Open a Demat Account!"* or *"EMI due in 2 days."* These are blind, one-way, impersonal.
**~98% of customers ignore them.** That's broadcasting, not engagement — and it's why banking
apps feel like spam while digital engagement keeps falling.

> Built for the **SBI Hackathon @ GFF 2026** — Theme: *Agentic AI for Customer Acquisition,
> Digital Adoption & Digital Engagement.*

---

## 💡 Solution

**FinPulse** is an Agentic AI money buddy named *Pulse* that studies each customer's actual
financial behaviour, then **autonomously reasons, decides, and acts** — speaking only when it
can genuinely help, and intelligently **staying silent** when a message would be irrelevant.

---

## ✨ Features (all in this repo)

| Feature | Where |
|---------|-------|
| 🤖 **Autonomous Agent** — monitors, decides & acts unprompted | `pulse_agent.py` |
| 🤫 **Smart Silence** — relevance filter that knows when NOT to message | `pulse_agent.py` |
| 📉 **Churn Prediction (ML)** — RandomForest flags at-risk customers | `churn_model.py` |
| 💯 **Money Health Score** — gamified 0–100 score | `finpulse_demo.py` |
| 🤔 **What-If Simulator** — instant cash-flow impact | `finpulse_demo.py` |
| 📅 **Weekly Money Story** — Spotify-Wrapped style recap | `finpulse_demo.py` |
| 🎙️ **Voice + Local Language** — Hindi/Punjabi/Tamil (Whisper-ready) | `finpulse_demo.py` |
| 👆 **One-Tap Actions** — every suggestion is a single tap | `finpulse_demo.py` |

---

## 🏗️ Architecture

```
[Customer Transaction & Behaviour Data]
            │
            ▼
[EVENT DETECTOR] — monitors triggers (salary, idle money, EMI, dormancy)
            │
            ▼
[CHURN MODEL + RELEVANCE FILTER]  ◄── SMART SILENCE (ML)
   Decides: Is this worth telling the customer?
            │ (only relevant cases pass)
            ▼
[PULSE AGENT (LLM + templates)] — reasons, personalizes, plans a one-tap action
            │
            ▼
[CUSTOMER] — gets a relevant one-tap nudge (or silence)
            │
            ▼
[MEMORY / BANK DASHBOARD — analytics]
```

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/GitwithEkam/finpulse-agentic-ai.git
cd finpulse-agentic-ai

# 2. (Recommended) create a virtual environment
python -m venv venv
# Windows:  venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) add an OpenAI key for live GPT-4o messages
#    Without a key the app uses built-in templates and still works fully.
# Windows:  set OPENAI_API_KEY=your-key
# Mac/Linux: export OPENAI_API_KEY=your-key

# 5. Run
streamlit run finpulse_demo.py
```

Then open the URL Streamlit prints (usually `http://localhost:8501`).

---

## 📂 Project Structure

```
finpulse-agentic-ai/
├── finpulse_demo.py     # Main Streamlit app (UI + all features)
├── pulse_agent.py       # Event detector + Smart Silence + Pulse agent
├── churn_model.py       # ML churn-prediction model
├── requirements.txt
├── SETUP_GUIDE.md       # Step-by-step guide for VS Code
├── assets/              # Screenshots for your deck
└── README.md
```

---

## 📈 Business Model

- **B2B SaaS** licensing for banks & fintechs (per active customer)
- **Per-outcome pricing** on relevant conversions
- **Premium analytics** dashboards

> Improving retention by 5% boosts bank profits by 25–95% (Bain & Co.).
> Agentic AI in BFSI is growing at 40%+ CAGR.

---

## 👤 Team

**Ekamnoor Singh** — Sardar Beant Singh State University, Gurdaspur

---


> ⭐ *FinPulse — turning passive, spammy banking apps into a money buddy people actually love.*
