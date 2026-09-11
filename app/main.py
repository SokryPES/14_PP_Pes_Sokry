import sys
from app.retrieval import retrieve  
from app.generate import generate_answer

def main():
    print("=" * 50)
    print(" Welcome to Naive RAG Baseline (Terminal Chat)")
    print(" Type 'exit' or 'quit' to end the conversation.")
    print("=" * 50)

    while True:
        try:
            user_query = input("\nYou: ").strip()
            if not user_query:
                continue
            
            if user_query.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            print("\nThinking...")
            
           
            chunks = retrieve(user_query)
            
            
            answer = generate_answer(user_query, chunks)
            
            print(f"\nAssistant: {answer}")

        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

if __name__ == "__main__":
    main()