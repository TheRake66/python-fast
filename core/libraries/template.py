from libraries.setting import get_value
from libraries.variable import get_injected
from libraries.catchable import Catchable
from libraries.system import root
from urllib.request import urlretrieve
from zipfile import ZipFile, ZipInfo
from pathlib import Path
from enum import Enum
import uuid, os, tempfile

class TemplateNotFound(Catchable): message="Template {} not found!"
class BadTemplateFormat(Catchable): message="Template {} is badly formatted!"
class CantDownloadTemplate(Catchable): message="Can't download {} template!"
class CantOpenTemplate(Catchable): message="Can't open {} template file!"

class ProcessType(Enum):
  DELETE: int = 0
  EXTRACT: int = 1

def __replace_variables(text: str, variables: dict[str, str]) -> str:
  for variable in variables.keys():
    if variable in text:
      value = variables[variable]
      text = text.replace(variable, value)
  return text

def __download_zip(url: str) -> Path:
  try:
    temp = Path(tempfile.gettempdir())
    name: str = str(uuid.uuid4().hex)
    path = temp / name
    urlretrieve(url, path)
    return path
  except: raise CantDownloadTemplate(url)

def __clean_zip(path: Path) -> None:
  try: os.remove(path)
  except: pass

def __extract_zip(path: Path, variables: dict[str, str], zip: ZipFile, info: ZipInfo) -> None:
  suffixs: list[str] = get_value("suffixs")
  # S'il n'est pas dans la liste des extensions on extrait juste le fichier tel quel.
  if not path.suffix in suffixs:
    zip.extract(info, ".")
    return
  # On lit son contenu.
  content: str = ""
  with zip.open(info, "r") as buffer:
    content = buffer.read().decode("utf-8")
  # Remplace les variables dans le contenu.
  content = __replace_variables(content, variables)
  # Extrait le nouveau fichier.
  path.parent.mkdir(parents=True, exist_ok=True)
  with open(path, "w", encoding="utf-8", newline="") as buffer:
    buffer.write(content)

def __delete_zip(path: Path) -> None:
  # Check si c'est un fichier ou un lien pour le supprimer.
  if path.is_file() or path.is_symlink():
    path.unlink()
    # Supprimer les dossier parents non vides pour remonter jusqu'au bon dossier.
    for parent in path.parents:
      try: parent.rmdir()
      except OSError: break

def __browse_zip(path: Path, variables: dict[str, str], type: ProcessType):
  try:
    with ZipFile(path, "r") as zip:
      for info in zip.infolist():
        if info.is_dir(): continue
        # Outils de merde qui mettent des backslashs non standards.
        info.filename = info.filename.replace('\\', '/')
        info.filename = __replace_variables(info.filename, variables)
        object: Path = Path(info.filename)
        try:
          match type:
            case ProcessType.EXTRACT: __extract_zip(object, variables, zip, info)
            case ProcessType.DELETE: __delete_zip(object)
        except: raise BadTemplateFormat(path)
  except: raise CantOpenTemplate(path)

def process_zip(template: str, namespace: str, extras: list[str], type: ProcessType):
  zip: str = get_value("templates", template)
  path: Path = root / "templates" / zip
  clean: bool = False
  if zip.startswith("http"):
    path = __download_zip(zip)
    clean = True
  if not path.exists(): raise TemplateNotFound(path)
  variables: dict[str, str] = get_injected(namespace, extras)
  __browse_zip(path, variables, type)
  if clean: __clean_zip(path)