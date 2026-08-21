from api.utils.response import Response
from api.utils.structure import Structure
from fastapi import APIRouter
from typing import Optional

router = APIRouter(prefix="/{{lower_name}}s")

class {{capitalize_name}}Create(Structure):
  id: int
  name: str
  description: str
  deleted: bool = False

class {{capitalize_name}}Update(Structure):
  id: int
  name: Optional[str] = None
  description: Optional[str] = None
  deleted: Optional[bool] = False

@router.get("/")
async def get_all_{{lower_name}}s(limit: int = 10) -> Response:
  return Response(message=f"Liste des {limit} premiers éléments.")

@router.get("/{id}")
async def get_{{lower_name}}_by_id(id: int) -> dict:
  return Response(message=f"Recuperation de l'élément {id}.")

@router.post("/")
async def create_{{lower_name}}(item: {{capitalize_name}}Create) -> dict:
  return Response(message=f"Création de la ressource {item}.")

@router.put("/{id}")
async def update_{{lower_name}}_full(id: int, item: {{capitalize_name}}Create) -> dict:
  return Response(message=f"Remplacement intégral de l'élément {id} par {item}.")

@router.patch("/{id}")
async def update_{{lower_name}}_partial(id: int, item: {{capitalize_name}}Update) -> dict:
  return Response(message=f"Remplacement partiel de l'élément {id} par {item.filter()}.")

@router.delete("/{id}")
async def delete_{{lower_name}}(id: int):
  return Response(message=f"Suppression de l'élément {id}.")