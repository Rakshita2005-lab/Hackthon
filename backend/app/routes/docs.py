from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.services.parser import parse_codebase
from app.services.doc_generator import generate_docs

router = APIRouter()

# ✅ Request model
class ProjectRequest(BaseModel):
    project_path: str

# ✅ Response model
class DocItem(BaseModel):
    file: str
    doc: str

class DocsResponse(BaseModel):
    docs: List[DocItem]

@router.post("/generate", response_model=DocsResponse)
def generate(request: ProjectRequest):
    structure = parse_codebase(request.project_path)

    # 🔍 Debug (optional)
    print("PATH:", request.project_path)
    print("FILES FOUND:", len(structure))

    docs = generate_docs(structure)

    return {"docs": docs}