from app.services.vectorstore import VectorStore
from pathlib import Path
from typing import Annotated
from app.services.loader import DocumentLoader
from app.services.splitter import TextSplitter

from fastapi import APIRouter , File , UploadFile

router = APIRouter(prefix="/upload",tags=["Upload"])

UPLOAD_DIR = Path("uploaded_docs")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/")
async def upload_files(
    files: Annotated[list[UploadFile],File(description="Upload files")]
):
    uploaded = []

    for file in files:
        destination = UPLOAD_DIR / file.filename

        with open(destination, "wb") as f:
            f.write(await file.read())

        documents = DocumentLoader.load_document(str(destination))

        chunks = TextSplitter.split_documents(documents)

        VectorStore.add_documents(chunks)

        print(f"{len(chunks)} chunks indexed successfully.")

        uploaded.append(file.filename)

    return {
        "message" : "Files uploaded successfully",
        "files":uploaded,
    }        

