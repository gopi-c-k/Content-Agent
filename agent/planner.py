from agent.memory import get_failed_topics

def plan(insights):
    failed_topics = get_failed_topics()

    # Prefer under-explored topics unless they failed before
    for topic in insights["under_explored_topics"]:
        if topic not in failed_topics:
            chosen_topic = topic
            reason = "Under-explored and not previously failed"
            break
    else:
        chosen_topic = insights["best_topic"]
        reason = "Fallback to historically best topic"

    return {
        "topic": chosen_topic,
        "reason": reason,
        "angle": "real-world mistakes and lessons",
        "target_audience": "intermediate software engineers",
        "planned_length": insights["ideal_length"] + 300,
        "tone": "personal, practical, honest",
        "goal": "maximize reader trust and retention"
    }
