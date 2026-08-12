# Week 5 - 室内 SLAM 建图

## 本周提交要求

- 室内地图文件（`map.yaml` + 图片）
- mapping launch 文件
- 建图 rosbag
- 地图质量报告
- 至少一个失败案例和原因分析

## 内容

```text
week5/
├── README.md
├── config/
│   └── slam_toolbox_mapping.yaml
├── launch/
│   └── mapping.launch.py
├── maps/
│   ├── map.yaml
│   ├── map.pgm              # 示例地图，真机建图后替换
│   ├── generate_example_map.py
│   └── README.md
├── scripts/
│   └── save_map.sh
├── evidence/
└── report/
    └── week5_report.md
```

## 1. 启动建图

先确保底盘、LiDAR、TF 正常：

```bash
source /opt/ros/humble/setup.bash
ros2 launch week5/launch/mapping.launch.py
```

真机或 bag 回放时把 `/scan`、`/odom`、`/tf` 提供给 SLAM Toolbox。

## 2. 保存地图

```bash
cd week5
bash scripts/save_map.sh maps/map
```

保存后会生成 `maps/map.yaml` 和 `maps/map.pgm`。

## 3. 建图路线建议

- 从机器人起点出发，低速沿墙走一圈。
- 在走廊交叉口和拐角减速，保证 scan matching 稳定。
- 避免在动态物体、镜子、玻璃、狭窄门口前长时间停留。
- 建图完成后回到起点附近，帮助形成 loop closure。

## 4. 检查地图质量

```bash
ros2 topic hz /scan
ros2 topic echo /odom --once
ros2 run tf2_tools view_frames
ros2 bag info <mapping_bag>
```

## 5. 示例地图说明

本目录附带一张 `map.pgm` 示例地图，用于验证 Week 6 离线流程。正式提交时建议使用真实 `map_saver_cli` 生成的地图替换，并在报告中写明地图来源。

## 证据

见 [evidence/README.md](evidence/README.md)。
