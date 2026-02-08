# LLM Security Helper

An application that uses a third-party LLM API to assist with security analysis.

## Features
1. Code → Security Fixes  
   - Detects security vulnerabilities in code
   - Provides security-focused fixes

2. Specs → LLM Vulnerabilities  
   - Analyzes GenAI app specifications
   - Maps risks to OWASP Top 10 for LLM apps and ATLAS threats

## Tech Stack
- FastAPI (Backend)
- Streamlit (Frontend)
- OpenAI API (LLM)

## How to Run

### Backend
```bash
cd backend
uvicorn main:app --reload
