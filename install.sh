#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Create a Python virtual environment
echo "Creating virtual environment..."
python3 -m venv python3

# Activate the virtual environment
echo "Activating virtual environment..."
source python3/bin/activate

# Install requirements from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "Error: requirements.txt not found!"
    exit 1
fi

NAMES=("stripchat" "chaturbate")
URLS=("https://raw.githubusercontent.com/community-plugins/streamlink-plugins/cloudscraper/plugins/stripchat.py"
      "https://raw.githubusercontent.com/community-plugins/streamlink-plugins/cloudscraper/plugins/chaturbate.py")
PYTHON_VERSION=$(python3 --version 2>&1)
PYTHON=$(echo "$PYTHON_VERSION" | sed -E 's/Python ([0-9]+\.[0-9]+).*/python\1/')
DEST_DIR="python3/lib/$PYTHON/site-packages/streamlink/plugins"

# Download and move the plugins
for i in "${!URLS[@]}"; do
    echo "Downloading ${NAMES[$i]} plugin..."
    curl -o "${NAMES[$i]}.py" "${URLS[$i]}"
    echo "Moving ${NAMES[$i]}.py to $DEST_DIR..."
    mv "${NAMES[$i]}.py" "$DEST_DIR/"
done

# Execute the main.py script
if [ -f "main.py" ]; then
    echo "Executing main.py..."
    echo "python3 main.py"
else
    echo "Error: main.py not found!"
    deactivate
    exit 1
fi

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate

echo "Script completed successfully!"
