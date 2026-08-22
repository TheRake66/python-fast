from libraries.structure import VarValue
from typing import NoReturn
from pathlib import Path
import sys, os, shutil


def load_values(name: str) -> VarValue:
  return VarValue(
    CAPITALIZE_NAME = name.capitalize(),
    UPPER_NAME = name.upper(),
    LOWER_NAME = name.lower())

def ensure_project() -> None:
  if Path("index.html").is_file(): return
  print("❌ Le répertoire courant n'est pas une application.")
  sys.exit(1)

def get_venv(binary: str) -> str:
  if sys.platform == 'win32':
    return os.path.join('venv', 'Scripts', f'{binary}.exe')
  return os.path.join('venv', 'bin', binary)

def get_npm() -> str:
  return shutil.which('npm') or 'npm'
