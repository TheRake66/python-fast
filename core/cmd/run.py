def parse_run(subparsers: _SubParsersAction) -> None:
  parser: Any = subparsers.add_parser(ActionType.RUN, help="Lance les services de l'application.")
  parser.set_defaults(func=handle_run)

def handle_run(args: Namespace) -> None:
  print("🚀 Lancement de l'application...")
