from argparse import ArgumentParser, Namespace, _SubParsersAction, REMAINDER
from libraries.message import print_info, print_success
from libraries.template import process_zip, ProcessType
from libraries.setting import get_value

def parse_add(subparsers: _SubParsersAction) -> None:
  templates: list[str] = get_value("templates").keys()
  parser: ArgumentParser = subparsers.add_parser("add",  help="Add a new element to your project from a template.")
  parser.add_argument("key", type=str, choices=templates, help="Template key in the settings file.")
  parser.add_argument("name", type=str, help="Name of the element to add.")
  parser.add_argument("extras", nargs=REMAINDER, help="Additional constants to add to the process.")
  parser.set_defaults(func=handle_add)

def handle_add(args: Namespace) -> None:
  print_info(f"Adding item: {args.name}...")
  process_zip(args.key, args.name, args.extras, ProcessType.EXTRACT)
  print_success("Successfully added.")