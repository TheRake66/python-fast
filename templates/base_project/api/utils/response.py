from pydantic import BaseModel

class Response(BaseModel):
  message: str
  code: int = 0
  content: dict | None = None