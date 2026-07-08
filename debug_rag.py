from app.services.loader import DocumentLoader
from app.services.splitter import TextSplitter
from app.services.vectorstore import VectorStore
from app.services.rag_chain import RAGChain

docs = DocumentLoader.load_document("uploaded_docs/test.txt")

chunks = TextSplitter.split_documents(docs)

VectorStore.add_documents(chunks)

answer = RAGChain.ask(
    "What is this document about?"
)

print(answer)