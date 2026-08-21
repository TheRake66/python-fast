from libraries.garbage import BaseEnum

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

class ItemType(BaseEnum):
  ENUMERATION: str = "enu"
  COMPONENT:   str = "com"
  STYLING:     str = "sty"
  SERVICE:     str = "srv"
  LIBRARY:     str = "lib"
  LOCALE:      str = "loc"
  PAGE:        str = "pag"
  TYPE:        str = "typ"
  API:         str = "api"

class FileExt(BaseEnum):
  TYPESCRIPT_JSX: str = "tsx"
  TYPESCRIPT:     str = "ts"
  PYTHON:         str = "py"
  JSON:           str = "json"
  HTML:           str = "html"
  SCSS:           str = "scss"

class VarName(BaseEnum):
  CAPITALIZE_NAME: str = r"{{capitalize_name}}"
  LOWER_NAME:      str = r"{{lower_name}}"
  UPPER_NAME:      str = r"{{upper_name}}"
  LANGUAGE_SHORT:  str = r"{{language_short}}"
  LANGUAGE_FULL:   str = r"{{language_full}}"
  LANGUAGE_NAME:   str = r"{{language_name}}"
  BACKEND_IP:      str = r"{{backend_ip}}"
  BACKEND_PORT:    str = r"{{backend_port}}"