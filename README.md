# Resume Intelligence System using Endee Vector Database

## Project Overview

This project implements a semantic resume search engine using the Endee Vector Database. It enables recruiters and hiring systems to search and retrieve resumes based on natural language queries rather than exact keyword matches.

Traditional resume screening relies on keyword matching, which often misses relevant candidates due to differences in wording. This system solves that problem using vector embeddings and semantic similarity, allowing more intelligent and accurate candidate retrieval.

The application uses Endee as the vector database backend to store resume embeddings and perform similarity-based search efficiently.

---

## Problem Statement

Recruiters often need to search through hundreds or thousands of resumes to find suitable candidates. Keyword-based filtering is inefficient and fails to capture semantic meaning.

Challenges include:

* Keyword mismatch between resumes and job descriptions
* Large volume of resumes
* Inefficient manual screening
* Lack of semantic understanding

This project addresses these challenges by:

* Converting resumes into vector embeddings
* Storing embeddings in Endee vector database
* Performing semantic similarity search using natural language queries

---

## System Design and Architecture

### High-Level Architecture

```
User Query (Streamlit UI)
        │
        ▼
Embedding Model (Sentence Transformers)
        │
        ▼
Endee Vector Database
        │
        ▼
Similarity Search
        │
        ▼
Ranked Resume Results
```

---

### System Components

#### 1. User Interface

* Built using Streamlit
* Allows users to upload resumes
* Allows users to search resumes using natural language

#### 2. Resume Parser

* Extracts text from PDF resumes
* Uses PyPDF2 for parsing

#### 3. Embedding Generator

* Uses Sentence Transformers (all-MiniLM-L6-v2)
* Converts resume text and queries into 384-dimensional vectors

#### 4. Vector Database (Endee)

* Stores vector embeddings of resumes
* Performs fast similarity search
* Handles vector indexing and retrieval

#### 5. Search Engine

* Converts user query into vector
* Searches Endee database
* Returns ranked resumes based on similarity

---

## Technical Approach

### Step 1: Resume Indexing

1. User uploads resumes
2. Resume text is extracted
3. Embeddings are generated using transformer model
4. Embeddings are stored in Endee vector database

### Step 2: Semantic Search

1. User enters search query
2. Query converted into embedding
3. Endee performs similarity search
4. Most relevant resumes returned

---

## How Endee Vector Database is Used

Endee serves as the core vector storage and retrieval system.

Endee is used for:

* Creating vector index
* Storing resume embeddings
* Performing similarity search
* Efficient vector retrieval

### Endee Operations Used

#### Index Creation

```
POST /api/v1/index/create
```

#### Vector Insertion

```
POST /api/v1/index/resumes/vector/insert
```

#### Vector Search

```
POST /api/v1/index/resumes/search
```

Endee enables efficient semantic search across resume embeddings with high performance.

---

## Project Structure

```
resume-intelligence/
│
├── app.py                 # Streamlit UI
├── search.py              # Indexing and search logic
├── database.py            # Endee database integration
├── embedder.py            # Embedding generation
├── resume_parser.py       # PDF text extraction
│
├── resumes/               # Resume storage folder
│
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

---

## Setup and Execution Instructions

### Step 1: Clone Repository

```
git clone https://github.com/AayushTripathi07/resume-intelligence.git
cd resume-intelligence
```

---

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

---

### Step 3: Start Endee Vector Database Server

Navigate to Endee build directory:

```
cd endee/build
export NDD_DATA_DIR=./endee_db
./ndd-neon-darwin
```

Server runs at:

```
http://localhost:8080
```

---

### Step 4: Run Streamlit Application

Navigate to project directory:

```
cd resume-intelligence
streamlit run app.py
```

Application runs at:

```
http://localhost:8501
```

---

## Example Usage

### Index Resumes

Upload PDF resumes and click "Index Resumes"

### Search Example Queries

```
Data analyst with Python experience
Machine learning engineer
Frontend developer
Business intelligence analyst
```

System returns ranked resumes based on semantic similarity.

---

## Key Features

* Semantic resume search
* Endee vector database integration
* Fast similarity-based retrieval
* Natural language search support
* Streamlit interactive interface
* Efficient vector storage and retrieval

---

## Technical Stack

| Component         | Technology               |
| ----------------- | ------------------------ |
| Frontend          | Streamlit                |
| Backend           | Python                   |
| Vector Database   | Endee                    |
| Embedding Model   | Sentence Transformers    |
| PDF Processing    | PyPDF2                   |
| Similarity Search | Vector cosine similarity |

---

## Performance and Scalability

Endee enables:

* Fast vector search
* Efficient indexing
* Scalable architecture
* Low-latency retrieval

The system can scale to thousands of resumes efficiently.

---

## Future Improvements

* Job description to candidate matching
* RAG-based recruiter assistant
* Resume ranking dashboard
* Cloud deployment
* Multi-user support

---

## Conclusion

This project demonstrates a complete semantic search system using Endee Vector Database. It replaces inefficient keyword search with intelligent vector-based retrieval, improving candidate matching accuracy and recruiter efficiency.

The system successfully integrates Endee for vector storage, indexing, and retrieval, fulfilling the project requirements for vector database integration and semantic search.

## Project Demo

###Demo Link: https://youtu.be/GulcNcYfRjI 
