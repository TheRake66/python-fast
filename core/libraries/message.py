
def __print_under(message: str) -> None:
  print()
  print(message)
  print((len(message)+1) * "-")
  
def print_info(message: str) -> None:
  print(f"📌 {message}")

def print_success(message: str) -> None:
  print(f"✅ {message}")
  
def print_warning(message: str) -> None:
  print(f"⚠️ {message}")

def print_error(message: str, error: Exception = None) -> None:
  print(f"❌ {message}")
  if error:
    __print_under("🛠️ Reason:")
    print(error)

def print_var(message: str, *variables: list[str]) -> None:
  formatted: tuple[str] = tuple(f'"{variable}"' for variable in variables)
  print(message.format(*formatted))

def print_list(label: str, items: list[str]) -> None:
  __print_under(f"{label}:")
  for item in items: 
    print(f"🔹 {item}")

def print_dict(label: str, items: dict[str, str]) -> None:
  __print_under(f"{label}:")
  for key, value in items.items():
    print(f"🔹 {key} ({value})")

def format_size(bytes: int) -> str:
  for symbol in ['o', 'Ko', 'Mo', 'Go', 'To']:
    if bytes < 1024.0:
      return f"{bytes:.2f} {symbol}"
    bytes /= 1024.0
  return f"{bytes:.2f} Po"