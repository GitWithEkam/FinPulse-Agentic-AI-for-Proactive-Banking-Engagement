# pulse_agent.py
# ---------------------------------------------------------------------------
# FinPulse — The "Pulse" Agentic AI brain
# ---------------------------------------------------------------------------
# This module contains the autonomous logic:
#   1. EVENT DETECTOR    -> scans transactions/profile for meaningful triggers
#   2. SMART SILENCE      -> decides IF each event is worth a message
#   3. PULSE AGENT        -> writes a friendly, personalized, one-tap message
#
# It works with OR without an OpenAI key. If a key is present it uses GPT-4o
# for natural language; otherwise it falls back to high-quality templated
# responses so the demo ALWAYS works offline.
# ---------------------------------------------------------------------------

import os

# --- Optional OpenAI import (demo runs fine without it) --------------------
try:
    from openai import OpenAI
    _OPENAI_AVAILABLE = True
except Exception:
    _OPENAI_AVAILABLE = False


# ===========================================================================
# 1. EVENT DETECTOR  — Pulse monitors behaviour WITHOUT being asked
# ===========================================================================
def detect_events(transactions, customer: dict) -> list:
    """Return a list of event dicts: {id, priority, text}."""
    events = []

    # Idle money sitting in savings
    if customer["idle_amount"] > 20_000 and customer["idle_months"] >= 2:
        events.append({
            "id": "idle_money",
            "priority": "high",
            "text": (f"₹{customer['idle_amount']:,} has been idle for "
                     f"{customer['idle_months']} months earning only ~3%."),
        })

    # High weekly spending
    spend = transactions.loc[transactions["category"] == "Spend", "amount"].sum()
    if spend > 20_000:
        events.append({
            "id": "high_spend",
            "priority": "medium",
            "text": f"High spending this week: ₹{int(spend):,}.",
        })

    # EMI vs salary timing risk
    if "EMI Due (10th)" in transactions["type"].values:
        events.append({
            "id": "emi_timing",
            "priority": "high",
            "text": "EMI is due on the 10th, but salary credits on the 5th — timing to watch.",
        })

    # No savings / investment plan
    if not customer.get("savings_account", False):
        events.append({
            "id": "no_savings",
            "priority": "medium",
            "text": "No savings or investment plan set up yet.",
        })

    # A deliberately IRRELEVANT promo event — Smart Silence should drop this
    events.append({
        "id": "generic_promo",
        "priority": "low",
        "text": "Generic promo: open a new Demat account (mass-marketing blast).",
    })

    return events


# ===========================================================================
# 2. SMART SILENCE  — the anti-spam relevance filter
# ===========================================================================
def smart_silence_filter(events: list, churn_risk: float) -> tuple:
    """
    Decide which events actually deserve a message.
    Returns (kept_events, skipped_events).

    Rules:
      * Generic mass-marketing blasts are ALWAYS dropped.
      * If the customer is healthy (low churn risk), low-priority nudges are
        suppressed too — a healthy, engaged user shouldn't be pestered.
    """
    kept, skipped = [], []
    for e in events:
        is_generic = "generic" in e["id"] or "promo" in e["id"]
        low_value_for_healthy = (e["priority"] == "low" and churn_risk < 30)

        if is_generic or low_value_for_healthy:
            skipped.append(e)
        else:
            kept.append(e)
    return kept, skipped


# ===========================================================================
# 3. PULSE AGENT  — turns events into friendly, one-tap messages
# ===========================================================================
_TEMPLATES = {
    "idle_money": ("💰 Hey {name}! ₹{idle:,} has been sitting idle for {months} "
                   "months earning just 3%. Want 3 safe ways to grow it?",
                   "Show me safe options"),
    "high_spend": ("📊 You've spent a bit more than usual this week. Want a quick "
                   "look at where it went? No judgement 😊",
                   "See my budget"),
    "emi_timing": ("⏰ Heads up {name} — your EMI is due on the 10th but salary "
                   "arrives on the 5th. Want me to line up auto-pay so you're safe?",
                   "Set auto-pay"),
    "no_savings": ("🏆 You don't have a savings plan yet. Want to start a tiny one? "
                   "Takes 60 seconds and I'll handle the rest.",
                   "Start saving"),
}


def _templated_messages(events, customer):
    out = []
    for e in events:
        tmpl, action = _TEMPLATES.get(
            e["id"],
            ("ℹ️ {name}, I noticed something worth a quick look.", "Tell me more"),
        )
        msg = tmpl.format(
            name=customer["name"],
            idle=customer["idle_amount"],
            months=customer["idle_months"],
        )
        out.append({"message": msg, "action": action})
    return out


def pulse_agent(events, customer, use_llm=True):
    """
    Generate personalized messages for the kept events.
    Tries GPT-4o if a key is available; otherwise uses templates.
    Returns a list of {message, action} dicts.
    """
    if not events:
        return []

    api_key = os.getenv("OPENAI_API_KEY")
    if use_llm and _OPENAI_AVAILABLE and api_key:
        try:
            client = OpenAI(api_key=api_key)
            event_lines = "\n".join(f"- {e['text']}" for e in events)
            prompt = (
                f"You are 'Pulse', a warm, friendly autonomous banking money-buddy "
                f"for {customer['name']} (balance ₹{customer['balance']:,}).\n"
                f"For EACH event below, write ONE short caring message (max 2 lines) "
                f"and a one-tap action label in [square brackets]. Never be salesy.\n\n"
                f"Events:\n{event_lines}"
            )
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
            )
            text = resp.choices[0].message.content.strip()
            # Return as a single block; UI will render it.
            return [{"message": text, "action": None}]
        except Exception:
            pass  # fall through to templates

    return _templated_messages(events, customer)
