
def emoji_bullet(message: str) -> str:
  return f"🔹 {message}"

def emoji_pin(message: str) -> str:
  return f"📌 {message}"

def emoji_check(message: str) -> str:
  return f"✅ {message}"
  
def emoji_triangle(message: str) -> str:
  return f"⚠️ {message}"

def emoji_cross(message: str) -> str:
  return f"❌ {message}"

def emoji_tools(message: str)-> str:
  return f"🛠️ {message}"

def emoji_down(message: str)-> str:
  return f"👇 {message}"

def print_info(message: str) -> None:
  print(emoji_pin(message))

def print_success(message: str) -> None:
  print(emoji_check(message))
  
def print_warning(message: str) -> None:
  print(emoji_triangle(message))

def print_error(message: str, error: Exception = None) -> None:
  print(emoji_cross(message))
  if error:
    print_under(emoji_tools("Reason:"))
    print(error)

def print_list(label: str, items: list[str]) -> None:
  __print_under(emoji_down(f"{label}:"))
  for item in items: 
    print(emoji_bullet(item))

def print_dict(label: str, items: dict[str, str]) -> None:
  __print_under(emoji_down(f"{label}:"))
  for key, value in items.items():
    print(emoji_bullet(f"{key} ({value})"))

def __print_under(message: str) -> None:
  print()
  print(message)
  print((len(message)+1) * "-")