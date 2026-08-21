from pydantic import BaseModel
from typing import Any

class Structure(BaseModel):

  def filter(self) -> dict[str, Any]:
    return self.model_dump(exclude_unset=True)