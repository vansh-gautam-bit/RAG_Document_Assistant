from fastapi import FastAPI

from app.routers.upload import router as upload_router

app = FastAPI(title="Multi-Format RAG Assistant")

app.include_router(upload_router)


@app.get("/")
def root():
    return{"message": "RAG Assistant Running"}