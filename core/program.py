from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.structure import AssemblyInfo

def main():
  parser: ArgumentParser = ArgumentParser(
    prog=AssemblyInfo.COMMAND,
    description="Générateur de template pour créer une application fullstack Vite + FastAPI.")

  subparsers: _SubParsersAction[ArgumentParser] = parser.add_subparsers(
    dest="command", 
    required=True, 
    help="Sous-commandes disponibles.")

  from commands.new import parse_new
  from commands.add import parse_add
  from commands.rename import parse_rename
  from commands.delete import parse_delete
  from commands.run import parse_run

  parse_new(subparsers)
  parse_add(subparsers)
  parse_rename(subparsers)
  parse_delete(subparsers)
  parse_run(subparsers)
  
  args: Namespace = parser.parse_args()
  args.func(args)
  
  print()

if __name__ == "__main__":
  main()