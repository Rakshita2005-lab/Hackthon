from fastapi import APIRouter
from app.services.vector_store import query_docs

router = APIRouter()

@router.post("/")
def chat(query: str):
    answer = query_docs(query)
    return {"answer": answer}