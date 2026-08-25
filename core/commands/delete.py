from argparse import ArgumentParser, Namespace, _SubParsersAction, REMAINDER
from libraries.message import print_info, print_success
from libraries.template import process_zip, ProcessType
from libraries.configuration import get_value

def parse_delete(subparsers: _SubParsersAction) -> None:
  templates: list[str] = get_value("templates").keys()
  parser: ArgumentParser = subparsers.add_parser("delete", help="Delete an existing element in your project from a template.")
  parser.add_argument("key", type=str, choices=templates, help="Template key in the configuration file.")
  parser.add_argument("name", type=str, help="Name of the element to delete.")
  parser.add_argument("extras", nargs=REMAINDER, help="Additional constants to add to the process.")
  parser.set_defaults(func=handle_delete)

def handle_delete(args: Namespace) -> None:
  print_info(f"Deleting item: {args.name}...")
  process_zip(args.key, args.name, args.extras, ProcessType.DELETE)
  print_success("Successfully deleted.")