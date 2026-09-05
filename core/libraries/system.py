from libraries.catchable import Catchable
from platform import system
from subprocess import run
from pathlib import Path
from enum import Enum

class SystemInvalidCmd(Catchable): message="Invalid command {} to run!"

class OSName(Enum):
  Windows: int = 0
  Linux: int = 1
  MacOS: int = 2
  Unknown: int = -1

root: Path = Path(__file__).parent.parent
working: Path = Path.cwd()

match system():
  case "Windows": name: OSName = OSName.Windows
  case "Darwin": name: OSName = OSName.MacOS
  case "Linux": name: OSName = OSName.Linux
  case _: name: OSName = OSName.Unknown

def new_terminal(cmd: str) -> None:
  args: dict[OSName, list[str]] = {
    OSName.Windows: ["start", "cmd", "/c", cmd],
    OSName.MacOS: ["osascript", "-e", f'tell application "Terminal" to do script "{cmd}"'],
    OSName.Linux: ["gnome-terminal", "--", "bash", "-c", f"{cmd}; exec bash"],
    OSName.Unknown: [cmd]}
  try: run(args[name], shell=True, check=True)
  except: raise SystemInvalidCmd(cmd)