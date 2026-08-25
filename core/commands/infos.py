from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.message import print_info, print_list, print_dict
from libraries.setting import get_used, get_value

def parse_infos(subparsers: _SubParsersAction) -> None:
  parser: ArgumentParser = subparsers.add_parser("infos", 
    help="Display many informations about current settings.")
  parser.set_defaults(func=handle_infos)

def handle_infos(args: Namespace) -> None:
  current: str = get_used()
  services: list[str] = get_value("services").keys()
  templates: list[str] = get_value("templates").keys()
  constants: dict[str, str] = get_value("constants")
  modules: list[str] = get_value("modules")
  suffixs: list[str] = get_value("suffixs")
  print_info(f"Current settings is: {current}")
  print()
  print_list(f"Available services:", services)
  print()
  print_list(f"Available templates:", templates)
  print()
  print_dict(f"Defined constants:", constants)
  print()
  print_list(f"Loaded modules:", modules)
  print()
  print_list(f"Editable files:", suffixs)