from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.message import print_info, print_success, print_error
from libraries.configuration import get_value
from subprocess import Popen

def parse_run(subparsers: _SubParsersAction[ArgumentParser]) -> None:
  scripts: list[str] = get_value("services").keys()
  parser: ArgumentParser = subparsers.add_parser("run", help="Run a service in the system terminal.")
  parser.add_argument("key", type=str, choices=scripts, help="Service key in the configuration file.")
  parser.set_defaults(func=handle_run)

def handle_run(args: Namespace) -> None:
  print_info(f"Running service: {args.key}...")
  command: str = get_value("services", args.key)
  try:
    Popen(command, shell=True)
    print_success("Successfully started.")
  except Exception as e:
    print_error("Cannot run this service!", e)