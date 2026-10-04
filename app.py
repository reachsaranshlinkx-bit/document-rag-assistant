from src.search import RAGSearch


def main():
    rag_search = RAGSearch()

    print("\n📚 Document RAG Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Ask a question: ").strip()

        if query.lower() == "exit":
            break

        answer = rag_search.search_and_summarize(
            query,
            top_k=3
        )

        print("\nAnswer:")
        print(answer)
        print()


if __name__ == "__main__":
    main()