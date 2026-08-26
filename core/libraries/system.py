from pathlib import Path
from enum import Enum
import platform

class OSType(Enum):
  Windows: int = 0
  Linux: int = 1
  MacOS: int = 2
  Unknown: int = -1

os: OSType | None = None
root: Path | None = None

if not root:
  root = Path(__file__).parent.parent

if not os:
  match platform.system():
    case "Windows": os = OSType.Windows
    case "Darwin": os = OSType.MacOS
    case "Linux": os = OSType.Linux
    case _: os = OSType.Unknown