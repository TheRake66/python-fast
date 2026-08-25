#!/bin/bash
echo "Installation..."

# ================================================
ZIP_URL="https://github.com/TheRake66/python-fast/raw/refs/heads/main/release.zip"
APP_FOLDER="Fast"
TEMP_ZIP="/tmp/install_${RANDOM}_${RANDOM}.zip"
if [[ "$OSTYPE" == "darwin"* ]]; then
    DEST_DIR="$HOME/Library/Application Support/$APP_FOLDER"
else
    DEST_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/$APP_FOLDER"
fi

# ================================================
if command -v curl &> /dev/null; then
    curl -sSL "$ZIP_URL" -o "$TEMP_ZIP"
elif command -v wget &> /dev/null; then
    wget -q "$ZIP_URL" -O "$TEMP_ZIP"
else
    echo "Curl or wget is required to download the file!"
    exit 1
fi
if [ $? -ne 0 ]; then
    echo "Download failed. Check your internet connection!"
    exit 1
fi

# ================================================
mkdir -p "$DEST_DIR"
if command -v unzip &> /dev/null; then
    unzip -q "$TEMP_ZIP" -d "$DEST_DIR"
else
    echo "Unzip command is required to decompress the archive!"
    rm -f "$TEMP_ZIP"
    exit 1
fi
if [ $? -ne 0 ]; then
    echo "Decompression failed!"
    rm -rf "$DEST_DIR"
    rm -f "$TEMP_ZIP"
    exit 1
fi

# ================================================
cd "$DEST_DIR" || exit 1
pip install -e .
if [ $? -ne 0 ]; then
    echo "Unable to install the command using pip!"
    rm -rf "$DEST_DIR"
    rm -f "$TEMP_ZIP"
    exit 1
fi

# ================================================
rm -f "$TEMP_ZIP"
echo "Installation done."