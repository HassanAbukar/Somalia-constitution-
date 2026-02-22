#  Somalia Constitution RAG Chatbot

A local Retrieval-Augmented Generation (RAG) system built using:

- Memvid (AI memory storage)
- Ollama (local LLM)
- Python

This project allows users to ask questions about the Constitution of Somalia and receive answers grounded strictly in the official document.

---

## 🧠 How It Works

1. The Constitution PDF is processed and converted into an AI memory file (`constitution.mp4`) using Memvid.
2. When a user asks a question:
   - Relevant sections are retrieved from memory.
   - The context is sent to a local LLM (via Ollama).
   - A grounded answer is generated.

---

## 📂 Project Structure

```
data/            → Constitution PDF  
memory/          → Generated AI memory files  
src/             → Ingest & Chat scripts  
```

---

## 🚀 Setup

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Build memory (run once)

```bash
python src/ingest.py
```

### 3️⃣ Start chatbot

Make sure Ollama is running:

```bash
ollama run llama3
```

Then:

```bash
python src/chat.py
```

---

## 🔒 Privacy

- Runs fully local
- No OpenAI API required
- No external data sharing

---

## ⚡ Future Improvements

- Web interface
- Article number citations
- Faster indexing optimization

## Data Setup

1. Place the constitution.mp4 and index.json file inside the /data folder
2. Then Run:
   python ingest.py