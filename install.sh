#!/bin/bash

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