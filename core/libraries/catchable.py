from libraries.message import emoji_cross

class Catchable(Exception):
  message: str = "Unknown error!"
  
  def __init__(self, *args: list[str]):
    if args: 
      formatted: tuple[str] = tuple(f"\"{arg}\"" for arg in args)
      message: str = self.message.format(*formatted)
    else: message: str = self.message
    super().__init__(emoji_cross(message))