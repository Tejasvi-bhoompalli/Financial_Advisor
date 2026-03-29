# FINANCIAL ADVISOR AND EXPENSE MANAGER AI AGENT
💰 Financial Advisor AI Agent

📌 Overview

This project is an AI-powered Financial Advisor Agent that provides personalized financial guidance using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

The agent can analyze financial queries, retrieve relevant knowledge, and generate intelligent recommendations for budgeting, saving, and investing.

---

🚀 Features

- 🤖 AI Agent using LLM
- 📊 Financial analysis & suggestions
- 🔍 RAG-based knowledge retrieval
- 🧮 Custom tools (calculator, finance logic)
- 💬 Natural language interaction

---

🧠 Tech Stack

- Python
- LangChain / LLM APIs (Gemini / Groq / OpenAI)
- ChromaDB / FAISS (Vector Database)
- Streamlit (if UI used)

---

⚙️ How It Works

1. User asks a financial question
2. Agent retrieves relevant data using RAG
3. LLM processes the query
4. Tools are used if required
5. Final answer is generated

---

▶️ Run Locally

pip install -r requirements.txt
python app.py

---

📂 Project Structure

financial-advisor-agent/
│
├── app.py                  # Main application (entry point)
├── agent.py                # AI agent logic (LLM + RAG)
├── tools.py                # Custom tools (calculator, finance logic)
├── prompts.py              # Prompt templates for LLM
├── config.py               # Configuration & API keys
│
├── data/                   # Financial datasets
│   └── sample_data.csv
│
├── vectorstore/            # Chroma / FAISS database for RAG
│
├── docs/                   # Project documentation
│   └── financial_advisor.pdf
│
├── assets/                 # Images / screenshots
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .env                    # Environment variables

🔍 Description

- app.py: Runs the application interface
- agent.py: Handles AI reasoning and decision-making
- tools.py: Contains utility functions for financial calculations
- prompts.py: Stores prompt templates used by the LLM
- config.py: Manages API keys and configuration settings
- vectorstore/: Stores embeddings for retrieval (RAG)
- data/: Contains datasets used in the project
- docs/: Includes project documentation and reports
- assets/: Stores images and screenshots for README
---
🔮 Future Improvements

- Real-time stock market integration
- Portfolio optimization
- Voice-based assistant

---

Team

1.Tejasvi Bhoompalli
2.A Likitha

