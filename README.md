<!-- Animated Header -->
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=28&duration=3000&color=8A2BE2&center=true&vCenter=true&width=950&lines=LangGraph+Workflow+Engineering;Stateful+LLM+Systems+%7C+RAG+%7C+HITL+%7C+Agents;Graph-Based+Execution+Architecture" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/LangGraph-Stateful_Workflows-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LangChain-Integrated-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RAG-Graph_Driven-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/HITL-Implemented-critical?style=for-the-badge" />
</p>

---

# 🧠 LangGraph Workflow Engineering

Structured implementation of **LangGraph-based LLM systems** covering sequential, parallel, conditional, iterative, and stateful workflows.

This repository demonstrates:

- Controlled graph execution  
- Deterministic routing  
- State management  
- Tool integration  
- RAG pipelines  
- Human-in-the-loop systems  

Each workflow is implemented independently and then composed into larger agentic systems.

---

# ⚙️ Graph Execution Model

### Directed Graph Flow

```
State
   ↓
Node Execution
   ↓
State Update
   ↓
Edge Routing (Conditional / Parallel / Loop)
   ↓
Next Node
```

LangGraph enables:

- Stateful execution  
- Deterministic routing  
- Controlled recursion  
- Interruptible workflows  
- Persistent checkpointing  

---

# 📂 Project Architecture

```
LangGraph/
│
├── 01. Sequential Workflow
├── 02. Parallel Workflow
├── 03. Conditional Workflow
├── 04. Iterative Workflow
├── 05. Chatbot
├── 06. Persistent
├── 07. Chatbot_with_UI_Streamlite
├── 08. Chatbot_with_tool_calling
├── 09. RAG
├── 10. HITL
├── 11. Subgraphs
├── 12. Blog Writing Agent
│
├── requirements.txt
└── README.md
```

---

# 🧩 Implemented Workflows

---

## 1️⃣ Sequential Workflow

📁 `01. Sequential Workflow/`

- Node-to-node execution  
- Prompt chaining  
- LLM chaining  
- Structured output parsing  
- Category classification  

Linear graph execution.

---

## 2️⃣ Parallel Workflow

📁 `02. Parallel Workflow/`

- Concurrent node execution  
- Cricket summarization  
- Essay evaluation  
- Independent task aggregation  

Parallel branch merging into shared state.

---

## 3️⃣ Conditional Workflow

📁 `03. Conditional Workflow/`

- Sentiment-based branching  
- Fitness tracking logic  
- Dynamic edge routing  
- State-driven decisions  

Model output determines next execution path.

---

## 4️⃣ Iterative Workflow

📁 `04. Iterative Workflow/`

- Controlled loops  
- Retry mechanisms  
- Refinement cycles  
- Recursion until condition satisfied  

Implements loop-based graph transitions.

---

## 5️⃣ Stateful Chatbot

📁 `05. Chatbot/`

- Graph-based conversation engine  
- Context preservation  
- State transitions  
- Memory node handling  

Conversation history maintained inside graph state.

---

## 6️⃣ Persistent Workflows

📁 `06. Persistent/`

- SQLite checkpointing  
- Long-term state storage  
- Resume execution capability  
- Durable graph sessions  

Supports recovery and continuation.

---

## 7️⃣ Streamlit Chatbot UI

📁 `07. Chatbot_with_UI_Streamlite/`

- Backend + frontend separation  
- Streaming responses  
- SQLite DB integration  
- Thread-based session resumption  

Production-style interface over LangGraph backend.

---

## 8️⃣ Tool Calling Workflow

📁 `08. Chatbot_with_tool_calling/`

- LLM + Tools integration  
- Tool execution routing  
- Controlled invocation logic  
- Backend/Frontend separation  

Graph manages tool execution deterministically.

---

## 9️⃣ Retrieval-Augmented Generation (RAG)

📁 `09. RAG/`

- Graph-driven RAG pipeline  
- Chroma vector store  
- Embedding-based retrieval  
- Context injection  
- Stateful retrieval flow  

```
Query
   ↓
Retriever Node
   ↓
Context Injection
   ↓
LLM Node
   ↓
Grounded Response
```

---

## 🔟 Human-In-The-Loop (HITL)

📁 `10. HITL/`

- Manual approval nodes  
- Interrupt → review → resume flow  
- Tool execution approval  
- Controlled agent behavior  

Graph pauses until human validation.

---

## 1️⃣1️⃣ Subgraphs

📁 `11. Subgraphs/`

- Modular workflow composition  
- Invoking subgraphs  
- Node abstraction  
- Reusable graph components  

Supports scalable graph design.

---

## 1️⃣2️⃣ Blog Writing Agent

📁 `12. Blog Writing Agent/`

- Multi-step content pipeline  
- Structured static blog generation  
- Section-wise drafting  
- Controlled execution flow  

Agentic content generation using graph orchestration.

---

# 🛠 Tech Stack

- Python  
- LangGraph  
- LangChain  
- Streamlit  
- ChromaDB  
- SQLite  
- OpenAI / LLM APIs  
- Prompt Engineering  
- Vector Embeddings  

---

# 🔬 Key Concepts Demonstrated

- State management using `TypedDict`  
- Directed graph execution  
- Conditional edge routing  
- Loop control mechanisms  
- Persistent checkpointing  
- Tool invocation control  
- Graph-based RAG  
- HITL interruption handling  
- Subgraph modularization  
- Production-ready UI integration  

---

# 🚀 How to Run

### Clone repository

```bash
git clone <repo-url>
cd LangGraph
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run frontend.py
```

---

# 🎯 What This Project Demonstrates

- Controlled graph-based LLM execution  
- Transition from linear chains → stateful workflows  
- Deterministic agent design  
- Interruptible execution pipelines  
- Persistent AI systems  
- End-to-end workflow engineering  

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:3A1C71,100:D76D77&height=120&section=footer"/>
</p>

---

# 👩‍💻 Author

**Sakshi Shimpi**  
AI/ML Engineer  

Focused on structured, controllable, production-grade LLM systems.