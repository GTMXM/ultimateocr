#!/usr/bin/env bash
set -e

MESSAGE="$1"

if [ -z "$MESSAGE" ]; then
    MESSAGE="Project update"
fi

echo "========================================"
echo " UltimateOCR Sync Pipeline"
echo "========================================"

echo
echo "Repository:"
git rev-parse --show-toplevel

echo
echo "Current Branch:"
git branch --show-current

echo
echo "Modified Files:"
git status --short

if git diff --quiet && git diff --cached --quiet; then
    echo
    echo "No changes detected."
    exit 0
fi

echo
echo "----------------------------------------"
echo "Running Quality Checks..."
echo "----------------------------------------"

# ---------- Python syntax ----------
echo
echo "[1/4] Python Syntax Check"

python -m compileall ultimateocr

# ---------- PyTest ----------
echo
echo "[2/4] PyTest"

if [ -d tests ]; then
    pytest -q
else
    echo "tests/ not found. Skipped."
fi

# ---------- Ruff ----------
echo
echo "[3/4] Ruff"

if command -v ruff >/dev/null 2>&1; then
    ruff check .
else
    echo "ruff not installed. Skipped."
fi

# ---------- Black ----------
echo
echo "[4/4] Black"

if command -v black >/dev/null 2>&1; then
    black --check .
else
    echo "black not installed. Skipped."
fi

echo
echo "----------------------------------------"
echo "Creating Commit..."
echo "----------------------------------------"

git add .

git commit -m "$MESSAGE"

echo
echo "----------------------------------------"
echo "Pushing..."
echo "----------------------------------------"

git push origin main

echo
echo "========================================"
echo "Sync Complete"
echo "========================================"

echo
git log -1 --stat
