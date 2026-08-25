from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.exlorer import open_folder, root, ExplorerInvalidPath
from libraries.message import print_error

def parse_root(subparsers: _SubParsersAction[ArgumentParser]) -> None:
  parser: ArgumentParser = subparsers.add_parser("root", 
    help="Open installation folder in file explorer.")
  parser.set_defaults(func=handle_root)

def handle_root(args: Namespace) -> None:
  try: open_folder(root)
  except ExplorerInvalidPath as e: 
    print_error("Cannot open installation folder!", e)