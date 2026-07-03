# 🏦 FinPulse — An Autonomous Agentic AI for Proactive Banking Engagement

> **Banking that acts before you ask.**
> Replacing impersonal banking spam with a personal AI money buddy.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/Agentic_AI-LangGraph-green.svg)](https://www.langchain.com/)
[![Status](https://img.shields.io/badge/Status-Prototype-orange.svg)]()

---

## 📌 Problem Statement

Banks today "engage" customers by blasting the **same generic notifications to millions** —
*"Open a Demat Account!"* or *"EMI due in 2 days."* These messages are blind, one-way, and
impersonal. **98% of customers ignore them.** This is broadcasting, not engagement — and it's
why banking apps feel like spam while digital engagement keeps falling.

> Built for the **SBI Hackathon @ GFF 2026** — Theme: *Agentic AI for Customer Acquisition,
> Digital Adoption & Digital Engagement.*

---

## 💡 Our Solution

**FinPulse** is an **Agentic AI money buddy** named *Pulse* that studies each customer's actual
financial behaviour, then **autonomously reasons, decides, and acts** — speaking only when it can
genuinely help, and intelligently **staying silent** when a message would be irrelevant.

Unlike rule-based reminder systems, Pulse **connects multiple data points** (salary, spending,
balance, goals, life events) to make smart, human-like decisions.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🤖 **Autonomous Agent** | Monitors, decides & acts on its own — no user prompt needed |
| 🤫 **Smart Silence** | ML-powered relevance filter that knows when NOT to message |
| 📊 **Churn Prediction** | ML model flags at-risk customers for proactive re-engagement |
| 💯 **Money Health Score** | Gamified 0–100 score that improves with good habits |
| 🤔 **What-If Simulator** | "Can I afford this?" → instant cash-flow impact |
| 🎙️ **Voice + Local Language** | Hindi/Punjabi/Tamil support via Whisper |
| 👆 **One-Tap Actions** | Every suggestion is a single tap — zero friction |
| 📅 **Weekly Money Story** | A Sunday recap, like Spotify Wrapped for your money |

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
[AI ORCHESTRATOR — LangGraph]
            │
            ▼
[PULSE AGENT (LLM + Memory)] — reasons, personalizes, plans action
            │
            ▼
[TOOL LAYER] — Notifications | Auto-Pay | Move Funds | Recommender
            │
            ▼
[CUSTOMER] — gets a relevant one-tap nudge (or silence)
            │
            ▼
[MEMORY (Vector DB)] → [BANK DASHBOARD — analytics]
```

---

## 🛠️ Tech Stack

- **Agentic AI:** LangChain / LangGraph, OpenAI GPT-4o
- **Machine Learning:** scikit-learn (churn prediction, relevance filter)
- **Backend:** Python, FastAPI
- **Frontend:** Streamlit (prototype), React.js (dashboard)
- **Memory:** ChromaDB (vector store / RAG)
- **Voice:** OpenAI Whisper
- **Database:** PostgreSQL, MongoDB
- **Infra:** AWS / Docker, OAuth 2.0, AES-256 (RBI & DPDP 2023 compliant)

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.10+
```

### Installation
```bash
# Clone the repo
git clone https://github.com/GitWithEkam/FinPulse-Agentic-AI-for-Proactive-Banking-Engagement/
cd finpulse-agentic-ai

# Install dependencies
pip install -r requirements.txt

# (Optional) Add your OpenAI API key
export OPENAI_API_KEY="your-key-here"

# Run the app
streamlit run finpulse_demo.py
```

### requirements.txt
```
streamlit
openai
pandas
scikit-learn
numpy
```

---

## 📂 Project Structure
```
finpulse-agentic-ai/
├── finpulse_demo.py        # Main Streamlit app
├── churn_model.py          # ML churn-prediction module
├── requirements.txt
├── assets/                 # Screenshots & demo images
└── README.md
```

---

## 🎥 Demo

- 📹 **Video Demo:** [YouTube Link](https://youtu.be/your-demo-link)
- 📊 **Pitch Deck:** [View Deck](link-to-deck)

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



---

> ⭐ *FinPulse — turning passive, spammy banking apps into a money buddy people actually love.*
