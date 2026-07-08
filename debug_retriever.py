from app.services.loader import DocumentLoader
from app.services.splitter import TextSplitter
from app.services.vectorstore import VectorStore
from app.services.retriever import Retriever

print("Loading...")
docs = DocumentLoader.load_document("uploaded_docs/test.txt")

print("Splitting...")
chunks = TextSplitter.split_documents(docs)

print("Creating FAISS...")
VectorStore.add_documents(chunks)

print("Creating Retriever...")
retriever = Retriever.get_retriever()

print("Searching...")
results = retriever.invoke("What is this document about?")

print(f"Retrieved {len(results)} document(s)\n")

for i, doc in enumerate(results, start=1):
    print(f"----- Result {i} -----")
    print(doc.page_content)
    print(doc.metadata)