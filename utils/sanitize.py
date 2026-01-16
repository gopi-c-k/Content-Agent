import re

def strip_think_blocks(text: str) -> str:
    """
    Removes <think>...</think> or similar reasoning blocks.
    """

    # Remove <think>...</think>
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE)

    # Remove standalone <think> lines
    text = re.sub(r"<think>.*", "", text, flags=re.IGNORECASE)

    return text.strip()
