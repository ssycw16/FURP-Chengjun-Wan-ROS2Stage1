# Week 4 - LiDAR、IMU、rosbag 与状态估计

## 本周提交要求

- 一段 Carter 运动 rosbag
- `ekf.yaml`
- raw odometry 与 filtered odometry 对比
- 传感器 TF 检查表
- RViz 中 LiDAR 截图

## 内容

```text
week4/
├── README.md
├── config/
│   ├── ekf.yaml
│   └── sensor_tf_checklist.md
├── launch/
│   └── ekf.launch.py
├── scripts/
│   ├── record_carter_motion.sh
│   └── compare_odometry.py
├── evidence/
└── report/
    └── week4_report.md
```

## 1. 记录 Carter 运动数据

```bash
cd week4
bash scripts/record_carter_motion.sh ~/carter_bags/week4_motion
```

推荐至少记录一次直线、一次转弯，并在运动中移动机器人，让 `/odom` 和 `/odometry/filtered` 有明显差异可对比。

## 2. 启动 EKF

```bash
source /opt/ros/humble/setup.bash
ros2 launch week4/launch/ekf.launch.py
```

## 3. 回放 bag 并对比 odom

```bash
ros2 bag play ~/carter_bags/week4_motion
python3 week4/scripts/compare_odometry.py --ros-args -p output_file:=odom_comparison.csv
```

`compare_odometry.py` 会在收到 `/odometry/filtered` 时，把对应时刻最近的 `/odom` 一起写入 CSV，并打印最大位置偏差。

## 4. 检查传感器 TF

```bash
ros2 run tf2_ros tf2_echo base_link laser_link
ros2 run tf2_ros tf2_echo base_link imu_link
ros2 topic hz /scan
ros2 topic echo /imu --once
ros2 topic echo /odometry/filtered --once
```

## 5. 常见问题

- LiDAR frame 错误：检查 `laser_link` 是否在 TF tree 中，`/scan.frame_id` 必须与 TF 一致。
- IMU 方向不一致：检查安装方向，必要时在驱动或 EKF 中修正。
- EKF 不输出：检查 `world_frame`、`odom_frame`、`base_link_frame` 是否与 TF 一致。
- bag 回放时间戳异常：确认 playback 时 `use_sim_time` 一致。

## 证据

见 [evidence/README.md](evidence/README.md)。截图、日志和 bag 请使用真实实验数据。
