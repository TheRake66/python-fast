from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.structure import ActionType, ItemType

def parse_rename(subparsers: _SubParsersAction[ArgumentParser]) -> None:
  parser: ArgumentParser = subparsers.add_parser(ActionType.RENAME, help="Renomme un élément existant.")
  parser.add_argument("type", type=ItemType, choices=ItemType.values(), help="Type d'élément.")
  parser.add_argument("old", type=str, help="Nom de l'élément existant.")
  parser.add_argument("new", type=str, help="Nouveau nom de l'élément.")
  parser.set_defaults(func=handle_rename)

def handle_rename(args: Namespace) -> None:
  print(f"✏️ Renommage de l'élément : {args.old} en {args.new} ({args.type.name})...")
  print("✅ Renommage terminé !")