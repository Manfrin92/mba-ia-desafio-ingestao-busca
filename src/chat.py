from search import search

def main():
    question = input("Pergunta: ")

    answer = search(question)

    print("\nResposta:")
    print(answer)

if __name__ == "__main__":
    main()