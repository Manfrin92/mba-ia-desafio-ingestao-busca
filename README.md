# Ingestão e Busca Semântica com LangChain e Postgres

## Como executar

1. Setar as env variables conforme .env.example
2. Iniciar o venv: `python3.13 -m venv venv`
3. Iniciar o venv: `source venv/bin/activate`
4. Installar as dependencias do projeto: `python -m pip install -r requirements.txt`
5. Iniciar o container com o banco vetorial: `docker compose up -d`
6. Executar a ingestão do pdf: `python src/ingest.py`
7. Rodar o chat: `python src/chat.py`
