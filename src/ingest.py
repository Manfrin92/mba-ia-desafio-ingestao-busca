import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")

loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)

chunks = splitter.split_documents(docs)

def ingest_pdf():
    pass


if __name__ == "__main__":
    ingest_pdf()