from libraries.catchable import Catchable
from libraries.system import type, OSType
from libraries.message import print_var
import subprocess, os
from pathlib import Path

class ExplorerInvalidPath(Catchable): message="Invalid path {} to open!"

def open_folder(path: str) -> None:
  real: Path = Path(path).resolve()
  try:
    match type:
      case OSType.Windows: os.startfile(real)
      case OSType.MacOS: subprocess.run(["open", real])
      case OSType.Linux: subprocess.run(["xdg-open", real])
  except: raise ExplorerInvalidPath(real)