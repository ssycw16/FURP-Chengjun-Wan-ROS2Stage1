#!/usr/bin/env bash
set -euo pipefail

OUT_DIR="${1:-$HOME/carter_bags/week7_outdoor}"
mkdir -p "$OUT_DIR"

ros2 bag record \
  /fix \
  /imu \
  /odom \
  /odometry/filtered \
  /odometry/global \
  /odometry/gps \
  /tf \
  /tf_static \
  /cmd_vel \
  -o "$OUT_DIR"
