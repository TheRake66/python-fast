from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.explorer import open_folder, ExplorerInvalidPath
from libraries.message import print_error
from libraries.system import root

def parse_root(subparsers: _SubParsersAction[ArgumentParser]) -> None:
  parser: ArgumentParser = subparsers.add_parser("root", help="Open installation folder in file explorer.")
  parser.set_defaults(func=handle_root)

def handle_root(args: Namespace) -> None:
  try: open_folder(root)
  except ExplorerInvalidPath as e: 
    print_error("Can't open installation folder!", e)