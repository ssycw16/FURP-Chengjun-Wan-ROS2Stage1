# Week 6 证据清单

```text
evidence/
├── logs/
├── screenshots/
└── rosbag/
```

## 必须提交

1. `screenshots/initial_pose.png`：initial pose 设置后的 AMCL 粒子。
2. `screenshots/single_goal.png`：单点目标、global path、local costmap。
3. `screenshots/multi_goal.png`：多点导航。
4. `screenshots/dynamic_obstacle.png`：动态障碍阻挡和恢复过程。
5. `logs/dynamic_obstacle_test.csv`：测试脚本输出。
6. `logs/nav2_log.txt`：Nav2 日志。
7. `rosbag/nav_test_bag/`：可选，导航过程 rosbag。

## 检查命令

```bash
ros2 node list | grep nav
ros2 topic list | grep costmap
ros2 topic echo /cmd_vel --once
ros2 run tf2_tools view_frames
```
