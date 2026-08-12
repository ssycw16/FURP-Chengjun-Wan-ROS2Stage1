#!/usr/bin/env bash
set -euo pipefail

source /opt/ros/humble/setup.bash

echo "== ROS distro =="
echo "ROS_DISTRO=${ROS_DISTRO:-not set}"

echo "== ros2 doctor =="
ros2 doctor || true

echo "== nodes =="
ros2 node list || true

echo "== topics =="
ros2 topic list || true

echo "== tf frames =="
ros2 run tf2_tools view_frames || true

echo "== controllers =="
ros2 control list_controllers || true

echo "Check complete. Review the output for missing nodes or broken TF."
