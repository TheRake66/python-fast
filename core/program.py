from argparse import ArgumentParser, Namespace, _SubParsersAction

import json, zipfile, os, uuid
from zipfile import ZipFile, ZipInfo
from typing import Any


def main():
  parser: ArgumentParser = ArgumentParser(prog=AssemblyInfo.COMMAND,
    description="Générateur de template pour créer une application fullstack Vite + FastAPI.")

  subparsers: _SubParsersAction[ArgumentParser] = parser.add_subparsers(
    dest="command", required=True, help="Sous-commandes disponibles.")

  parse_new(subparsers)
  parse_add(subparsers)
  parse_rename(subparsers)
  parse_delete(subparsers)
  parse_run(subparsers)
  
  args: Namespace = parser.parse_args()
  args.func(args)

if __name__ == "__main__":
  main()