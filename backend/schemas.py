from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    mode: str
    content: str

class AnalyzeResponse(BaseModel):
    result: str
