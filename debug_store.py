from app.services.loader import DocumentLoader
from app.services.splitter import TextSplitter
from app.services.embeddings import EmbeddingModel

print("Step 1: Loading...")
docs = DocumentLoader.load_document("uploaded_docs/test.txt")
print("Loaded:", len(docs))

print("Step 2: Splitting...")
chunks = TextSplitter.split_documents(docs)
print("Chunks:", len(chunks))

print("Step 3: Generating embeddings...")

embedding_model = EmbeddingModel.get_embeddings()

vectors = embedding_model.embed_documents(
    [chunk.page_content for chunk in chunks]
)

print("Generated embeddings:", len(vectors))
print("Dimension:", len(vectors[0]))