from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.message import print_success, print_error, print_var
from libraries.system import new_terminal
from libraries.setting import get_value

def parse_start(subparsers: _SubParsersAction[ArgumentParser]) -> None:
  scripts: list[str] = get_value("services").keys()
  parser: ArgumentParser = subparsers.add_parser("start", help="Start a service in the system terminal.")
  parser.add_argument("key", type=str, choices=scripts, help="Service key in the settings file.")
  parser.set_defaults(func=handle_start)

def handle_start(args: Namespace) -> None:
  command: str = get_value("services", args.key)
  print_var('🚀 Service startup {}...', args.key)
  new_terminal(command)