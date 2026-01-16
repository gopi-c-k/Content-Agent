import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt: str, model: str, temperature: float = 0.7) -> str:
    """
    Centralized LLM call.
    Model must be explicitly passed by caller.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )

    return response.choices[0].message.content.strip()
