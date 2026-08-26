from pathlib import Path
import platform
import getpass
import os

current: Path = Path.cwd()

variables: dict[str, str] = {
  "current_directory": str(current),
  "system_drive": os.path.splitdrive(current)[0],
  "user_name": getpass.getuser(),
  "machine_name": platform.node(),
}