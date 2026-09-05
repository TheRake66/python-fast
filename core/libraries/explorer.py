from libraries.catchable import Catchable
from libraries.system import name, OSName
from subprocess import run
from pathlib import Path
from os import startfile

class ExplorerInvalidPath(Catchable): message="Invalid path {} to open!"

def open_folder(path: str) -> None:
  real: Path = Path(path).resolve()
  try:
    match name:
      case OSName.Windows: startfile(real)
      case OSName.MacOS: run(["open", real])
      case OSName.Linux: run(["xdg-open", real])
  except: raise ExplorerInvalidPath(real)