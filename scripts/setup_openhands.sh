#!/bin/bash
# Sets up OpenHands (https://github.com/All-Hands-AI/OpenHands) in a Python 3.12 venv.
set -e

VENV_DIR="${OPENHANDS_VENV:-$HOME/.openhands-venv}"

if ! command -v python3.12 &>/dev/null; then
    echo "Error: Python 3.12 is required but not found." >&2
    exit 1
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment at $VENV_DIR ..."
    python3.12 -m venv "$VENV_DIR"
fi

echo "Installing openhands-ai ..."
"$VENV_DIR/bin/pip" install --quiet --upgrade openhands-ai

echo "OpenHands installed successfully."
echo "  Version: $("$VENV_DIR/bin/python" -c 'import openhands; print(openhands.__version__)')"
echo "  Activate: source $VENV_DIR/bin/activate"
echo "  Run CLI:  $VENV_DIR/bin/python -m openhands.core.cli"
