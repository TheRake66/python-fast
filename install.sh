#!/bin/bash
set -e

CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

ZIP_URL="https://github.com/TheRake66/python-fast/raw/refs/heads/main/release.zip"
APP_DIR="Fast"
TMP_ZIP="/tmp/install_$$.zip"
ERROR_MSG=""

if [[ "$OSTYPE" == darwin* ]]; then
    APP_PATH="$HOME/Library/Application Support/$APP_DIR"
else
    APP_PATH="${XDG_CONFIG_HOME:-$HOME/.config}/$APP_DIR"
fi

VENV_PY="$APP_PATH/.venv"
VENV_BIN="$VENV_PY/bin"

trap 'echo -e "${RED}${ERROR_MSG}${NC}"; exit 1' ERR

ERROR_MSG="Unable to download file archive!"
echo -e "${CYAN}Download in progress...${NC}"
curl -sSL "$ZIP_URL" -o "$TMP_ZIP" 2>/dev/null

ERROR_MSG="Unable to decompress file archive!"
echo -e "${CYAN}Decompression...${NC}"
mkdir -p "$APP_PATH"
unzip -qo "$TMP_ZIP" -d "$APP_PATH" 2>/dev/null || [ $? -eq 1 ]

ERROR_MSG="Unable to install the command using pip!"
echo -e "${CYAN}Installation with pip...${NC}"
python3 -m venv "$VENV_PY"
source "$VENV_BIN/activate"
pip install -e "$APP_PATH" -q --disable-pip-version-check

ERROR_MSG="Unable to create symlink!"
echo -e "${CYAN}Creating symlink...${NC}"
mkdir -p "$HOME/.local/bin"
ln -sf "$VENV_BIN/fast" "$HOME/.local/bin/fast"

ERROR_MSG="Unable to clean the installation!"
echo -e "${CYAN}Cleaning installation...${NC}"
rm -f "$TMP_ZIP"

echo -e "${GREEN}Installation done.${NC}"