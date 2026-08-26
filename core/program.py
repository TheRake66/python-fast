from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.setting import load_json
import sys

def main():
  try:
    
    load_json()
    
    parser: ArgumentParser = ArgumentParser(prog="fast",
      description="Template-based file generator for creating an app quickly.")

    subparsers: _SubParsersAction[ArgumentParser] = parser.add_subparsers(
      dest="command", required=True, help="Available subcommands...")

    from commands.create import parse_create
    from commands.delete import parse_delete
    from commands.start import parse_start
    from commands.infos import parse_infos
    from commands.load import parse_load
    from commands.root import parse_root
    from commands.open import parse_open
    from commands.git import parse_git

    parse_create(subparsers)
    parse_delete(subparsers)
    parse_start(subparsers)
    parse_infos(subparsers)
    parse_load(subparsers)
    parse_root(subparsers)
    parse_open(subparsers)
    parse_git(subparsers)
    
    args: Namespace = parser.parse_args()
    args.func(args)
    
  except Exception as e:
    print(e)
    sys.exit(1)

if __name__ == "__main__":
  main()