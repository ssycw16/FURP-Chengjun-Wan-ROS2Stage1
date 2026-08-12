# Week 7 证据清单

```text
evidence/
├── logs/
├── screenshots/
└── rosbag/
```

## 必须提交

1. `rosbag/week7_outdoor/` 或 `videos/outdoor_demo.mp4`。
2. `config/waypoints/outdoor_waypoints.yaml` 或 `fallback_waypoints.yaml`。
3. `config/robot_localization_global.yaml`。
4. `config/navsat_transform.yaml`。
5. `safety/outdoor_safety_checklist.md`。
6. `logs/gps_log.csv`：GPS 离线分析数据。
7. `logs/outdoor_test_log.txt`：测试日志。
8. `screenshots/outdoor_rviz.png`：室外轨迹截图。

## 分析命令

```bash
python3 scripts/analyze_gps_log.py logs/gps_log.csv
```
