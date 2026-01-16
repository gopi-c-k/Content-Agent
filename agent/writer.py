from utils.llm import call_llm

WRITER_MODEL = "llama-3.3-70b-versatile"

SECTIONS = [
    "Introduction",
    "Problem Context",
    "Real-World Mistake",
    "How to Fix It",
    "Key Takeaways"
]

def write(plan):
    article = ""

    for section in SECTIONS:
        prompt = f"""
You are writing a Medium blog.

Topic: {plan['topic']}
Angle: {plan['angle']}
Target audience: {plan['target_audience']}
Tone: {plan['tone']}

Write ONLY the section titled: {section}

Rules:
- Simple English
- Human tone
- Real-world examples
- No fluff
"""

        section_text = call_llm(
            prompt=prompt,
            model=WRITER_MODEL,
            temperature=0.8   # slightly creative
        )

        article += f"## {section}\n\n{section_text}\n\n"

    return article
