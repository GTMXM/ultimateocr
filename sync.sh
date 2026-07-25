#!/bin/bash
set -e

MESSAGE="$1"

if [ -z "$MESSAGE" ]; then
    MESSAGE="Project update"
fi

echo "=============================="
echo "UltimateOCR Sync"
echo "=============================="

git add .

if git diff --cached --quiet; then
    echo "No changes to commit."
    exit 0
fi

git commit -m "$MESSAGE"

git push origin main

echo ""
echo "Sync completed successfully."
