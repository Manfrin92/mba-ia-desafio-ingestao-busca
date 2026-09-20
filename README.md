# Ingestão e Busca Semântica com LangChain e Postgres

Projeto de ingestão de um arquivo PDF utilizando LangChain, geração de embeddings com Google Gemini e armazenamento em PostgreSQL com pgvector. O projeto também disponibiliza um chat via CLI para realizar perguntas sobre o conteúdo do PDF utilizando busca semântica (RAG).

## Pré-requisitos

* Python 3.13
* Docker e Docker Compose
* Uma API Key do Google Gemini

## Como executar

1. Crie o ambiente virtual:

```bash
python3.13 -m venv venv
```

2. Ative o ambiente virtual:

```bash
source venv/bin/activate
```

3. Crie o arquivo `.env` a partir do exemplo:

```bash
cp .env.example .env
```

4. Configure as variáveis de ambiente no `.env`.

5. Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

6. Inicie o PostgreSQL com pgvector:

```bash
docker compose up -d
```

7. Execute a ingestão do PDF:

```bash
python src/ingest.py
```

8. Inicie o chat:

```bash
python src/chat.py
```

O arquivo `document.pdf` utilizado na ingestão já está disponível na raiz do projeto.
