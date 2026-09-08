#!/usr/bin/env bash
set -euo pipefail
TARGET_DIR="${HOME}/.gemini/config/plugins/bean-cup"
echo "🗑️  Removing ${TARGET_DIR}..."
python3 -c "import shutil, os; p = os.path.expanduser('~/.gemini/config/plugins/bean-cup'); shutil.rmtree(p) if os.path.exists(p) else None"
echo "✅ Uninstalled bean-cup."
