from utils.scoring import score_text
from utils.llm import call_llm
from agent.llm_critic import llm_evaluate, CRITIC_MODEL
from utils.sanitize import strip_think_blocks

# 🔥 DEFINE CONSTANTS HERE (TOP LEVEL)
QUALITY_THRESHOLD = 8
MAX_REWRITES = 3

def rewrite_with_feedback(article: str, llm_eval: dict) -> str:
    """
    Normal rewrite using critic feedback
    """
    feedback = f"""
You are improving a Medium blog post.

Main issues:
{llm_eval["main_issues"]}

Weak sections:
{llm_eval["weak_sections"]}

Suggestions:
{llm_eval["improvement_suggestions"]}

Rewrite the article to fix these issues.
Do NOT change the topic or structure.
Use simple, human English.
"""

    result = call_llm(
    prompt=feedback + "\n\n" + article,
    model=CRITIC_MODEL,
    temperature=0.3
    )

    return strip_think_blocks(result)


def escalate_rewrite(article: str, llm_eval: dict) -> str:
    """
    Escalation rewrite when stagnation is detected
    """
    prompt = f"""
You are a senior technical editor.

CRITICAL RULES:
- DO NOT include <think>, reasoning, analysis, or internal thoughts
- DO NOT explain what you are doing
- DO NOT narrate your process
- ONLY output the revised blog content
- Keep the section structure unchanged

Force improvements by:
- Rewriting the INTRODUCTION with a strong personal hook
- Adding ONE concrete real-world example
- Removing generic or AI-sounding lines

Main issues:
{llm_eval["main_issues"]}

Return ONLY the final revised article.
"""


    result = call_llm(
    prompt=prompt + "\n\n" + article,
    model=CRITIC_MODEL,
    temperature=0.25
)

    return strip_think_blocks(result)


def critique(article: str) -> str:
    previous_scores = []

    for attempt in range(1, MAX_REWRITES + 1):
        rule_eval = score_text(article)
        rule_score = rule_eval["score"]

        llm_eval = llm_evaluate(article)
        llm_score = llm_eval["overall_score"]

        final_score = round((rule_score + llm_score) / 2, 2)

        print(f"\n[Critic] Attempt {attempt}")
        print(f"[Critic] Rule score: {rule_score}/10")
        print(f"[Critic] LLM score: {llm_score}/10")
        print(f"[Critic] Final score: {final_score}/10")

        # 🔁 STAGNATION DETECTION
        if final_score in previous_scores:
            print("[Critic] ⚠️ Stagnation detected. Escalating rewrite strategy.")
            return escalate_rewrite(article, llm_eval)

        previous_scores.append(final_score)

        if final_score >= QUALITY_THRESHOLD:
            print("[Critic] Quality threshold met ✅")
            return article

        article = rewrite_with_feedback(article, llm_eval)

    print("[Critic] Max rewrites reached. Returning best version.")
    return article
