from pathlib import Path
import os
import platform

current: Path = Path.cwd()

def get_username() -> str:
  if hasattr(os, "getlogin"):return os.getlogin()
  return os.environ.get("USER", os.environ.get("USERNAME", ""))

variables: dict[str, str] = {
  "current_directory": str(current),
  "system_drive": os.path.splitdrive(current)[0],
  "user_name": get_username(),
  "machine_name": platform.node(),
}