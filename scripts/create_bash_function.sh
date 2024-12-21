#!/bin/bash

# Path to the .bashrc file
BASHRC_FILE="$HOME/.bashrc"

# Function to add
FUNCTION="workdir () 
{ 
    if [[ \"\$1\" == \"set\" ]]; then
        handler_workdir set;
    else
        cd \$(handler_workdir);
    fi
}
"

# Check if the function is already defined in the .bashrc file
if ! grep -q "workdir ()" "$BASHRC_FILE"; then
    echo "The 'workdir' function is not defined. Adding it to the end of the .bashrc file..."
    echo "$FUNCTION" >> "$BASHRC_FILE"
    echo "The 'workdir' function was successfully added."
else
    echo "The 'workdir' function is already defined in .bashrc."
fi

