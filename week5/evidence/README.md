# Week 5 证据清单

```text
evidence/
├── logs/
├── screenshots/
└── rosbag/
```

## 必须提交

1. `maps/map.yaml` 和 `maps/map.pgm`：真实建图结果。
2. `launch/mapping.launch.py`：已提供。
3. `rosbag/mapping_bag/`：建图过程 rosbag。
4. `screenshots/map_rviz.png`：RViz 中地图截图。
5. `screenshots/mapping_route.png`：建图路线/轨迹截图。
6. `logs/mapping_log.txt`：SLAM 建图日志。

## 生成命令

```bash
ros2 bag record /scan /odom /tf /tf_static -o evidence/rosbag/mapping_bag
ros2 run tf2_tools view_frames
ros2 bag info evidence/rosbag/mapping_bag > evidence/logs/bag_info.txt
```
