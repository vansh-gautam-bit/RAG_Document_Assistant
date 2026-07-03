from app.services.vectorstore import VectorStore

class Retriever:

    @staticmethod
    def get_retriever():
        db = VectorStore.get_db()

        return db.as_retriever(
            search_kwargs={"k":4}
        )