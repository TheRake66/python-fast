from argparse import ArgumentParser, Namespace, _SubParsersAction, REMAINDER
from libraries.message import print_success, print_var
from libraries.template import process_zip, ProcessType
from libraries.setting import get_value

def parse_create(subparsers: _SubParsersAction) -> None:
  templates: list[str] = get_value("templates").keys()
  parser: ArgumentParser = subparsers.add_parser("create", help="Create a new element from a template.")
  parser.add_argument("key", type=str, choices=templates, help="Template key in the settings file.")
  parser.add_argument("name", type=str, help="Name of the element to add.")
  parser.add_argument("extras", nargs=REMAINDER, help="Additional constants to add to the process.")
  parser.set_defaults(func=handle_create)

def handle_create(args: Namespace) -> None:
  print_var("🎨 Creation of item {}...", args.name)
  process_zip(args.key, args.name, args.extras, ProcessType.EXTRACT)
  print_success("Successfully created.")