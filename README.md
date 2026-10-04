# 📚 Document RAG Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about documents and receive answers based on relevant retrieved content.

The project uses LangChain for the RAG pipeline, Sentence Transformers for embeddings, FAISS for vector similarity search, and Groq for LLM-based answer generation.

## 🚀 Project Overview

Traditional LLMs may not have access to the specific information contained in a user's documents.

This project solves that problem using Retrieval-Augmented Generation:

```text
Documents
    ↓
Document Loading
    ↓
Text Chunking
    ↓
Embeddings
    ↓
FAISS Vector Store
    ↓
Similarity Search
    ↓
Relevant Context
    ↓
Groq LLM
    ↓
Generated Answer
