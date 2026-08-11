from fastapi import APIRouter, status, Response
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/{{lower_item_name}}s", tags=["{{capitalize_item_name}}s"])

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

@router.get("/")
async def get_all_{{lower_item_name}}s(limit: int = 10) -> dict:
  return { "message": f"Liste des {limit} premiers éléments." }

@router.get("/{item_id}")
async def get_{{lower_item_name}}_by_id(item_id: int) -> dict:
  return { "message": f"Recuperation de l'élément {item_id}." }

@router.post("/")
async def create_{{lower_item_name}}(item: ItemCreate) -> dict:
  return { "message": f"Création de la ressource {item}." }

@router.put("/{item_id}")
async def update_{{lower_item_name}}_full(item_id: int, item: ItemCreate) -> dict:
  return {"message": f"Remplacement intégral de l'élément {item_id} par {item}." }

@router.patch("/{item_id}")
async def update_{{lower_item_name}}_partial(item_id: int, item: ItemUpdate) -> dict:
  update_data = item.model_dump(exclude_unset=True)
  return {"message": f"Remplacement partiel de l'élément {item_id} par {update_data}." }

@router.delete("/{item_id}")
async def delete_{{lower_item_name}}(item_id: int):
  return {"message": f"Suppression de l'élément {item_id}." }