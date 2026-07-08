from langchain_core.documents import Document
from app.services.vectorstore import VectorStore

db = VectorStore.get_db()

doc = Document(
    page_content="Hello from ChatGPT",
    metadata={"source": "debug"}
)

print("Adding...")
ids = db.add_documents([doc])
print(ids)
print("DONE")