from agent.observer import observe
from agent.analyzer import analyze
from agent.planner import plan
from agent.writer import write
from agent.critic import critique

if __name__ == "__main__":
    history = observe()
    insights = analyze(history)
    content_plan = plan(insights)

    draft = write(content_plan)
    final_article = critique(draft)

    print("\nFINAL ARTICLE PREVIEW:\n")
    print(final_article[:1500])
