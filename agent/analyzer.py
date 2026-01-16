from collections import defaultdict

def analyze(history):
    """
    Analyzer:
    - Processes historical content performance
    - Extracts insights for planning
    """

    topic_stats = defaultdict(lambda: {
        "articles": 0,
        "total_reads": 0,
        "total_views": 0,
        "total_length": 0
    })

    for post in history:
        topic = post["topic"]
        topic_stats[topic]["articles"] += 1
        topic_stats[topic]["total_reads"] += post["reads"]
        topic_stats[topic]["total_views"] += post["views"]
        topic_stats[topic]["total_length"] += post["length"]

    insights = {}

    # 1️⃣ Best topic (highest read ratio)
    best_topic = None
    best_ratio = 0

    for topic, stats in topic_stats.items():
        if stats["total_views"] == 0:
            continue

        ratio = stats["total_reads"] / stats["total_views"]
        if ratio > best_ratio:
            best_ratio = ratio
            best_topic = topic

    insights["best_topic"] = best_topic

    # 2️⃣ Ideal length (average of best topic)
    if best_topic:
        stats = topic_stats[best_topic]
        insights["ideal_length"] = stats["total_length"] // stats["articles"]
    else:
        insights["ideal_length"] = 1500  # fallback

    # 3️⃣ Under-explored topics
    min_articles = min(stats["articles"] for stats in topic_stats.values())
    insights["under_explored_topics"] = [
        topic for topic, stats in topic_stats.items()
        if stats["articles"] == min_articles
    ]

    return insights
