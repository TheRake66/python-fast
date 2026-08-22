from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.template import download_zip, extract_zip, clean_zip
from libraries.structure import ActionType, AssemblyInfo, ItemType, ItemUrl, VarValue
from libraries.configuration import configuration
from libraries.garbage import load_values
import os, subprocess

def parse_new(subparsers: _SubParsersAction) -> None:
  parser: ArgumentParser = subparsers.add_parser(ActionType.NEW, help="Créer une nouvelle application.")
  parser.add_argument("name", type=str, help="Nom de l'application.")
  parser.set_defaults(func=handle_new)

def handle_new(args: Namespace) -> None:
  print(f"🎨 Création de l'application : {args.name}...")
  os.makedirs(args.name, exist_ok=True)
  os.chdir(args.name)
  uuid: str = download_zip(ItemUrl.PROJECT)
  values: VarValue = load_values(args.name)
  extract_zip(uuid, values)
  clean_zip(uuid)
  print("✅ Création terminée !")
  __open_vscode()
  __show_tips()

def __show_tips() -> None:
  if not configuration["tips"]: return
  print(f"Ajouter votre premiere page avec : {AssemblyInfo.COMMAND} {ActionType.ADD} {ItemType.PAGE} ma-page")
  print(f"Lancer l'application avec : {AssemblyInfo.COMMAND} {ActionType.RUN}")
  
def __open_vscode() -> None:
  if not configuration["vscode"]: return
  try: subprocess.run(["code", "."], shell=True)
  except: pass