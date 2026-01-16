def score_text(article: str) -> dict:
    """
    Scores the article based on clear, explainable rules.
    Returns a breakdown, not just a number.
    """

    score = 0
    reasons = []

    word_count = len(article.split())

    # Length check
    if word_count >= 1200:
        score += 2
        reasons.append("Good length")
    else:
        reasons.append("Too short")

    # Structure check
    if article.count("## ") >= 5:
        score += 2
        reasons.append("Clear section structure")
    else:
        reasons.append("Weak structure")

    # Practical signals
    lowered = article.lower()
    if "example" in lowered or "mistake" in lowered:
        score += 2
        reasons.append("Contains practical examples")
    else:
        reasons.append("Lacks practical examples")

    # Engagement signals
    if "?" in article:
        score += 2
        reasons.append("Engaging questions present")
    else:
        reasons.append("No engaging questions")

    # Readability heuristic
    avg_sentence_length = word_count / max(article.count("."), 1)
    if avg_sentence_length < 25:
        score += 2
        reasons.append("Readable sentence length")
    else:
        reasons.append("Sentences too long")

    return {
        "score": score,        # out of 10
        "reasons": reasons
    }
