# 🎥 AI Video Assistant

> Turn long-form videos into structured, searchable knowledge using Speech AI, Generative AI, and Retrieval-Augmented Generation.

AI Video Assistant is an end-to-end AI system that takes a **YouTube video or local media file**, transcribes it using **Whisper**, extracts key insights using **LLMs**, and builds a **RAG-powered conversational layer** so users can ask questions directly about the content.

Instead of manually watching a long video, the system converts it into:

- 📌 A meaningful title
- 📝 A concise summary
- ✅ Action items
- 🔑 Key decisions
- ❓ Open questions
- 💬 A searchable AI chat experience

---

## ✨ Why This Project?

Long-form videos contain valuable information, but extracting useful insights from them is time-consuming.

AI Video Assistant converts unstructured audio/video content into a structured knowledge layer by combining:

```text
Speech Recognition
        +
LLM Orchestration
        +
Information Extraction
        +
Vector Search
        +
Retrieval-Augmented Generation
```

The result is an AI-powered assistant capable of understanding, summarizing, structuring, and answering questions about video content.

---

# 🚀 Core Features

### 🎬 YouTube & Local Media Support

Accepts:

```text
YouTube URL
     OR
Local Media File
```

The system automatically extracts and prepares the audio for processing.

---

### 🎙️ AI-Powered Transcription

Uses **OpenAI Whisper** to convert audio into text.

```text
Video
  ↓
Audio Extraction
  ↓
Audio Chunking
  ↓
Whisper
  ↓
Transcript
```

Supports long-form content by breaking audio into manageable chunks before transcription.

---

### 🧠 Intelligent Summarization

Long transcripts are divided into smaller sections and summarized using a **map-reduce style LLM workflow**.

```text
Full Transcript
      ↓
Text Chunking
      ↓
┌──────────┬──────────┬──────────┐
│ Chunk 1  │ Chunk 2  │ Chunk 3  │
└────┬─────┴────┬─────┴────┬─────┘
     ↓          ↓          ↓
 Summary 1   Summary 2   Summary 3
     └──────────┬──────────┘
                ↓
        Final LLM Summary
```

This makes it possible to handle transcripts larger than a single model context window.

---

### ✅ Action Item Extraction

Automatically identifies actionable tasks from the transcript.

Example:

```text
1. Task: Complete backend integration
   Owner: Rahul
   Deadline: Friday

2. Task: Review final product flow
   Owner: Product Team
   Deadline: Not specified
```

---

### 🔑 Key Decision Extraction

Extracts important decisions made during the discussion so the user can understand the outcome without reading the entire transcript.

---

### ❓ Open Question Detection

Identifies unresolved questions, pending discussions, and areas requiring follow-up.

---

# 💬 Chat With Your Video

The project builds a complete **Retrieval-Augmented Generation pipeline** over the video transcript.

Users can ask questions such as:

```text
"What were the main decisions?"

"Who is responsible for deployment?"

"What did the speaker say about AI?"

"Were any deadlines mentioned?"
```

The assistant retrieves relevant sections of the transcript and generates an answer grounded only in that context.

---

# 🔍 RAG Architecture

```text
                     User Question
                           │
                           ▼
                       Retriever
                           │
                           ▼
                 Semantic Similarity Search
                           │
                           ▼
                 Top Relevant Transcript Chunks
                           │
                           ▼
                 ┌──────────────────────┐
                 │ Context + Question   │
                 └──────────┬───────────┘
                            │
                            ▼
                           LLM
                            │
                            ▼
                     Grounded Answer
```

The system is instructed to avoid answering when relevant information cannot be found in the transcript.

---

# 🧩 End-to-End Architecture

```text
                        ┌──────────────────────┐
                        │   YouTube / File     │
                        └──────────┬───────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │   Audio Processing   │
                        │ yt-dlp + FFmpeg      │
                        └──────────┬───────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │       Whisper        │
                        │   Speech → Text      │
                        └──────────┬───────────┘
                                   │
                                   ▼
                             Transcript
                                   │
                  ┌────────────────┴────────────────┐
                  │                                 │
                  ▼                                 ▼
        ┌──────────────────┐              ┌──────────────────┐
        │  LLM Processing  │              │   Vector Store   │
        │                  │              │                  │
        │ • Summary        │              │     ChromaDB     │
        │ • Action Items   │              │        +         │
        │ • Decisions      │              │ Nomic Embeddings │
        │ • Questions      │              └────────┬─────────┘
        └──────────────────┘                       │
                                                 ▼
                                          Semantic Retriever
                                                 │
                                                 ▼
                                           RAG Q&A Engine
                                                 │
                                                 ▼
                                        Context-Aware Answers
```

---

# 🛠️ Tech Stack

### Backend & Application

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)

- Python
- Streamlit

### Generative AI

![LangChain](https://img.shields.io/badge/LangChain-LLM%20Orchestration-black)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-white)
![Whisper](https://img.shields.io/badge/Whisper-Speech%20AI-blueviolet)

- LangChain
- Ollama
- Qwen 2.5
- OpenAI Whisper

### RAG & Vector Search

![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-orange)

- ChromaDB
- Nomic Embed
- Recursive Character Text Splitting
- Semantic Similarity Retrieval
- Retrieval-Augmented Generation

### Media Processing

![FFmpeg](https://img.shields.io/badge/FFmpeg-Audio%20Processing-green?logo=ffmpeg)

- yt-dlp
- FFmpeg
- pydub

---

# 📂 Project Structure

```text
AI-Video-Assistant/
│
├── core/
│   │
│   ├── transcriber.py
│   │   └── Whisper-based transcription
│   │
│   ├── summarize.py
│   │   └── Chunked map-reduce summarization
│   │
│   ├── extractor.py
│   │   ├── Action item extraction
│   │   ├── Key decision extraction
│   │   └── Open question extraction
│   │
│   ├── vector_store.py
│   │   ├── Transcript chunking
│   │   ├── Embedding generation
│   │   ├── ChromaDB persistence
│   │   └── Retriever creation
│   │
│   └── rag_engine.py
│       └── Retrieval + prompt + LLM Q&A pipeline
│
├── utils/
│   └── audio_processor.py
│       ├── YouTube audio download
│       ├── FFmpeg conversion
│       └── Audio chunking
│
├── app.py
│   └── Streamlit interface
│
├── main.py
│   └── CLI application & pipeline orchestration
│
├── requirement.txt
├── .gitignore
└── README.md
```

---

# ⚙️ How It Works

## 1️⃣ Input Processing

The user provides either:

```text
YouTube URL
```

or:

```text
Local video/audio file
```

For YouTube videos, `yt-dlp` downloads the audio stream.

FFmpeg and pydub then prepare the media for transcription.

---

## 2️⃣ Audio Chunking

Long audio files are divided into manageable sections.

```text
Full Audio

↓ ↓ ↓ ↓

Chunk 1
Chunk 2
Chunk 3
...
```

Each chunk is independently processed by Whisper.

---

## 3️⃣ Speech-to-Text

Whisper generates the transcript:

```text
Audio Chunk
     ↓
   Whisper
     ↓
Transcript Text
```

The individual transcriptions are combined into a complete transcript.

---

## 4️⃣ LLM Processing

The transcript is passed through multiple specialized LangChain pipelines.

```text
                  Transcript
                     │
        ┌────────────┼──────────────┐
        │            │              │
        ▼            ▼              ▼
     Summary    Action Items    Decisions
                                      │
                                      ▼
                                Open Questions
```

Each workflow uses a dedicated prompt rather than asking one LLM call to perform every task.

---

# 🧠 Map-Reduce Summarization

For longer transcripts, directly sending everything to the model is inefficient and may exceed the model's context window.

The application therefore follows:

```text
Transcript
   ↓
Split into chunks
   ↓
Summarize every chunk
   ↓
Join partial summaries
   ↓
Generate final summary
```

Conceptually:

```python
chunk_summaries = [
    summarize(chunk)
    for chunk in transcript_chunks
]

combined_summary = combine(chunk_summaries)
```

This architecture makes long-form processing significantly more scalable.

---

# 🧠 Vector Embeddings

The transcript is divided into semantic text chunks:

```text
Transcript
      ↓
RecursiveCharacterTextSplitter
      ↓
Chunk 1
Chunk 2
Chunk 3
...
```

Each chunk is represented as a vector using:

```text
nomic-embed-text
```

and persisted inside:

```text
ChromaDB
```

---

# 🔎 Semantic Retrieval

When the user asks:

```text
"What did the speaker say about hierarchy?"
```

the question is embedded and compared against the stored transcript vectors.

The retriever selects the most relevant chunks:

```text
Question
   ↓
Embedding
   ↓
Vector Similarity
   ↓
Top K Relevant Chunks
```

The current retriever uses:

```text
Similarity Search
Top K = 4
```

---

# 🔗 LangChain Runnable Pipeline

The RAG workflow uses LangChain's composable Runnable architecture:

```text
Question
   │
   ├────────────────────┐
   │                    │
   ▼                    ▼
Retriever          RunnablePassthrough
   │                    │
   ▼                    │
Documents               │
   │                    │
   ▼                    │
format_docs()            │
   │                    │
   └──────────┬─────────┘
              ▼
      Context + Question
              │
              ▼
            Prompt
              │
              ▼
             LLM
              │
              ▼
       StrOutputParser
              │
              ▼
           Answer
```

---

# 🖥️ Running the Project

## 1. Clone Repository

```bash
git clone https://github.com/Kanishq2324/AI-Video-Assistant.git

cd AI-Video-Assistant
```

---

## 2. Install Python 3.12 with `uv`

```bash
uv python install 3.12
```

Create the virtual environment:

```bash
uv venv --python 3.12
```

Activate on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
uv pip install -r requirement.txt
```

---

## 4. Install FFmpeg

FFmpeg is required for media processing.

### Windows

```powershell
winget install -e --id Gyan.FFmpeg
```

Verify:

```bash
ffmpeg -version
ffprobe -version
```

---

## 5. Install Ollama Models

Pull the generation model:

```bash
ollama pull qwen2.5:1.5b
```

Pull the embedding model:

```bash
ollama pull nomic-embed-text
```

Verify:

```bash
ollama list
```

---

# ▶️ Run the CLI

```bash
python main.py
```

Example:

```text
Enter YouTube URL or local file path:
https://youtube.com/watch?v=...

Language:
english

Starting AI Video Assistant...

Detected YouTube URL. Downloading audio...

Chunking audio...

Using Whisper for transcription...

Generating summary...

Extracting action items...

Building vector store...

Ready.
```

---

# 🌐 Run the Streamlit Application

```bash
python -m streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

---

# 💡 Example Output

### 📌 Generated Title

```text
Building Better Systems Through Responsibility and Hierarchy
```

### 📋 Summary

```text
• The speaker discusses social hierarchies and responsibility.

• Hierarchies are explored as systems influenced by competence,
  incentives, and individual behavior.

• The discussion examines the consequences of viewing social
  structures purely through power-based frameworks.
```

### ✅ Action Items

```text
1. Evaluate assumptions behind existing organizational structures.

2. Examine alternative explanations for hierarchy formation.

3. Consider individual responsibility when analyzing social systems.
```

---

# 💬 Example RAG Conversation

```text
You:
What did the speaker say about hierarchy?

Assistant:
The speaker argued that hierarchies should not be viewed purely
as arbitrary power structures and discussed competence and
responsibility as factors influencing their formation.
```

If information cannot be found:

```text
Assistant:
I could not find this information in the meeting transcript.
```

---

# 🔐 Environment & Git Safety

The following files should never be committed:

```text
.env
.venv/
vector_db/
downloads/
__pycache__/
*.pyc
```

Recommended `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc

downloads/
vector_db/
```

---

# 🧑‍💻 Engineering Decisions

### Modular Architecture

Each major responsibility is isolated into its own component:

```text
Media Processing
Transcription
Summarization
Information Extraction
Embeddings
Vector Storage
Retrieval
Generation
UI
```

This makes the system easier to test, extend, and maintain.

---

### Specialized LLM Chains

Instead of using one large prompt for every task, the project creates dedicated chains for:

```text
Summarization
Action Items
Key Decisions
Open Questions
RAG Q&A
```

This keeps individual workflows simpler and easier to optimize.

---

### Persistent Vector Storage

ChromaDB allows transcript embeddings to be persisted and loaded later without rebuilding the entire knowledge base every time.

---

### Grounded Generation

The RAG assistant is explicitly instructed to answer based only on retrieved transcript context.

This helps reduce hallucination and improves factual grounding.

---

# 📈 What This Project Demonstrates

This project demonstrates hands-on experience with:

- Generative AI application development
- Retrieval-Augmented Generation
- LLM orchestration with LangChain
- Semantic search and vector databases
- Embedding pipelines
- Speech-to-text systems
- Long-context processing
- Map-reduce summarization
- Prompt engineering
- Modular backend architecture
- Production-oriented AI workflow design
- Media processing pipelines
- Streamlit application development

---

# 🗺️ Future Roadmap

### 🔹 Source-Aware RAG

Return transcript timestamps alongside retrieved answers.

```text
Answer:
Deployment was discussed as a Friday target.

Source:
12:43 – 13:20
```

### 🔹 Multi-Video Knowledge Base

Support multiple videos inside the same searchable workspace.

```text
Video 1
Video 2
Video 3
   ↓
Shared Knowledge Base
```

### 🔹 Conversation Memory

Support contextual multi-turn conversations:

```text
User:
Who owns deployment?

Assistant:
Rahul.

User:
When is he expected to finish?

Assistant:
Friday.
```

### 🔹 Speaker Diarization

Identify speakers automatically.

```text
Speaker 1:
...

Speaker 2:
...
```

### 🔹 FastAPI Backend

Expose the AI pipeline through production APIs.

### 🔹 Background Processing

Move transcription and embedding creation into asynchronous jobs for long videos.

### 🔹 Evaluation & Observability

Add:

- Retrieval quality metrics
- LLM response evaluation
- Token usage monitoring
- Latency tracking
- RAG trace visualization

---

# 🎯 Vision

AI Video Assistant is designed around a simple idea:

> **Long-form media should be searchable, structured, and conversational.**

The project combines traditional backend engineering with modern AI techniques to transform raw video content into a usable knowledge system.

```text
Video
  ↓
Speech
  ↓
Text
  ↓
Knowledge
  ↓
Search
  ↓
Conversation
```

---

## 👨‍💻 Author

**Kanishq Choudhary**

Software Engineer focused on backend engineering, Machine Learning, Generative AI, RAG, and agentic systems.

[GitHub](https://github.com/Kanishq2324)

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐.

It helps support continued development and future improvements.
