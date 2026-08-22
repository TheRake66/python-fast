from libraries.structure import ItemUrl, VarName, VarValue, FileExt, ItemType
from urllib.request import urlretrieve
from zipfile import ZipFile
from pathlib import Path
import uuid, re, os

def __progress_callback(index: int, size: int, total: int) -> None:
  downloaded: int = min(index * size, total)
  percent: float = (downloaded / total) * 100 if total > 0 else 0
  print(f"\rTéléchargement : {percent:.1f}% ({downloaded}/{total} octets)", end="", flush=True)

def __contains_variables(text: str) -> bool:
  pattern: str = r"\{\{(\w+)\}\}"
  return re.search(pattern, text)

def __replace_variables(text: str, values: VarValue) -> str:
  for var in VarName:
    if var.value in text:
      value: str = str(getattr(values, var.name))
      text: str = text.replace(var.value, value)
  return text

def get_zip(item: ItemType) -> str:
  return str(getattr(ItemUrl, item.name))

def download_zip(url: ItemUrl) -> str:
  name: str = str(uuid.uuid4().hex)
  urlretrieve(url, name, reporthook=__progress_callback)
  print()
  return name

def clean_zip(path: str) -> None:
  os.remove(path)

def extract_zip(path: str, values: VarValue) -> None:
  with ZipFile(path, "r") as zip:
    for info in zip.infolist():
      extracted: str = zip.extract(info, ".")
      # Renomme le fichier ou dossier s'il a une ou des 
      # variables dans son chemin.
      if __contains_variables(extracted):
        renamed: str = __replace_variables(extracted, values)
        os.rename(extracted, renamed)
        extracted = renamed
      # Check si c'est un fichier, s'il est dans la liste
      # des extension et s'il contient des variables.
      object = Path(extracted)
      if object.is_dir(): continue
      if not object.suffix in FileExt.values(): continue
      content: str = object.read_text()
      if not content: continue
      # Remplace les variables dans le contenu.
      if __contains_variables(content):
        modified: str = __replace_variables(content, values)
        object.write_text(modified)