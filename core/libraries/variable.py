from libraries.setting import get_value
from libraries.catchable import Catchable
import os, importlib

class InvalidNamespace(Catchable): message="Namespace {} is not valid!"
class InvalidModule(Catchable): message="Module {} is not valid!"
class InvalidConstant(Catchable): message="Constants from settings are not valid!"
class InvalidExtra(Catchable): message="Extra constant {} is not valid!"

def __from_extras(extras: list[str]) -> dict[str, str]:
  variables: dict[str, str] = {}
  for extra in extras:
    try:
      split: list[str] = extra.split("=")
      key, value = split[0], split[1]
      if key.startswith("--"): key = key[2:]
      variables[key] = value
    except: raise InvalidExtra(extra)
  return variables

def __from_constants() -> dict[str, str]:
  try: return get_value("constants")
  except: raise InvalidConstant()

def __from_modules() -> dict[str, str]:
  modules: list[str] = get_value("modules")
  variables: dict[str, str] = {}
  for module in modules:
    try:
      loaded = importlib.import_module(f"modules.{module}")
      variables |= getattr(loaded, "variables")
    except: raise InvalidModule(module)
  return variables

def __from_namespace(namespace: str) -> dict[str, str]:
  try:
    parts: list[str] = namespace.split("-")
    packages: list[str] = parts[0:-1]
    relative: str = len(packages) * "../"
    name: str = parts[-1]
    path: str = f"{relative}{name}"
    ossep: str = os.sep.join(parts)
    slash: str = "\\".join(parts)
    back: str = "/".join(parts)
    dots: str = ".".join(parts)
    dash: str = "-".join(parts)
    under: str = "-".join(parts)

    return {                                         # Example: pkg1-pkg2-name
      "lower_name":            name.lower(),     # name
      "upper_name":            name.upper(),     # NAME
      "title_name":            name.title(),     # Name
      
      "relative_dir":          relative,         # ../../
      "relative_parent":       f"../{relative}", # ../../../
      
      "relative_path_lower":   path.lower(),     # ../../name
      "relative_path_upper":   path.upper(),     # ../../NAME
      "relative_path_title":   path.title(),     # ../../Name
      
      "namespace_ossep_lower": ossep.lower(),    # pkg1\pkg2\name
      "namespace_ossep_upper": ossep.upper(),    # PKG1\PKG2\NAME
      "namespace_ossep_title": ossep.title(),    # Pkg1\Pkg2\Name
    
      "namespace_slash_lower": slash.lower(),    # pkg1\pkg2\name
      "namespace_slash_upper": slash.upper(),    # PKG1\PKG2\NAME
      "namespace_slash_title": slash.title(),    # Pkg1\Pkg2\Name

      "namespace_back_lower":  back.lower(),     # pkg1/pkg2/name
      "namespace_back_upper":  back.upper(),     # PKG1/PKG2/NAME
      "namespace_back_title":  back.title(),     # Pkg1/Pkg2/Name

      "namespace_dash_lower":  dash.lower(),     # pkg1-pkg2-name
      "namespace_dash_upper":  dash.upper(),     # PKG1-PKG2-NAME
      "namespace_dash_title":  dash.title(),     # Pkg1-Pkg2-Name

      "namespace_under_lower": under.lower(),    # pkg1_pkg2_name
      "namespace_under_upper": under.upper(),    # PKG1_PKG2_NAME
      "namespace_under_title": under.title(),    # Pkg1_Pkg2_Name
      
      "namespace_dots_lower":  dots.lower(),     # pkg1.pkg2.name
      "namespace_dots_upper":  dots.upper(),     # PKG1.PKG2.NAME
      "namespace_dots_title":  dots.title()      # Pkg1.Pkg2.Name
    }
  except: raise InvalidNamespace(namespace)

def __add_braces(variables: dict[str, str]) -> dict[str, str]:
  return {"{{" + key + "}}": value \
    for key, value in variables.items()}

def get_injected(namespace: str, extras: list[str]) -> dict[str, str]:
  return __add_braces(
    __from_namespace(namespace) | \
    __from_modules() | \
    __from_constants() | \
    __from_extras(extras))