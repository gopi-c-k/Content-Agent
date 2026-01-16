from utils.llm import call_llm

if __name__ == "__main__":
    output = call_llm(
        "Explain what an AI agent is in one simple paragraph."
    )
    print("\nLLM OUTPUT:\n")
    print(output)
