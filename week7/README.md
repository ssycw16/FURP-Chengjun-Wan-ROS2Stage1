# Week 7 - 室外 waypoint 导航与 GPS / RTK 扩展

## 本周提交要求

- 室外 waypoint 文件
- 室外 bag 或演示视频
- 定位配置文件
- 安全 checklist
- 失败案例分析

如果 GPS / RTK 不稳定，可降级为：

- 轮速计 + IMU 的短距离室外 waypoint 测试
- GPS 数据记录和离线分析
- 仿真中的 waypoint navigation 演示

本目录同时提供 Nav2 waypoint 方案和死推算降级方案。

## 内容

```text
week7/
├── README.md
├── config/
│   ├── robot_localization_global.yaml
│   ├── navsat_transform.yaml
│   └── waypoints/
│       ├── outdoor_waypoints.yaml
│       └── fallback_waypoints.yaml
├── launch/
│   └── outdoor_bringup.launch.py
├── scripts/
│   ├── follow_waypoints.py
│   ├── follow_waypoints_dead_reckoning.py
│   ├── analyze_gps_log.py
│   └── record_outdoor_data.sh
├── safety/
│   └── outdoor_safety_checklist.md
├── evidence/
└── report/
    └── week7_report.md
```

## 1. 记录室外数据

```bash
cd week7
bash scripts/record_outdoor_data.sh ~/carter_bags/week7_outdoor
```

记录后检查 GPS fix：

```bash
ros2 topic echo /fix --once
ros2 topic echo /imu --once
ros2 topic echo /odometry/global --once
ros2 bag info ~/carter_bags/week7_outdoor
```

## 2. GPS / RTK 方案

```bash
ros2 launch week7/launch/outdoor_bringup.launch.py
python3 week7/scripts/follow_waypoints.py \
  week7/config/waypoints/outdoor_waypoints.yaml
```

使用前必须确认：

- `/fix` 有有效 fix。
- `navsat_transform` 输出 `/odometry/gps`。
- `map -> odom` 方向正确。
- RTK 精度满足实验要求。

## 3. 降级方案：轮速计 + IMU 短距离 waypoint

```bash
python3 week7/scripts/follow_waypoints_dead_reckoning.py \
  week7/config/waypoints/fallback_waypoints.yaml
```

该脚本直接读取 `/odom`，用简单的比例控制器向 `odom` 坐标系中的目标点移动，只适合 5-10 米内的低速短距离测试。

## 4. GPS 离线分析

把 `ros2 topic echo /fix` 输出整理成 CSV 后：

```bash
python3 week7/scripts/analyze_gps_log.py gps_log.csv
```

## 安全提醒

室外测试必须先完成 [safety/outdoor_safety_checklist.md](safety/outdoor_safety_checklist.md) 中的检查项。

## 证据

见 [evidence/README.md](evidence/README.md)。
