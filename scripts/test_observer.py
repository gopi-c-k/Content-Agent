from agent.observer import observe

if __name__ == "__main__":
    data = observe()
    print("\nObserver Output:\n")
    for post in data:
        print(f"- {post['title']} | Reads: {post['reads']} | Claps: {post['claps']}")
