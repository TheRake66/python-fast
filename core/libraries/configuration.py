import json, os

configuration: dict | None = None

if not configuration:
  this = os.path.realpath(__file__)
  path = os.path.dirname(this)
  file = os.path.join(path, "configuration.json")
  with open(file) as buffer:
    configuration = json.load(buffer)