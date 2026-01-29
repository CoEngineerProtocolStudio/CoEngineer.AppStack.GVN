

# Co-engineer Protocol Kit (v0.1)

A repeatable incubation protocol and technical stack designed to help studios embed execution support into daily work and compound collective intelligence across cohorts.

## 🧠 The Co-engineer Philosophy

The Kit implements the **Builder Stack**, a ritual system comprising two engines:

1. **Epiphany Engine (See the leverage):** A structured reflection ritual for discovering what's working and what's stuck.
2. **Quick Turn Stack (Build from it):** A support layer turning insights into launchable actions (tasks, experiments, SOPs) using the **Co-engineer AI Companion** and the **Studio Thesis**.

## 🏛 Project Structure

```text
co-engineer-protocol-kit/
├── README.md                # Project Overview
├── BUILDER_STACK.md         # Ritual system & rhythms
├── PROTOCOL.md              # Core logic & compounding
├── CUSTODIAN_GUIDE.md       # Rhythms for Studio Custodians
├── STUDIO_THESIS_TEMPLATE.md # Tech + Econ templates
│
├── kit/                     # Core Logic (The Package)
│   ├── src/coengineer/      # RAG Engine & Config
│   ├── prompts/             # Daily, Weekly, & Distillation Packs
│   └── workflows/           # Ritual checklists
│
├── reference-implementation/# Technical Wiring
│   ├── ingestion/           # Vertex AI RAG syncing
│   └── ui/                  # Streamlit embedding
│
└── examples/                # Vertical Implementations
    └── oyster-mushroom/     # Reference Studio

```

## 🛠 Technical Stack: The Co-engineer Builder

The kit provides a modular Python package (`coengineer-appstack-gvn`) as the technical backbone:

* **Engine:** Gemini 2.0 Flash.
* **Retrieval:** Native Vertex AI RAG integration.
* **Context Handling:** Specialized mapping for stateful, grounded consultations.

### Installation

```bash
pip install -e ./kit --break-system-packages

```

## 🚀 Deployment & Releases

Automated via GitHub Actions.

* **Tags:** Pushing a version tag (e.g., `v0.1.0`) triggers a GitHub Release.
* **Artifacts:** Includes compiled Python wheel and protocol documentation.

---

**Lead Developer:** Min Thu Khaing Min Bhone Shan
---
**Organization:** Riverlach Protocol lab Studio
