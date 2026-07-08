from app.services.loader import DocumentLoader
from app.services.splitter import TextSplitter
from app.services.vectorstore import VectorStore

print("Loading...")
docs = DocumentLoader.load_document("uploaded_docs/test.txt")

print("Splitting...")
chunks = TextSplitter.split_documents(docs)

print("Creating FAISS...")
VectorStore.add_documents(chunks)

print("SUCCESS!")