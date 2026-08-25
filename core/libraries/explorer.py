from libraries.catchable import Catchable
import subprocess, platform, os
from pathlib import Path

class ExplorerInvalidPath(Catchable): message="Invalid path {} to open!"

root: Path | None = None

if not root:
  root = Path(__file__).parent.parent

def open_folder(path: str) -> None:
  try:
    object: Path = Path(path).resolve()
    system: str = platform.system()
    if system == "Windows": os.startfile(object)
    elif system == "Darwin": subprocess.run(["open", object])
    else: subprocess.run(["xdg-open", object])
  except: raise ExplorerInvalidPath(path)