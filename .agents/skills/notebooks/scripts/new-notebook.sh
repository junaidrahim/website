#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"

if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
  echo 'usage: new-notebook.sh <slug> "<title>" [technical|undertones|essay]' >&2
  exit 2
fi

SLUG="$1"
TITLE="$2"
KIND="${3:-technical}"
[ "$KIND" != "essay" ] || KIND="undertones"

export NOTEBOOK_REPO_ROOT="$REPO_ROOT"
exec uv run --project "$REPO_ROOT" --frozen python "$REPO_ROOT/main.py" new "$SLUG" "$TITLE" --kind "$KIND"
