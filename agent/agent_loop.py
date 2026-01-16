from agent.observer import observe
from agent.analyzer import analyze
from agent.planner import plan
from agent.writer import write
from agent.memory import save_run
from agent.critic import critique
from pathlib import Path

OUTPUT_FILE = Path("output/final_article.md")

def run_agent():
    print("\n🚀 Agent started\n")

    # 1️⃣ Observe
    print("👁️ Observing past content...")
    history = observe()

    # 2️⃣ Analyze
    print("🧠 Analyzing patterns...")
    insights = analyze(history)

    # 3️⃣ Plan
    print("🧭 Planning next article...")
    content_plan = plan(insights)

    print("\n📌 Content Plan:")
    for k, v in content_plan.items():
        print(f"  - {k}: {v}")

    # 4️⃣ Write
    print("\n✍️ Writing draft...")
    draft = write(content_plan)

    # 5️⃣ Critique & Improve
    print("\n🧪 Critiquing & improving...")
    final_article = critique(draft)

    # Extract final score info (simple heuristic)
    stagnated = "Stagnation detected" in final_article
    final_score = 8.0 if not stagnated else 6.5  # conservative estimate

    save_run(content_plan, final_score, stagnated)


    # 6️⃣ Save output
    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(final_article, encoding="utf-8")

    print(f"\n✅ Agent finished. Article saved to {OUTPUT_FILE}")

    return final_article
