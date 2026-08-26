from libraries.message import print_var, print_error
from libraries.variable import get_injected
from libraries.setting import get_value
from libraries.catchable import Catchable
from libraries.system import root, working
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
  # S'il existe deja on skip.
  if path.is_file():
    print_var("⚠️ File {} already exist, skipped.", path)
    return
  # On cree l'arborescence.
  parent: Path = path.parent
  if not parent.is_dir():
    try:
      print_var("📁 Creation of folder {}...", parent)
      parent.mkdir(parents=True, exist_ok=True)
    except:
      print_error("Failed to create folder!")
      return
  # S'il n'est pas dans la liste des extensions on extrait juste le fichier tel quel.
  suffixs: list[str] = get_value("suffixs")
  if not path.suffix in suffixs:
    try:
      print_var("📄 Creation of file {}...", path)
      with zip.open(info, "r") as source, open(path, "wb") as target:
        target.write(source.read())
    except: 
      print_error("Failed to create file!")
    return
  # On modifie le fichier.
  try:
    print_var("📝 Creation and edition of file {}...", path)
    content: str = ""
    # On lit son contenu.
    with zip.open(info, "r") as buffer:
      content = buffer.read().decode("utf-8")
    # Remplace les variables dans le contenu.
    content = __replace_variables(content, variables)
    # Extrait le nouveau fichier.
    with open(path, "w", encoding="utf-8", newline="") as buffer:
      buffer.write(content)
  except: print_error("Failed to create and edit file!")

def __delete_zip(path: Path) -> None:
  # S'il n'existe plus on skip.
  if not path.is_file():
    print_var("⚠️ File {} not found, skipped.", path)
    return
  # On supprime le fichier.
  try:
      print_var("🗑️ Deletion of file {}...", path)
      path.unlink()
  except:
    print_error("Failed to delete file!")
    return
  # Supprimer les dossier parents non vides pour remonter jusqu'au bon dossier.
  for parent in path.parents:
    if parent.resolve() == working.resolve(): break
    if any(parent.iterdir()): break
    try:
      print_var("📁 Deletion of folder {}...", parent)
      parent.rmdir()
    except:
      print_error("Failed to delete folder!")
      break

def __browse_zip(path: Path, variables: dict[str, str], type: ProcessType):
  try: zip = ZipFile(path, "r")
  except: raise CantOpenTemplate(path)
  with zip:
    for info in zip.infolist():
      if info.is_dir(): continue
      # Outils de merde qui mettent des backslashs non standards.
      info.filename = info.filename.replace('\\', '/')
      info.filename = __replace_variables(info.filename, variables)
      object: Path = Path(info.filename)
      match type:
        case ProcessType.EXTRACT: __extract_zip(object, variables, zip, info)
        case ProcessType.DELETE: __delete_zip(object)

def process_zip(template: str, namespace: str, extras: list[str], type: ProcessType):
  zip: str = get_value("templates", template)
  path: Path = root / "templates" / zip
  clean: bool = False
  # On telecharge si c'est une url.
  if zip.startswith("http"):
    print_var("📥 Downloading template archive {}...", path.name)
    path = __download_zip(zip)
    clean = True
  if not path.is_file(): raise TemplateNotFound(path)
  variables: dict[str, str] = get_injected(namespace, extras)
  try: __browse_zip(path, variables, type)
  finally:
    if clean: __clean_zip(path)