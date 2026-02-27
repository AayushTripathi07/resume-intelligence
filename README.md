# Resume Intelligence System using Endee Vector Database

## Overview

This project is a semantic resume search engine built using the Endee Vector Database. It allows recruiters to search resumes using natural language queries and find the most relevant candidates using vector similarity.

## Features

- Resume upload and indexing
- Semantic search using embeddings
- Endee vector database integration
- Fast similarity-based retrieval
- Streamlit web interface

## Tech Stack

- Python
- Endee Vector Database
- Sentence Transformers
- Streamlit
- PyPDF2

## Architecture

User Query → Embedding Model → Endee Vector Database → Similarity Search → Results Display

## How Endee is Used

Endee is used as the vector database backend to store resume embeddings and perform similarity-based retrieval.

Key operations:

- Vector insertion
- Vector storage
- Vector search

## Setup Instructions

### Step 1: Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/resume-intelligence.git
cd resume-intelligence
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```
### Step 3: Start Endee server

```bash
cd endee/build
./ndd-neon-darwin
```
### Step 4: Run Streamlit app

```bash
streamlit run app.py
```

## Author
## Aayush Tripathi
