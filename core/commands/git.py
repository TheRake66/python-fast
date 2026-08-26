from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.message import print_error
import webbrowser

def parse_git(subparsers: _SubParsersAction[ArgumentParser]) -> None:
  parser: ArgumentParser = subparsers.add_parser("git", help="Open source code repository in web browser.")
  parser.set_defaults(func=handle_git)

def handle_git(args: Namespace) -> None:
  if not webbrowser.open("https://github.com/TheRake66/python-fast"):
    print_error("Can't open repository!")