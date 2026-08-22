from enum import Enum

class BaseEnum(str, Enum):

  def __str__(self) -> str:
    return self.value

  @classmethod
  def names(cls) -> list[str]:
    return [item.name for item in cls]

  @classmethod
  def values(cls) -> list[str]:
    return [item.value for item in cls]