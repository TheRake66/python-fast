def parse_add(subparsers: _SubParsersAction) -> None:
  parser: Any = subparsers.add_parser(ActionType.ADD, help="Ajouter un nouvel élément.")
  parser.add_argument("type", type=ItemType, choices=list(ItemType), help="Type d'élément.")
  parser.add_argument("name", type=str, help="Nom de l'élément.")
  parser.set_defaults(func=handle_add)

def handle_add(args: Namespace) -> None:
  print(f"➕ Ajout de [{args.type.value}] ({args.type.name}) -> {args.name}")
  print(args)
  #match args.type.value:
  #    case ItemType.:
  #        return "Bad request"
  #    case 404:
  #        return "Not found"
  #    case 418:
  #        return "I'm a teapot"
  # import Example from './pages/example.tsx'
  # <Route path='/:lang/example' element={<Example />} />
  # from api.routes.example import router as example
  # add_routers(example)