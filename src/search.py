import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain_postgres import PGVector

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""


def search(question):
    load_dotenv()

    embeddings = GoogleGenerativeAIEmbeddings(
        model=os.getenv("GOOGLE_EMBEDDING_MODEL"),
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
    )

    results = store.similarity_search(question, k=3)

    contexto = "\n\n".join(
        document.page_content
        for document in results
    )

    prompt = PromptTemplate(
        input_variables=["contexto", "pergunta"],
        template=PROMPT_TEMPLATE,
    )

    model = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0.5,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )

    chain = prompt | model

    response = chain.invoke({
        "contexto": contexto,
        "pergunta": question,
    })

    return response.content


if __name__ == "__main__":
    question = input("Pergunta: ")
    answer = search(question)

    print("\nResposta:")
    print(answer)