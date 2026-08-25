from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.message import print_info, print_success
from libraries.configuration import set_used, get_list

def parse_load(subparsers: _SubParsersAction) -> None:
  files: list[str] = get_list()
  parser: ArgumentParser = subparsers.add_parser("load", help="Load another configuration file.")
  parser.add_argument("name", type=str, choices=files, help="Filename of configuration without suffix.")
  parser.set_defaults(func=handle_load)

def handle_load(args: Namespace) -> None:
  print_info(f"Load configuration: {args.name}...")
  set_used(args.name)
  print_success("Successfully loaded.")