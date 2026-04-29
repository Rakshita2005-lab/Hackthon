from pydantic import BaseModel

class Document(BaseModel):
    file: str
    content: str