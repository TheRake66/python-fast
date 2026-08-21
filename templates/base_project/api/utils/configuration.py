import json

configuration: dict | None = None

if not configuration:
  with open("api/configuration.json") as buffer:
    configuration = json.load(buffer)