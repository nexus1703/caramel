# Caramel

**Caramel is a contextual multi-agent orchestrator.**  
It routes queries via Redis and a vector store, dynamically loads the relevant corpus, weights source reliability/bias, preserves all hypotheses, supports user HITL arbitration, and can generate visual reasoning graphs on demand.

---

## ✨ Features
- Context-aware orchestration with a pinned analysis agent
- Progressive corpus loading (L0 → L3) from Redis/vector store
- Source reliability & bias scoring
- Hypothesis preservation (no discarded paths)
- Human-in-the-loop (HITL) arbitration for biased/contradictory sources
- On-demand visual reasoning graphs

---

## 📦 Architecture
- **Orchestrator** → routes requests, manages context
- **Pinned Analysis Agent** → intent classification & corpus plan
- **Specialized Agents** (on demand) → legal, daily, intimate, geo, etc.
- **Redis (hot context)** + **Vector Store (cold context)** → layered memory
- **HITL loop** → user decides when sources conflict

---

## 🚀 Getting Started
```bash
# clone repository
git clone https://github.com/yourname/caramel.git
cd caramel

# install dependencies
pip install -r requirements.txt

# run orchestrator
python caramel.py

