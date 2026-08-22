from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.structure import ActionType, ItemType

def parse_delete(subparsers: _SubParsersAction) -> None:
  parser: ArgumentParser = subparsers.add_parser(ActionType.DELETE, help="Supprimer un élément existant.")
  parser.add_argument("type", type=ItemType, choices=ItemType.values(), help="Type d'élément.")
  parser.add_argument("name", type=str, help="Nom de l'élément.")
  parser.set_defaults(func=handle_delete)

def handle_delete(args: Namespace) -> None:
  print(f"🗑️ Suppression de l'élément : {args.name} ({args.type.name})...")
  print("✅ Suppression terminée !")
