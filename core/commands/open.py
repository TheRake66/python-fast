from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.explorer import open_folder, ExplorerInvalidPath
from libraries.message import print_error
from pathlib import Path

def parse_open(subparsers: _SubParsersAction[ArgumentParser]) -> None:
  parser: ArgumentParser = subparsers.add_parser("open", help="Open current folder in file explorer.")
  parser.set_defaults(func=handle_open)

def handle_open(args: Namespace) -> None:
  try: open_folder(Path.cwd())
  except ExplorerInvalidPath as e: 
    print_error("Can't open current folder!", e)