from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.explorer import open_folder
from libraries.system import root

def parse_root(subparsers: _SubParsersAction[ArgumentParser]) -> None:
  parser: ArgumentParser = subparsers.add_parser("root", help="Open installation folder in file explorer.")
  parser.set_defaults(func=handle_root)

def handle_root(args: Namespace) -> None:
  print("📂 Opening installation folder...")
  open_folder(root)