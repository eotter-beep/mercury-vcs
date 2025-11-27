#!/bin/bash

# Name of the alias
ALIAS_NAME="mercury"

# Command the alias should run
ALIAS_COMMAND="~/cli.py"

# Determine the shell config file
if [ -n "$ZSH_VERSION" ]; then
    CONFIG_FILE="$HOME/.zshrc"
else
    CONFIG_FILE="$HOME/.bashrc"
fi

# Add the alias to the shell config if it doesn't already exist
if ! grep -q "alias $ALIAS_NAME=" "$CONFIG_FILE"; then
    echo "alias $ALIAS_NAME='$ALIAS_COMMAND'" >> "$CONFIG_FILE"
    echo "Alias '$ALIAS_NAME' added to $CONFIG_FILE"
else
    echo "Alias '$ALIAS_NAME' already exists in $CONFIG_FILE"
fi

# Reload the shell configuration (optional for the current script)
source "$CONFIG_FILE"
