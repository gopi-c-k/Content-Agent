import json
from pathlib import Path

DATA_FILE = Path("data/medium_history.json")

def observe():
    """
    Observer:
    - Reads historical content performance
    - Validates schema
    - Returns structured data for the agent
    """
    if not DATA_FILE.exists():
        raise FileNotFoundError("medium_history.json not found")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)

    # Basic validation (important)
    for post in history:
        required_keys = [
            "title", "topic", "length",
            "views", "reads", "claps"
        ]
        for key in required_keys:
            if key not in post:
                raise ValueError(f"Missing key '{key}' in post")

    return history
