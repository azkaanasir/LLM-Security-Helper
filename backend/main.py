from fastapi import FastAPI
from schemas import AnalyzeRequest, AnalyzeResponse
from prompts import code_security_prompt, specs_security_prompt
from llmclient import call_gemini


app = FastAPI(title="LLM Security Helper")

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    if request.mode == "Code → Security Fixes":
        prompt = code_security_prompt(request.content)
    elif request.mode == "Specs → LLM Vulnerabilities":
        prompt = specs_security_prompt(request.content)
    else:
        return {"result": "Invalid mode selected"}

    result = call_gemini(prompt)
    return {"result": result}
