from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.structure import ActionType, AssemblyInfo
from libraries.configuration import configuration

def parse_new(subparsers: _SubParsersAction) -> None:
  parser: ArgumentParser = subparsers.add_parser(ActionType.NEW,
    help="Créer une nouvelle application.")
  parser.add_argument("name", type=str,
    help="Nom de l'application.")
  parser.set_defaults(func=handle_new)

def handle_new(args: Namespace) -> None:
  print(f"📂 Création de l'application : {args.name}")
  url: str = configuration["templates"]["project"]
  unzip_file(download_template(url))
  print(f"Ajouter votre premiere page avec : {AssemblyInfo.COMMAND} {ActionType.ADD} {ItemType.PAGE} ma-page")
  print(f"Lancer l'application avec : {AssemblyInfo.COMMAND} {ActionType.RUN}")