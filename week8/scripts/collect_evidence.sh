#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EVIDENCE_DIR="$SCRIPT_DIR/../evidence"
LOG_DIR="$EVIDENCE_DIR/logs"
SCREEN_DIR="$EVIDENCE_DIR/screenshots"
BAG_DIR="$EVIDENCE_DIR/rosbag"
VIDEO_DIR="$EVIDENCE_DIR/videos"

mkdir -p "$LOG_DIR" "$SCREEN_DIR" "$BAG_DIR" "$VIDEO_DIR"

source /opt/ros/humble/setup.bash

{
  echo "Captured at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "ROS_DISTRO=${ROS_DISTRO:-not set}"
  ros2 doctor
  echo
  echo "== node list =="
  ros2 node list
  echo
  echo "== topic list =="
  ros2 topic list
  echo
  echo "== tf frames =="
  ros2 run tf2_tools view_frames
  echo
  echo "== controllers =="
  ros2 control list_controllers
} > "$LOG_DIR/system_check.txt" 2>&1 || true

echo "Evidence collected:"
echo "  $LOG_DIR/system_check.txt"
echo "Put screenshots into $SCREEN_DIR"
echo "Put rosbag into $BAG_DIR"
echo "Put demo video into $VIDEO_DIR"
