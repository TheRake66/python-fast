from libraries.catchable import Catchable
from libraries.explorer import root
from pathlib import Path
import json

class CantOpenSettings(Catchable): message="Can't open settings file!"
class MissingSettings(Catchable): message="Settings file not found!"
class InvalidSettings(Catchable): message="Settings file {} doesn't contain JSON!"
class SettingsKeyNotFound(Catchable): message="Key {} doesn't exist in settings file!"
class SettingsNotLoaded(Catchable): message="Settings file not loaded or empty!"

__settings: dict | None = None
__used: Path | None = None
__folder: Path = Path(root / "settings")
__save: Path = Path(root / "usedsettings")

def load_json() -> None:
  global __settings
  global __used
  try: 
    name: str = "react-fastapi.json" \
      if not __save.exists() else __save.read_text()
    file: Path = __folder / name
    content: str = file.read_text()
  except: raise MissingSettings(file)
  try: 
    __settings = json.loads(content)
    __used = file
  except: raise InvalidSettings(file.name)

def set_used(name: str) -> None:
  file: Path = __folder / f"{name}.json"
  if not file.exists(): raise MissingSettings()
  try: __save.write_text(file.name)
  except: raise CantOpenSettings()

def get_used() -> str:
  if not __used: raise SettingsNotLoaded()
  return __used.stem

def get_list() -> str:
  files: list[Path] = list(__folder.glob("*.json"))
  return [file.stem for file in files]

def get_value(*keys: tuple[str]) -> str | int | bool:
  if not __settings: raise SettingsNotLoaded()
  current: dict | None = __settings
  for key in keys:
    if isinstance(current, dict) and key in current:
      current = current[key]
    else: raise SettingsKeyNotFound(key)
  return current