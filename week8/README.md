# Week 8 - Capstone 集成与最终演示

## 最终提交要求

- Git 仓库
- launch 文件
- 参数文件
- 地图文件
- rosbag 文件
- 演示视频
- final report
- 复现实验说明

## 内容

```text
week8/
├── README.md
├── launch/
│   └── full_bringup.launch.py
├── config/
│   └── final_params.md
├── docs/
│   ├── final_report.md
│   └── reproduction.md
├── scripts/
│   ├── check_system.sh
│   └── collect_evidence.sh
├── evidence/
└── README.md
```

## 一键启动完整系统

```bash
source /opt/ros/humble/setup.bash
ros2 launch week8/launch/full_bringup.launch.py
```

该 launch 会依次包含：

1. Week 3 Carter fake hardware / diff_drive_controller
2. Week 4 EKF
3. Week 6 Nav2 导航

如果只需要建图，请单独运行 Week 5 mapping launch。

## 最终演示 10-15 分钟建议流程

1. 系统架构：展示 node/topic/TF 图，2 分钟。
2. Carter bringup：启动和健康检查，2 分钟。
3. 室内地图/定位：展示地图和 AMCL，2 分钟。
4. 室内导航与避障：单点/多点/动态障碍，4 分钟。
5. 室外 waypoint 或降级演示：2 分钟。
6. 失败与经验、未来改进：2 分钟。

## 提交前检查

```bash
bash week8/scripts/check_system.sh
bash week8/scripts/collect_evidence.sh
```

完整报告见 [docs/final_report.md](docs/final_report.md)，复现步骤见 [docs/reproduction.md](docs/reproduction.md)。
