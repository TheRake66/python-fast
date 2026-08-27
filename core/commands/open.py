from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.explorer import open_folder
from libraries.system import working

def parse_open(subparsers: _SubParsersAction[ArgumentParser]) -> None:
  parser: ArgumentParser = subparsers.add_parser("open", help="Open current folder in file explorer.")
  parser.set_defaults(func=handle_open)

def handle_open(args: Namespace) -> None:
  print("📂 Opening current folder...")
  open_folder(working)