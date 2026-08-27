from libraries.message import print_var
from libraries.variable import get_injected
from libraries.setting import get_value
from libraries.catchable import Catchable
from libraries.system import root, working
from urllib.request import urlretrieve
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
from pathlib import Path
from enum import Enum
import uuid, os, tempfile

class TemplateNotFound(Catchable): message="Template {} not found!"
class CantDownloadTemplate(Catchable): message="Can't download {} template!"
class CantOpenTemplate(Catchable): message="Can't open {} template file!"

class CantCreateFolder(Catchable): message="Failed to create {} as folder!"
class CantCreateFile(Catchable): message="Failed to create {} as file!"
class CantCreateEditFile(Catchable): message="Failed to create and edit {} as file!"

class CantDeleteFolder(Catchable): message="Failed to delete {} as folder!"
class CantDeleteFile(Catchable): message="Failed to delete {} as file!"

class TemplateAlreadyExist(Catchable): message="Template {} already exists!"
class CantCreateTemplate(Catchable): message="Can't create {} template file!"
class CantListFiles(Catchable): message="Can't list files in {} folder!"
class CantCompressFile(Catchable): message="Can't compress file {} into template file!"

class ProcessType(Enum):
  DELETE: int = 0
  EXTRACT: int = 1
  INTEGRITY: int = 2

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

def __extract_zip(path: Path, variables: dict[str, str], suffixs: list[str], zip: ZipFile, info: ZipInfo) -> None:
  # S'il existe deja on skip.
  if path.is_file():
    print_var("⚠️ File {} already exists, skipped.", path)
    return
  # On cree l'arborescence.
  parent: Path = path.parent
  if not parent.is_dir():
    print_var("📁 Creation of folder {}...", parent)
    try: parent.mkdir(parents=True, exist_ok=True)
    except: raise CantCreateFolder(parent)
  # S'il n'est pas dans la liste des extensions on extrait juste le fichier tel quel.
  if not path.suffix in suffixs:
    print_var("📄 Creation of file {}...", path)
    try:
      with zip.open(info, "r") as source, open(path, "wb") as target:
        target.write(source.read())
    except: raise CantCreateFile(path)
    return
  # On lit son contenu, remplace les variables, extrait le nouveau fichier.
  print_var("📝 Creation and edition of file {}...", path)
  try:
    with zip.open(info, "r") as buffin, open(path, "w", encoding="utf-8", newline="") as buffout:
      content: str = buffin.read().decode("utf-8")
      buffout.write(__replace_variables(content, variables))
  except: raise CantCreateEditFile(path)

def __check_zip(path: Path) -> None:
  print_var( \
  "✅ File {} was found." if path.is_file() else \
  "⚠️ File {} was not found." , path)

def __delete_zip(path: Path) -> None:
  # S'il n'existe plus on skip.
  if not path.is_file():
    print_var("⚠️ File {} not found, skipped.", path)
    return
  # On supprime le fichier.
  print_var("🗑️ Deletion of file {}...", path)
  try: path.unlink()
  except: raise CantDeleteFile(path)
  # Supprimer les dossier parents non vides pour remonter jusqu'au bon dossier.
  for parent in path.parents:
    if parent.resolve() == working.resolve(): break
    if any(parent.iterdir()): break
    print_var("📁 Deletion of folder {}...", parent)
    try: parent.rmdir()
    except: raise CantDeleteFolder(parent)

def __browse_zip(path: Path, variables: dict[str, str], type: ProcessType):
  # On ouvre le template.
  try: zip = ZipFile(path, "r")
  except: raise CantOpenTemplate(path)
  # On prepare les suffixs.
  if type == ProcessType.EXTRACT:
    suffixs: list[str] = get_value("suffixs")
  with zip:
    for info in zip.infolist():
      # Outils de merde qui mettent des backslashs non standards.
      info.filename = info.filename.replace('\\', '/')
      if info.is_dir(): continue
      # On injecte les variables dans le chemin.
      info.filename = __replace_variables(info.filename, variables)
      item: Path = Path(info.filename)
      # On bloque pas si un fichier pose problemes.
      try:
        match type:
          case ProcessType.EXTRACT: __extract_zip(item, variables, suffixs, zip, info)
          case ProcessType.DELETE: __delete_zip(item)
          case ProcessType.INTEGRITY: __check_zip(item)
      except Exception as e: print(e)

def process_zip(template: str, namespace: str, extras: list[str], type: ProcessType):
  zip: str = get_value("templates", template)
  path: Path = root / "templates" / zip
  clean: bool = False
  # On telecharge si c'est une url.
  if zip.startswith("http"):
    print_var("📥 Downloading template archive {}...", path.name)
    path = __download_zip(zip)
    clean = True
  # S'il existe pas ca crash.
  if not path.is_file(): raise TemplateNotFound(path)
  # On prepare les variables et on process.
  variables: dict[str, str] = get_injected(namespace, extras)
  try: __browse_zip(path, variables, type)
  finally:
    # Clean le tmp si c'est une url.
    if clean: __clean_zip(path)

def packinto_zip(name: str) -> None:
  # S'il existe pas on le creer.
  path: Path = root / "templates" / f"{name}.zip"
  if path.is_file(): raise TemplateAlreadyExist(path)
  try: zip = ZipFile(path, "w", ZIP_DEFLATED)
  except: raise CantCreateTemplate(path)  
  try:
    with zip:
      # On parcourt tous les fichiers et sous-dossiers
      try: files: list[Path] = working.rglob("*")
      except: raise CantListFiles(working)
      for file in files:
        if file.is_file():
          # On garde qu'un chemin relatif.
          arcname = file.relative_to(working)
          print_var("📄 Compression of file {}...", arcname)
          try: zip.write(file, arcname)
          except: raise CantCompressFile(file)
  except:
    # On nettoie le fichier incomplet.
    if path.is_file(): path.unlink()
    raise