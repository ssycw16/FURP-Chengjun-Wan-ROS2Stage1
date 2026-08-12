# Week 4 证据清单

```text
evidence/
├── logs/
├── screenshots/
└── rosbag/
```

## 必须提交

1. `rosbag/week4_motion/`：Carter 运动 rosbag。
2. `screenshots/lidar_rviz.png`：RViz 中 LiDAR 截图。
3. `screenshots/raw_vs_filtered.png`：raw odometry 与 filtered odometry 轨迹对比。
4. `logs/odometry_comparison.csv`：对比脚本输出。
5. `logs/sensor_tf_check.txt`：`tf2_echo` 和 topic echo 输出。

## 生成命令

```bash
ros2 bag info ~/carter_bags/week4_motion > evidence/logs/bag_info.txt
ros2 topic hz /scan > evidence/logs/scan_hz.txt
ros2 topic echo /imu --once > evidence/logs/imu_once.txt
ros2 topic echo /odometry/filtered --once > evidence/logs/filtered_once.txt
```
