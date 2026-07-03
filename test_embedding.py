from app.services.embeddings import EmbeddingModel

embeddings = EmbeddingModel.get_embeddings()

vector = embeddings.embed_query("Hello RAG")

print(len(vector))
print(vector[:5])