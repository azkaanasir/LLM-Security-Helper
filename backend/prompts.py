def code_security_prompt(code: str) -> str:
    return f"""
You are a security expert.

Analyze the following code ONLY for security vulnerabilities.
Do NOT suggest refactoring, performance, or style improvements.

For each vulnerability:
- Vulnerability Name
- Why it is dangerous
- How to fix it (include secure code snippet if relevant)

Code:
{code}
"""


def specs_security_prompt(specs: str) -> str:
    return f"""
You are a GenAI security expert.

Given the following GenAI / agentic application specification,
identify potential vulnerabilities.

For EACH issue, provide:
- Vulnerability
- OWASP Top 10 for LLM Applications category
- ATLAS threat perspective
- Attack scenario
- Concrete mitigation

Application Specs:
{specs}
"""
