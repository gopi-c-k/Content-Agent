from agent.observer import observe
from agent.analyzer import analyze

if __name__ == "__main__":
    history = observe()
    insights = analyze(history)

    print("\nAnalyzer Insights:\n")
    for k, v in insights.items():
        print(f"{k}: {v}")
