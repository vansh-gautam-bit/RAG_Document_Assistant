from app.services.vectorstore import VectorStore

print("Opening DB...")
db = VectorStore.get_db()
print(db)

print("Collection:")
print(db._collection)