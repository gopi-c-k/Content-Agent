from agent.observer import observe
from agent.analyzer import analyze
from agent.planner import plan
from agent.writer import write

if __name__ == "__main__":
    history = observe()
    insights = analyze(history)
    content_plan = plan(insights)

    article = write(content_plan)

    print("\nGenerated Article Preview:\n")
    print(article[:1500])  # preview only
