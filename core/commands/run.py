from argparse import ArgumentParser, Namespace, _SubParsersAction
from libraries.garbage import ensure_project, get_npm, get_venv
from libraries.structure import ActionType
from subprocess import Popen

def parse_run(subparsers: _SubParsersAction[ArgumentParser]) -> None:
  parser: ArgumentParser = subparsers.add_parser(ActionType.RUN, help="Lance les services de l'application.")
  parser.set_defaults(func=handle_run)

def handle_run(args: Namespace) -> None:
  ensure_project()
  print("🚀 Lancement de l'application...")
  __start_uvicorn()
  __start_vite()
  print("✅ Lancement effectué !")

def __start_uvicorn() -> None:
  print('⌛ Lancement de Uvicorn...')
  python = get_venv('python')
  command = [python, '-m', 'uvicorn', 'api.main:application', '--reload']
  if UVICORN['hosted']: command += ['--host', UVICORN['address']]
  Popen(command + ['--port', str(UVICORN['port'])])

def __start_vite() -> None:
  print('⌛ Lancement de Vite...')
  npm = get_npm()
  command = [npm, 'run', 'dev', '--']
  if VITE['hosted']: command += ['--host', VITE['address']]
  Popen(command + ['--port', str(VITE['port'])])