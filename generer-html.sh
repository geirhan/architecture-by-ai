#!/bin/bash
#
# Genererer HTML-versjoner av alle markdown-rapporter.
# Wrapper som kaller Python-scriptet.
#
# Bruk: ./generer-html.sh
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/generer-html.py"
