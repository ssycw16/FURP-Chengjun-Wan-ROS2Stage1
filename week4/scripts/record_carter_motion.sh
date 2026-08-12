#!/usr/bin/env bash
set -euo pipefail

OUT_DIR="${1:-$HOME/carter_bags/week4_motion}"
mkdir -p "$OUT_DIR"

ros2 bag record \
  /cmd_vel \
  /odom \
  /odometry/filtered \
  /scan \
  /imu \
  /tf \
  /tf_static \
  /joint_states \
  -o "$OUT_DIR"
