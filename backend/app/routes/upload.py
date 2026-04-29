from fastapi import APIRouter, UploadFile
import zipfile, os

router = APIRouter()

UPLOAD_DIR = "temp_projects"

@router.post("/")
async def upload_project(file: UploadFile):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    zip_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(zip_path, "wb") as f:
        f.write(await file.read())

    extract_path = zip_path.replace(".zip", "")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

    return {"message": "Project uploaded", "path": extract_path}