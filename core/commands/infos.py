from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.message import print_list, print_dict, print_var
from libraries.setting import get_used, get_value
from libraries.variable import from_modules

def parse_infos(subparsers: _SubParsersAction) -> None:
  parser: ArgumentParser = subparsers.add_parser("infos", help="Display many informations about current settings.")
  parser.set_defaults(func=handle_infos)

def handle_infos(args: Namespace) -> None:
  current: str = get_used()
  variables: dict[str, str] = from_modules()
  services: list[str] = get_value("services").keys()
  templates: list[str] = get_value("templates").keys()
  constants: dict[str, str] = get_value("constants")
  modules: list[str] = get_value("modules")
  suffixs: list[str] = get_value("suffixs")
  print_var("⚙️ Current settings is {}.", current)
  print_list("🚀 Available services", services)
  print_list("📦 Available templates", templates)
  print_dict("🔡 Defined constants", constants)
  print_list("🧩 Loaded modules", modules)
  print_dict("🔡 Module variables", variables)
  print_list("📄 Editable files", suffixs)