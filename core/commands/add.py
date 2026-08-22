from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.template import download_zip, extract_zip, clean_zip, get_zip
from libraries.garbage import load_values, ensure_project
from libraries.structure import ActionType, ItemType, VarValue
from libraries.configuration import configuration

def parse_add(subparsers: _SubParsersAction) -> None:
  parser: ArgumentParser = subparsers.add_parser(ActionType.ADD, help="Ajouter un nouvel élément.")
  parser.add_argument("type", type=ItemType, choices=ItemType.values(), help="Type d'élément.")
  parser.add_argument("name", type=str, help="Nom de l'élément.")
  parser.set_defaults(func=handle_add)

def handle_add(args: Namespace) -> None:
  ensure_project()
  print(f"➕ Ajout de l'élément : {args.name} ({args.type.name})...")
  zip: str = get_zip(args.type)
  uuid: str = download_zip(zip)
  values: VarValue = load_values(args.name)
  extract_zip(uuid, values)
  clean_zip(uuid)
  print("✅ Ajout terminé !")
  __show_tips(args.type, values)

def __print_tip(tip: str) -> None:
  print(f"💡 {tip} :")

def __show_tips(item: ItemType, values: VarValue) -> None:
  if not configuration["tips"]: return
  match item:
    case ItemType.COMPONENT:
      __print_tip("Ajouter une section dans vos fichiers de langue")
      print("{")
      print("  \"components\": {")
      print("    \"" + values.LOWER_NAME + "\": {")
      print("")
      print("    }")
      print("  }")
      print("}")
    case ItemType.STYLE:
      __print_tip("Importez votre fichier de style dans le fichier \"main.tsx\"")
      print(f"import './styles/{values.LOWER_NAME}.scss'")
    case ItemType.LOCALE:
      __print_tip("Ajoutez votre langue dans l'énumération \"language.type.ts\"")
      print("export const Language = {")
      print(f"  {values.CAPITALIZE_NAME}: '{values.LOWER_NAME}'")
      print("} as const;")
      __print_tip("Importez votre fichier de langue dans la librairie \"language.ts\"")
      print(f"import {values.LOWER_NAME} from '../locales/{values.LOWER_NAME}.json';")
      __print_tip("Chargez votre langue dans les langues de i18n dans \"language.ts\"")
      print("resources: {")
      print("  " + values.LOWER_NAME + ": { translation: " + values.LOWER_NAME + " }")
      print("}")
    case ItemType.PAGE:
      __print_tip("Ajouter une section dans vos fichiers de langue")
      print("{")
      print("  \"pages\": {")
      print("    \"" + values.LOWER_NAME + "\": {")
      print("")
      print("    }")
      print("  }")
      print("}")
      __print_tip("Ajouter une route dans le fichier \"main.tsx\"")
      print("<Route path='/:lang/" + values.LOWER_NAME + "' element={<" + values.CAPITALIZE_NAME + " />} />")
    case ItemType.API:
      __print_tip("Ajouter votre route au fichier \"main.py\"")
      print(f"from api.routes.{values.LOWER_NAME} import router as {values.LOWER_NAME}")
      print(f"add_routers({values.LOWER_NAME})")