# CodeLens

# 🧠 Context-Aware Documentation Generator

An intelligent system that **automatically generates high-quality, modular, and context-aware documentation** by deeply analyzing a project's codebase.

Unlike traditional doc generators, this system understands **code structure, intent, and changes over time** using AST parsing, semantic diffing, and LLMs.

---

## 🚀 Core Idea

This is not just a documentation tool — it is an **AI-powered developer assistant** that:

* 📂 Parses code intelligently using AST
* 🔄 Detects meaningful code changes (semantic diff)
* 🧠 Generates human-like documentation using LLMs
* 🔍 Indexes knowledge into a vector database
* 💬 Answers queries using a RAG (Retrieval-Augmented Generation) system

---

## ✨ Key Features

* 📤 Upload project as ZIP or connect GitHub via OAuth
* 🧩 Automatic parsing of:

  * Modules
  * Classes
  * Functions
* 🧠 Context-aware docstring generation
* 📘 Modular documentation per component/service
* 📄 Auto-generation of `README.md` with:

  * Setup instructions
  * Usage examples
  * API documentation
* 🔄 Semantic diff engine for tracking meaningful code changes
* 🔍 Intelligent query answering (RAG system)
* 🚀 Option to push generated docs back to GitHub

---

## 🏗️ System Architecture

```
        ┌──────────────┐
        │  Frontend UI │
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │   FastAPI    │
        │  Backend     │
        └──────┬───────┘
               │
   ┌───────────▼───────────┐
   │ Code Processing Layer │
   │ (Tree-sitter + AST)   │
   └───────────┬───────────┘
               │
   ┌───────────▼───────────┐
   │ Semantic Diff Engine  │
   │ (GitPython + AST)     │
   └───────────┬───────────┘
               │
   ┌───────────▼───────────┐
   │     LLM Engine        │
   │ (OpenAI / Claude)     │
   └───────────┬───────────┘
               │
   ┌───────────▼───────────┐
   │ Vector DB (RAG Layer) │
   │ (FAISS / Pinecone)    │
   └───────────────────────┘
```

---

## 🧩 Tech Stack

### ⚙️ Backend

* FastAPI (async, high performance)
* Python

### 🧠 AI/LLM

* OpenAI (GPT-4 / GPT-4o) OR Anthropic Claude

### 🔍 Code Parsing

* Tree-sitter (Python + JavaScript support)
* AST-based structure extraction

### 🔄 Semantic Diff

* GitPython
* AST comparison for meaningful change detection

### 📦 Storage & Retrieval

* FAISS / Pinecone (Vector Database)
* Enables RAG-based intelligent answers

### 🔐 Integrations

* GitHub OAuth (repo access)
* Optional push-back of generated docs

---

## ⚡ How It Works

1. 📥 User uploads ZIP or connects GitHub repo
2. 🔍 Backend parses code using Tree-sitter
3. 🧠 Extracts:

   * Functions
   * Classes
   * Dependencies
4. 🔄 Semantic diff detects meaningful changes
5. ✨ LLM generates:

   * Docstrings
   * README
   * Code explanations
6. 📦 Data indexed into vector DB
7. 💬 User can query codebase using RAG

---




## 🛠️ Installation

```bash
git clone https://github.com/your-username/context-doc-generator.git
cd context-doc-generator

pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📡 API Endpoints

| Method | Endpoint       | Description              |
| ------ | -------------- | ------------------------ |
| POST   | /upload        | Upload ZIP project       |
| POST   | /analyze       | Parse & analyze codebase |
| POST   | /generate-docs | Generate documentation   |
| GET    | /docs          | View generated docs      |

---

## 🔮 Future Enhancements

* 🌐 Multi-language support (Java, C++)
* 🤖 Fine-tuned LLM for code understanding
* 📊 Documentation quality scoring
* 🧪 Test case generation
* 🔁 CI/CD integration (auto doc updates)

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork and improve 🚀

---

## 📄 License

MIT License

---

## 👩‍💻 Author

**Rakshita Handage**
📍 Belagavi, India
🔗 GitHub | LinkedIn






## 🌐 Live Demo

🔗 https://hackthon-frontend-gamma.vercel.app

