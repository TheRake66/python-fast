from pathlib import Path
import json

configuration: dict | None = None

if not configuration:
  file = Path(__file__).resolve() \
    .parent.parent / "configuration.json"
  with open(file) as buffer:
    configuration = json.load(buffer)