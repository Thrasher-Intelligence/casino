#!/bin/bash

# Resolve the repo directory
REPO_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Directories to exclude
EXCLUDES="--exclude-dir=venv,.venv,__pycache__,airlock"

# Ensure cloc is installed
if ! command -v cloc &> /dev/null; then
    echo "cloc is not installed. Install it with: sudo apt install cloc"
    exit 1
fi

# Get current time
NOW=$(date +"%H:%M:%S")
HOUR_COLOR="\033[1;36m"     # Cyan
MIN_COLOR="\033[1;35m"      # Magenta
SEC_COLOR="\033[1;33m"      # Yellow
RESET_COLOR="\033[0m"

# Print ASCII clock
echo -e ""
echo -e "       ⏰ CLOCTOWER STATUS"
echo -e ""
echo -e "       ${HOUR_COLOR}${NOW:0:2}${RESET_COLOR} : ${MIN_COLOR}${NOW:3:2}${RESET_COLOR} : ${SEC_COLOR}${NOW:6:2}${RESET_COLOR}"
echo -e ""
echo -e "       🗼 Initiating code count for: $REPO_DIR"
echo -e ""

# Run cloc
cloc $EXCLUDES "$REPO_DIR"
