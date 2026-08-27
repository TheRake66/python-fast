from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.message import print_success, print_var
from libraries.template import packinto_zip
from libraries.explorer import open_folder
from libraries.system import root, working

def parse_pack(subparsers: _SubParsersAction) -> None:
  parser: ArgumentParser = subparsers.add_parser("pack", help="Pack current folder into a template.")
  parser.add_argument("name", type=str, nargs="?", default=None, help="Name of the output archive for template.")
  parser.set_defaults(func=handle_pack)

def handle_pack(args: Namespace) -> None:
  if not args.name: args.name = working.stem
  print_var("📦 Pack current folder into {} template...", args.name)
  packinto_zip(args.name)
  print_success('Successfully packed.')
  print('📂 Opening templates folder...')
  open_folder(root / "templates")