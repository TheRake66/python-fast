from argparse import ArgumentParser, Namespace, _SubParsersAction
from urllib.request import urlretrieve
import json, zipfile, os, uuid
from zipfile import ZipFile
from enum import Enum

# Data structure =====================================================

class FastConf:
  __data: dict = None
  @classmethod
  def get(cls) -> dict:
    if cls.__data is None:
      path = os.path.dirname(os.path.realpath(__file__))
      file = os.path.join(path, "configuration.json")
      with open(file) as buffer:
        cls.__data = json.load(buffer)
    return cls.__data

class ItemType(Enum):
  COMPONENT: str = "com"
  API_REST : str = "api"
  STYLING  : str = "sty"
  SERVICE  : str = "srv"
  LIBRARY  : str = "lib"
  LOCALE   : str = "loc"
  PAGE     : str = "pag"
  TYPE     : str = "typ"
  def __str__(self) -> str:
    return self.value

class FileExt(Enum):
  TYPESCRIPT_JSX  : str = "tsx"
  TYPESCRIPT      : str = "ts"
  PYTHON          : str = "py"
  JSON            : str = "json"
  HTML            : str = "html"
  SCSS            : str = "scss"
  def __str__(self) -> str:
    return self.value

class VarName(Enum):
  CAPITALIZE : str = r"{{capitalize_item_name}}"
  LOWER      : str = r"{{lower_item_name}}"
  UPPER      : str = r"{{upper_item_name}}"
  def __str__(self) -> str:
    return self.value

# Utils funcs ========================================================

def progress_callback(index: int, size: int, total: int) -> None:
  downloaded: int = min(index * size, total)
  percent: float = (downloaded / total) * 100 if total > 0 else 0
  print(f"\rProgression : {percent:.1f}% ({downloaded}/{total} octets)", end="", flush=True)

def download_template(url: str) -> str:
  name = str(uuid.uuid4().hex)
  urlretrieve(url, name, reporthook=progress_callback)
  return name

def unzip_file(name: str) -> None:  
  with ZipFile(name, "r") as zip:
    for item in zip.infolist():
      print(item.filename)

# New application ====================================================
  
def parse_new(subparsers: _SubParsersAction) -> None:
  parser = subparsers.add_parser("new", help="Créer une nouvelle application.")
  parser.add_argument("name", type=str, help="Nom de l'application.")
  parser.set_defaults(func=handle_new)

def handle_new(args: Namespace) -> None:
  print(f"📂 Création de l'application : {args.name}")
  url = FastConf.get()["templates"]["project"]
  unzip_file(download_template(url))

# Add item ===========================================================

def parse_add(subparsers: _SubParsersAction) -> None:
  parser = subparsers.add_parser("add", help="Ajouter un nouvel élément.")
  parser.add_argument("type", type=ItemType, choices=list(ItemType), help="Type d'élément.")
  parser.add_argument("name", type=str, help="Nom de l'élément.")
  parser.set_defaults(func=handle_add)
  
  # import Example from './pages/example.tsx'
  # <Route path='/:lang/example' element={<Example />} />
  
  # from api.routes.example import router as example
  # add_routers(example)

def handle_add(args: Namespace) -> None:
  print(f"➕ Ajout de [{args.type.value}] ({args.type.name}) -> {args.name}")

# Rename item ========================================================

def parse_ren(subparsers: _SubParsersAction) -> None:
  parser = subparsers.add_parser("ren", help="Renommer un élément existant.")
  parser.add_argument("type", type=ItemType, choices=list(ItemType), help="Type d'élément.")
  parser.add_argument("old", type=str, help="Nom actuel de l'élément.")
  parser.add_argument("new", type=str, help="Nouveau nom de l'élément.")
  parser.set_defaults(func=handle_add)

def handle_ren(args: Namespace) -> None:
  print(f"✏️  Renommage de [{args.type.value}] {args.old} -> {args.new}")

# Delete item ========================================================

def parse_del(subparsers: _SubParsersAction) -> None:
  parser = subparsers.add_parser("del", help="Supprimer un élément existant.")
  parser.add_argument("type", type=ItemType, choices=list(ItemType), help="Type d'élément.")
  parser.add_argument("name", type=str, help="Nom de l'élément.")
  parser.set_defaults(func=handle_add)

def handle_del(args: Namespace) -> None:
  print(f"🗑️  Suppression de [{args.type.value}] -> {args.name}")

# Run application ====================================================

def parse_run(subparsers: _SubParsersAction) -> None:
  parser = subparsers.add_parser("run", help="Lance les services de l'application.")
  parser.set_defaults(func=handle_add)

def handle_run(args: Namespace) -> None:
  print("🚀 Lancement de l'application...")

# Entry point ========================================================

def main():
  parser: ArgumentParser = ArgumentParser(prog="fast",
    description="Générateur de template pour créer une application fullstack Vite + FastAPI.")

  subparsers: _SubParsersAction[ArgumentParser] = parser.add_subparsers(
    dest="command", required=True, help="Sous-commandes disponibles.")

  parse_new(subparsers)
  parse_add(subparsers)
  parse_ren(subparsers)
  parse_del(subparsers)
  parse_run(subparsers)
  
  args = parser.parse_args()
  args.func(args)

if __name__ == "__main__":
  main()