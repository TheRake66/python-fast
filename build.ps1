Get-ChildItem -Path "core" -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
Compress-Archive -Path 'core\*' -DestinationPath 'release.zip' -Force