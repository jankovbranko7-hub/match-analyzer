#!/bin/bash
# Installiert die Abhaengigkeiten aus requirements.txt (numpy, scipy).
# Frische Container von Claude Code on the web haben sie nicht vorinstalliert,
# ohne sie bricht analyse/modell.py sofort ab.
set -euo pipefail

# Nur im Cloud-Container. Lokal verwaltet der Nutzer seine Umgebung selbst.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"

pip install --quiet --root-user-action=ignore --requirement requirements.txt
python3 -c "import numpy, scipy"   # Abbruch, falls die Installation nicht griff
