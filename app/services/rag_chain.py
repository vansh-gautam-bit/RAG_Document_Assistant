from app.prompts.rag_prompt import RAG_PROMPT
from app.services.llm import LLM
from app.services.retriever import Retriever

class RAGChain:

    @staticmethod
    def ask(question: str):

        retriever = Retriever.get_retriever()

        docs = retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        llm = LLM.get_llm()

        prompt = RAG_PROMPT.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        response = llm.invoke(prompt)

        return response.content