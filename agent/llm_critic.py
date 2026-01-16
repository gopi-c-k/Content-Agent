from utils.llm import call_llm
import json

CRITIC_MODEL = "qwen/qwen3-32b"

def llm_evaluate(article: str) -> dict:
    prompt = f"""
You are a strict Medium editor.

CRITICAL RULES:
- DO NOT include <think>, reasoning, or explanations
- DO NOT include analysis text
- ONLY return valid JSON
- If unsure, still return JSON

Return ONLY this JSON format:

{{
  "overall_score": <1-10>,
  "weak_sections": ["..."],
  "main_issues": ["..."],
  "improvement_suggestions": ["..."]
}}

Blog:
\"\"\"
{article}
\"\"\"
"""


    response = call_llm(
        prompt=prompt,
        model=CRITIC_MODEL,
        temperature=0.2   # strict, low creativity
    )
    if "<think>" in response.lower():
        return {
            "overall_score": 5,
            "weak_sections": [],
            "main_issues": ["Model leaked chain-of-thought (<think>)"],
            "improvement_suggestions": [
                "Rewrite with strict no-reasoning constraint"
            ]
        }
    

    try:
        return json.loads(response)
    except Exception:
        return {
            "overall_score": 5,
            "weak_sections": [],
            "main_issues": ["Failed to parse critic output"],
            "improvement_suggestions": []
        }
