from urllib.request import urlretrieve
from zipfile import ZipFile, ZipInfo
from enum import Enum
import uuid

class BaseEnum(Enum):
  def __str__(self) -> str:
    return self.value

def progress_callback(index: int, size: int, total: int) -> None:
  downloaded: int = min(index * size, total)
  percent: float = (downloaded / total) * 100 if total > 0 else 0
  print(f"\rProgression : {percent:.1f}% ({downloaded}/{total} octets)", end="", flush=True)

def download_template(url: str) -> str:
  name: str = str(uuid.uuid4().hex)
  urlretrieve(url, name, reporthook=progress_callback)
  return name

def unzip_file(path: str) -> None:  
  with ZipFile(path, "r") as zip:
    for info in zip.infolist():
      process_zipinfo(info)

def process_zipinfo(info: ZipInfo):
  print(info)
  pass