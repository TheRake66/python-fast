from libraries.configuration import configuration
from libraries.enumeration import BaseEnum
from dataclasses import dataclass

class AssemblyInfo(BaseEnum):
  NAME:    str = "Fast"
  COMMAND: str = "fast"
  VERSION: str = "1.0.0.0"

class ActionType(BaseEnum):
  DELETE: str = "del"
  RENAME: str = "ren"
  NEW:    str = "new"
  ADD:    str = "add"
  RUN:    str = "run"

class FileExt(BaseEnum):
  TYPESCRIPT_SX: str = ".tsx"
  JAVASCRIPT_SX: str = ".jsx"
  TYPESCRIPT:     str = ".ts"
  JAVASCRIPT:     str = ".js"
  PYTHON:         str = ".py"
  JSON:           str = ".json"
  HTML:           str = ".html"
  SCSS:           str = ".scss"

class ItemType(BaseEnum):
  ENUMERATION: str = "enu"
  COMPONENT:   str = "com"
  SERVICE:     str = "srv"
  LIBRARY:     str = "lib"
  LOCALE:      str = "loc"
  STYLE:       str = "sty"
  PAGE:        str = "pag"
  TYPE:        str = "typ"
  API:         str = "api"

@dataclass
class ItemUrl:
  ENUMERATION: str = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/templates/base_enum.zip"
  COMPONENT:   str = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/templates/base_component.zip"
  PROJECT:     str = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/templates/base_project.zip"
  SERVICE:     str = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/templates/base_service.zip"
  LIBRARY:     str = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/templates/base_library.zip"
  LOCALE:      str = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/templates/base_locale.zip"
  STYLE:       str = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/templates/base_style.zip"
  PAGE:        str = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/templates/base_page.zip"
  TYPE:        str = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/templates/base_type.zip"
  API:         str = "https://github.com/TheRake66/python-fast/raw/refs/heads/main/templates/base_api.zip"

class VarName(BaseEnum):
  CAPITALIZE_NAME: str = r"{{capitalize_name}}"
  LOWER_NAME:      str = r"{{lower_name}}"
  UPPER_NAME:      str = r"{{upper_name}}"
  NAMESPACE_SLASH: str = r"{{namespace_slash}}"
  NAMESPACE_BACK:  str = r"{{namespace_back}}"
  NAMESPACE_DOTS:  str = r"{{namespace_dots}}"
  LANGUAGE_SHORT:  str = r"{{language_short}}"
  LANGUAGE_FULL:   str = r"{{language_full}}"
  LANGUAGE_NAME:   str = r"{{language_name}}"
  BACKEND_IP:      str = r"{{backend_ip}}"
  BACKEND_PORT:    str = r"{{backend_port}}"
  CREATOR_NAME:    str = r"{{creator_name}}"

@dataclass
class VarValue:
  CAPITALIZE_NAME: str = ""
  LOWER_NAME:      str = ""
  UPPER_NAME:      str = ""
  NAMESPACE_SLASH: str = ""
  NAMESPACE_BACK:  str = ""
  NAMESPACE_DOTS:  str = ""
  LANGUAGE_SHORT:  str = configuration["frontend"]["language"]["short"]
  LANGUAGE_FULL:   str = configuration["frontend"]["language"]["full"]
  LANGUAGE_NAME:   str = configuration["frontend"]["language"]["name"]
  BACKEND_IP:      str = configuration["backend"]["server"]["address"]
  BACKEND_PORT:    str = configuration["backend"]["server"]["port"]
  CREATOR_NAME:    str = configuration["creator"]