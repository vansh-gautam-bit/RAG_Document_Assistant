from app.services.vectorstore import VectorStore

class Retriever:

    @staticmethod
    def get_retriever():
        db = VectorStore.get_db()

        if db is None:
            raise ValueError("Vector Store is empty. Upload documents first.")
        
        return db.as_retriever(
            search_kwargs={"k":4}
        )