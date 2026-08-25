from libraries.catchable import Catchable
from libraries.exlorer import root
from pathlib import Path
import json

class CantOpenConfiguration(Catchable): message="Can't open configuration file!"
class MissingConfiguration(Catchable): message="Configuration file not found!"
class InvalidConfiguration(Catchable): message="Configuration file {} doesn't contain JSON!"
class ConfigurationKeyNotFound(Catchable): message="Key {} doesn't exist in configuration!"
class ConfigurationNotLoaded(Catchable): message="Configuration file not loaded or empty!"

__configuration: dict | None = None
__used: Path | None = None
__folder: Path = Path(root / "settings")
__save: Path = Path(root / "usedsettings")

def load_json() -> None:
  global __configuration
  global __used
  try: 
    name: str = "default.json" \
      if not __save.exists() else __save.read_text()
    file: Path = __folder / name
    content: str = file.read_text()
  except: raise MissingConfiguration(file)
  try: 
    __configuration = json.loads(content)
    __used = file
  except: raise InvalidConfiguration(file.name)

def set_used(name: str) -> None:
  file: Path = __folder / f"{name}.json"
  if not file.exists(): raise MissingConfiguration()
  try: __save.write_text(file.name)
  except: raise CantOpenConfiguration()

def get_used() -> str:
  if not __used: raise ConfigurationNotLoaded()
  return __used.stem

def get_list() -> str:
  files: list[Path] = list(__folder.glob("*.json"))
  return [file.stem for file in files]

def get_value(*keys: tuple[str]) -> str | int | bool:
  if not __configuration: raise ConfigurationNotLoaded()

  if not __configuration: raise Exception
  current: dict | None = __configuration
  for key in keys:
    if isinstance(current, dict) and key in current:
      current = current[key]
    else: raise ConfigurationKeyNotFound(key)
  return current