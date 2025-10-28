# 🧠 Agentic AI — Research-to-Article Pipeline  

## 📘 Overview  

This project demonstrates a **multi-agent AI system (Agentic AI)** designed to perform an end-to-end **research-to-article pipeline**.  
It automates the process of topic research, article writing, and critique using specialized AI agents that collaborate intelligently to generate refined, high-quality content.  

The objective is to simulate a **self-improving autonomous workflow**, where multiple agents work together to produce factually grounded and coherent articles with minimal human input.  

**🔗 GitHub Repository:** [https://github.com/SmdAthahar/Agentic_AI_demo_project](https://github.com/SmdAthahar/Agentic_AI_demo_project)  

---

## ⚙️ Architecture  

### 🧩 System Flow  


---

## 🧠 Components  

### 🧭 Orchestrator (`orchestrator.py`)
- Acts as the central controller.  
- Takes topic input from the user.  
- Sequentially triggers all three agents.  
- Logs and saves the final article in `/outputs/final_article.txt`.  
- Can run improvement loops between **Writer** and **Critic** agents if enabled.  

---

### 🔍 ResearchAgent (`agents/researchagent.py`)
- Uses **Wikipedia API** and web scraping to gather topic-related insights.  
- Summarizes **4–6 credible sources** with URLs and short explanations.  
- Returns structured data for downstream processing.  

---

### ✍️ WriterAgent (`agents/writeragent.py`)
- Uses **OpenAI’s GPT-4o-mini model** via the latest `openai>=1.0.0` SDK.  
- Converts research snippets into a **700–1200 word article** with citations.  
- Employs structured prompt engineering for clarity and coherence.  

---

### 🧩 CriticAgent (`agents/criticagent.py`)
- Serves as an **AI editor** that evaluates and improves drafts based on:
  - Factual accuracy  
  - Flow and coherence  
  - Tone and style  
  - Citation consistency  
- Produces both a **critique summary** and an **improved article version**.  

---

### ⚙️ Utilities
- **Logger (`utils/logger.py`)** — Handles detailed logs with timestamps.  
- **Outputs folder** — Stores all intermediate and final results.  

---

## 💡 Design Decisions  

### 1️⃣ Agentic Workflow  
The architecture follows a **pipeline-based agent orchestration** pattern:  
1. **Research Agent** gathers factual data.  
2. **Writer Agent** generates structured drafts.  
3. **Critic Agent** refines and validates output.  

This modular separation ensures flexibility and reusability of each agent.  

---

### 2️⃣ Language Model & API  
- **Model:** `gpt-4o-mini` (optimized for reasoning and efficiency)  
- **SDK:** `openai>=1.0.0`  
- **Future Scope:** Integrate **Retrieval-Augmented Generation (RAG)** for real-time factual grounding.  

---

### 3️⃣ Logging & Transparency  
Each stage (topic entry → research → drafting → critique → completion) is timestamped in logs, ensuring **traceability and reproducibility**.  

---

### 4️⃣ Gradio Integration  
A user-friendly **Gradio interface (`app.py`)** is included:  
- Accepts user topic input.  
- Displays:
  - Research sources  
  - Drafted article  
  - Critique summary  
  - Improved final version  
- Automatically saves the final output to `/outputs/final_article.txt`.  

---

## 🧰 Implementation Details  

### 🧪 Environment Setup
```bash
conda create -n venv python=3.10
conda activate venv
pip install -r requirements.txt
