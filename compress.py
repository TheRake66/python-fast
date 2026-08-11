import os, shutil

try:
  for dir in os.listdir():
    if dir.startswith("template_"):
      print(f"📦 Compression du dossier : {dir}...")
      shutil.make_archive(base_name=dir, format="zip", root_dir=dir)
  print(f"✅ Compression terminé.")
except Exception as ex:
  print(f"❌ Erreur lors de la compression ! ({ex})")
