from llm.router import get_answer   

def main():
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            break

        context = ""   # No RAG for now

        try:
            answer = get_answer(context, query)
            print("\nAnswer:\n", answer, "\n")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()