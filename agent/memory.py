import json
from pathlib import Path
from datetime import datetime

MEMORY_FILE = Path("data/agent_memory.json")

def load_memory():
    if not MEMORY_FILE.exists():
        return []

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_run(plan: dict, final_score: float, stagnated: bool):
    memory = load_memory()

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "topic": plan["topic"],
        "angle": plan["angle"],
        "final_score": final_score,
        "stagnated": stagnated
    }

    memory.append(entry)

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

def get_failed_topics(threshold: float = 7.0):
    """
    Returns topics that repeatedly failed or stagnated
    """
    memory = load_memory()
    failures = {}

    for run in memory:
        if run["final_score"] < threshold or run["stagnated"]:
            failures.setdefault(run["topic"], 0)
            failures[run["topic"]] += 1

    return [topic for topic, count in failures.items() if count >= 2]
