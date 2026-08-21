def parse_new(subparsers: _SubParsersAction) -> None:
  parser: Any = subparsers.add_parser(ActionType.NEW, help="Créer une nouvelle application.")
  parser.add_argument("name", type=str, help="Nom de l'application.")
  parser.set_defaults(func=handle_new)

def handle_new(args: Namespace) -> None:
  print(f"📂 Création de l'application : {args.name}")
  url: str = FastConf.get()["templates"]["project"]
  unzip_file(download_template(url))
  print(f"Ajouter votre premiere page avec : {AssemblyInfo.COMMAND} {ActionType.ADD} {ItemType.PAGE} ma-page")
  print(f"Lancer l'application avec : {AssemblyInfo.COMMAND} {ActionType.RUN}")