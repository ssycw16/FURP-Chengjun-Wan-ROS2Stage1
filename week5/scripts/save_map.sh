#!/usr/bin/env bash
set -euo pipefail

OUT_PREFIX="${1:-maps/map}"
OUT_DIR="$(dirname "$OUT_PREFIX")"
mkdir -p "$OUT_DIR"

ros2 run nav2_map_server map_saver_cli -f "$OUT_PREFIX"
