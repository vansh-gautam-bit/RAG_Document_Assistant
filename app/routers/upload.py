# from pathlib import Path

# from fastapi import APIRouter, UploadFile, File

# router =APIRouter(prefix="/upload", tags=["Upload"])

# UPLOAD_DIR = Path("uploaded_docs")
# UPLOAD_DIR.mkdir(exist_ok=True)

# @router.post("/")
# async def upload_files(files: list[UploadFile]= File(...)):

#     uploaded = []

#     for file in files:

#         destination = UPLOAD_DIR / file.filename

#         with open(destination, "wb") as f:
#             f.write(await file.read())

#         uploaded.append(file.filename)

#         return {
#             "message": "Files uploaded successfully",
#             "files": uploaded,
#         }    

from typing import Annotated

from fastapi import APIRouter, File, UploadFile

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
async def upload_files(
    files: Annotated[list[UploadFile], File(description="Upload files")]
):
    return {
        "count": len(files),
        "files": [f.filename for f in files],
    }