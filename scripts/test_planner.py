from agent.observer import observe
from agent.analyzer import analyze
from agent.planner import plan

if __name__ == "__main__":
    history = observe()
    insights = analyze(history)
    content_plan = plan(insights)

    print("\nPlanner Output:\n")
    for key, value in content_plan.items():
        print(f"{key}: {value}")
