# Week 6 - Nav2 室内导航与避障

## 本周提交要求

- 单点室内导航
- 多点室内导航
- 简单动态障碍避障
- 一个失败案例和 root-cause 分析

## 内容

```text
week6/
├── README.md
├── config/
│   ├── nav2_params.yaml
│   └── multi_waypoints.yaml
├── launch/
│   └── navigation.launch.py
├── scripts/
│   ├── send_goal.py
│   ├── send_multiple_goals.py
│   └── dynamic_obstacle_test.py
├── evidence/
└── report/
    └── week6_report.md
```

## 1. 前置条件

- Week 3 底盘 `/odom`、`/tf` 正常。
- Week 4 LiDAR `/scan` 正常。
- Week 5 地图 `map.yaml` 可用。

## 2. 启动导航

```bash
source /opt/ros/humble/setup.bash
ros2 launch week6/launch/navigation.launch.py
```

启动后打开 RViz：

```bash
rviz2
```

如果需要指定其他地图：

```bash
ros2 launch week6/launch/navigation.launch.py \
  map:=$(pwd)/week5/maps/map.yaml
```

先用 `2D Pose Estimate` 设置 initial pose，再观察 AMCL 粒子是否收敛。

## 3. 单点导航

```bash
python3 week6/scripts/send_goal.py 1.0 2.0 1.57
```

也可以在 RViz 中点击 `Nav2 Goal` 发送目标。

## 4. 多点导航

编辑 `config/multi_waypoints.yaml`，然后：

```bash
python3 week6/scripts/send_multiple_goals.py \
  week6/config/multi_waypoints.yaml
```

## 5. 动态障碍测试

```bash
# 终端 1：运行导航
# 终端 2：运行测试脚本，脚本会发送目标并记录 /cmd_vel
python3 week6/scripts/dynamic_obstacle_test.py 2.0 1.0 0.0
```

测试流程：

1. 第一次不放置障碍，记录导航时间。
2. 第二次在路径中途放置一个纸箱/椅子。
3. 观察机器人是否停止、等待或重规划。
4. 移除障碍后观察机器人是否继续完成目标。
5. 保存截图、`/cmd_vel` CSV 和日志。

## 6. 调参原则

- 先检查 TF 和 costmap，再调参数。
- 速度参数从保守值开始：`max_vel_x=0.5`、`max_vel_theta=1.0`。
- 膨胀半径太大会导致无路可走，太小会擦墙。
- 不要一次改多个参数，每次只改一个并记录结果。

## 证据

见 [evidence/README.md](evidence/README.md)。
