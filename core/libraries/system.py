from pathlib import Path
from enum import Enum
import platform

class OSType(Enum):
  Windows: int = 0
  Linux: int = 1
  MacOS: int = 2
  Unknown: int = -1

type: OSType | None = None
root: Path | None = None

if not root:
  root = Path(__file__).parent.parent

if not type:
  match platform.system():
    case "Windows": type = OSType.Windows
    case "Darwin": type = OSType.MacOS
    case "Linux": type = OSType.Linux
    case _: type = OSType.Unknown