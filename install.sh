#!/bin/bash
# This script installs the jcc command line tool

# Check for xclip dependency
if ! command -v xclip 2>&1 >/dev/null; then
    printf "Xclip is not installed but is required for jcc to function.\n"
    printf "Install xclip? (y/n): "
    read -n1 response
    if [ "$response" = "y" ]; then
        sudo apt-get install xclip
    else
        printf "\nExiting..."
        exit 1
    fi
fi

# Define the source and destination paths
SRC_PATH="jcc/jcc.py"
DEST_PATH="/usr/local/bin/jcc"

# Check if the source file exists
if [ ! -f "$SRC_PATH" ]; then
    echo "Source file $SRC_PATH does not exist."
    exit 1
fi

# Copy the source file to the destination
cp "$SRC_PATH" "$DEST_PATH"

# Make the destination file executable
chmod +x "$DEST_PATH"

echo "Installation complete. You can now run 'jcc' from the command line."