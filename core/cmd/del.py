def parse_delete(subparsers: _SubParsersAction) -> None:
  parser: Any = subparsers.add_parser(ActionType.DELETE, help="Supprimer un élément existant.")
  parser.add_argument("type", type=ItemType, choices=list(ItemType), help="Type d'élément.")
  parser.add_argument("name", type=str, help="Nom de l'élément.")
  parser.set_defaults(func=handle_delete)

def handle_delete(args: Namespace) -> None:
  print(f"🗑️ Suppression de [{args.type.value}] -> {args.name}")
