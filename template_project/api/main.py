from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from api.utils.configuration import configuration

application = FastAPI()
application.add_middleware(CORSMiddleware,
    allow_credentials=configuration["credentials"],
    allow_origins=configuration["origins"], 
    allow_methods=configuration["methods"], 
    allow_headers=configuration["headers"])

def add_routers(*routers: APIRouter) -> None:
  api_prefix = f"/api/{configuration["version"]}"
  for router in routers:
    application.include_router(router, prefix=api_prefix)