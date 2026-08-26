from libraries.catchable import Catchable
from libraries.system import os, OSType
import subprocess, os
from pathlib import Path

class ExplorerInvalidPath(Catchable): message="Invalid path {} to open!"

def open_folder(path: str) -> None:
  try:
    object: Path = Path(path).resolve()
    match os:
      case OSType.Windows: os.startfile(object)
      case OSType.MacOS: subprocess.run(["open", object])
      case OSType.Linux: subprocess.run(["xdg-open", object])
  except: raise ExplorerInvalidPath(path)