#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Ensure the Python 3 interpreter is available
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it first."
    exit 1
fi

# Check if the script accepts up to 5 arguments
if [ "$#" -gt 5 ]; then
    echo "Usage: $0 [arg1] [arg2] [arg3] [arg4] [arg5]"
    exit 1
fi

echo "Activating virtual environment..."
source python3/bin/activate

# Run main.py with the provided arguments
echo "Running main.py with arguments: $@"
python3 main.py "$@"

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "Script execution completed!"
