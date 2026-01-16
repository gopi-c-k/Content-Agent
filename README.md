# 🤖 Content-Agent

> A modular, LLM-driven content generation agent that analyzes historical Medium-style article metrics, plans new articles, generates drafts, critiques and iterates on them, and saves high-quality final outputs.

**Content-Agent** is designed for researchers, writers, and engineers who want a **reproducible, inspectable content pipeline** powered by large language models.  
The system emphasizes **clear modular responsibilities**, **iterative quality control**, and **traceable run metadata**.

---

## 🚀 What This Project Solves

This project automates the end-to-end content ideation and drafting process by:

- Analyzing historical article performance data
- Selecting topics and planning article structure
- Generating sectioned drafts using an LLM
- Iteratively critiquing and rewriting drafts until quality thresholds are met
- Persisting run metadata and final articles for reproducibility

The full agent loop is orchestrated in:

```

agent/agent_loop.py

```

---

## 🎯 Target Users & Use Cases

### Content Teams
- Automate topic selection and article drafting
- Maintain consistent writing quality at scale

### Engineers
- Prototype LLM-based writing or planning agents
- Experiment with critique-and-rewrite loops

### Researchers
- Study iterative LLM critique strategies
- Evaluate rule-based + LLM hybrid quality signals

---

## 🧠 Core Design Philosophy

- **Single-responsibility modules**
  - Observe → Analyze → Plan → Write → Critique → Remember
- **Centralized LLM caller**
  - Consistent API usage and credential handling
- **Hybrid critique**
  - Rule-based scoring + LLM-based evaluation
- **Minimal external surface**
  - JSON-based persistence for transparency and reproducibility
- **Composable architecture**
  - Individual modules are easy to test, replace, or extend

---

## 🏗 System Architecture

![Architecture Diagram](utils/ContentGenerationArchitecture.png)

The system consists of the following components:

- **Observer**
  - Reads historical article data (`data/medium_history.json`)
- **Analyzer**
  - Computes topic statistics and insights
- **Planner**
  - Selects topic, angle, and article blueprint
- **Writer**
  - Generates sectioned content using an LLM
- **Critic**
  - Scores drafts and requests rewrites until quality thresholds are met
- **Memory**
  - Records run results (`data/agent_memory.json`)
- **LLM Utils**
  - Centralized LLM client wrapper using the Groq SDK

The centralized LLM integration lives in:

```

utils/llm.py

````

and expects a `GROQ_API_KEY` from environment variables.

---

## 🧩 Major Modules & Responsibilities

### Core Agent Pipeline

- **agent/agent_loop.py**
  - Orchestrates the full run lifecycle

- **agent/observer.py**
  - Loads and validates historical JSON data

- **agent/analyzer.py**
  - Computes topic statistics and insights

- **agent/planner.py**
  - Chooses topic and builds article plan

- **agent/writer.py**
  - Generates section content via LLM calls

- **agent/critic.py**
  - Scores drafts and manages rewrite loops

- **agent/llm_critic.py**
  - Uses a dedicated LLM prompt to produce structured JSON evaluations

- **agent/memory.py**
  - Loads and saves run metadata

### Utilities

- **utils/llm.py**
  - Central LLM client using Groq SDK
- **utils/scoring.py**
  - Rule-based text scoring
- **utils/sanitize.py**
  - Text cleanup and normalization

---

## 🔄 How Data Flows Through the System

1. **Observer**
   - Reads `data/medium_history.json`

2. **Analyzer**
   - Computes insights:
     - Best topics
     - Ideal article length
     - Under-explored topics

3. **Planner**
   - Combines insights with agent memory
   - Chooses topic and article blueprint

4. **Writer**
   - Generates section text via LLM calls
   - Combines sections into a draft

5. **Critic**
   - Scores draft (rule-based + LLM JSON evaluation)
   - Requests rewrites until quality threshold or max attempts

6. **Memory**
   - Records run metadata
   - Final article written to `output/final_article.md`

---

## 📦 Project Structure

```txt
agent/
 ├── agent_loop.py
 ├── observer.py
 ├── analyzer.py
 ├── planner.py
 ├── writer.py
 ├── critic.py
 ├── llm_critic.py
 └── memory.py

data/
 ├── medium_history.json
 └── agent_memory.json

output/
 └── final_article.md

scripts/
 ├── run_agent.py
 ├── test_observer.py
 ├── test_analyzer.py
 ├── test_planner.py
 ├── test_writer.py
 ├── test_critic.py
 └── test_llm.py

utils/
 ├── llm.py
 ├── scoring.py
 └── sanitize.py

requirements.txt
README.md
````

This layout groups code **by responsibility**, making the pipeline easy to inspect and extend.

---

## 🧠 Core Logic & Key Files

* **agent/agent_loop.py**

  * Primary entrypoint for a full run

* **utils/llm.py**

  * Centralizes LLM provider integration and credentials

* **agent/writer.py**

  * Defines section prompts and article structure

* **agent/critic.py / agent/llm_critic.py**

  * Implements scoring, rewrite loops, and escalation logic

* **agent/memory.py**

  * Persists run metadata to guide future planning

* **data/medium_history.json**

  * Required input data for analysis and planning

---

## 🔌 Public Interfaces

This repository exposes **no HTTP API**. Public interfaces are Python module functions:

* `agent.agent_loop.run_agent()`
* `utils.llm.call_llm(prompt, model, temperature)`
* `agent.observer.observe()`
* `agent.planner.plan(insights)`
* `agent.writer.write(plan)`
* `agent.critic.critique(article)`

### Inputs & Outputs

* **Inputs:** JSON files and Python dicts
* **Outputs:** Markdown article files
* **Side Effects:**

  * External LLM API calls
  * JSON writes to agent memory
  * File writes to `output/`

---

## ▶️ Setup & Run Instructions

### 1. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate        # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=sk-xxxx
```

The key is loaded automatically via `python-dotenv`.

---

### 4. Provide Input Data

Populate `data/medium_history.json`:

```json
[
  {
    "title": "Example post",
    "topic": "system design",
    "length": 1200,
    "views": 2000,
    "reads": 300,
    "claps": 50
  }
]
```

---

### 5. Run the Agent

```bash
python scripts/run_agent.py
```

Outputs:

* `output/final_article.md`
* Updated `data/agent_memory.json`

---

## 🧪 Optional: Run Module Tests

```bash
python scripts/test_observer.py
python scripts/test_analyzer.py
python scripts/test_planner.py
python scripts/test_writer.py
python scripts/test_critic.py
python scripts/test_llm.py
```

---

## 👤 Author

**[Gopi C K](https://github.com/gopi-c-k)**

---

⭐ If you’re exploring LLM agents, critique loops, or reproducible content pipelines, consider starring the repo.
