from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # 👈 ADD THIS

from app.routes import upload, docs, chat

app = FastAPI(title="CodeLens Backend")

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (for hackathon)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(docs.router, prefix="/docs", tags=["Docs"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/")
def root():
    return {"message": "CodeLens Backend Running 🚀"}