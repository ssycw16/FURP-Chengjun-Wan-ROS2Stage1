# Week 3 证据清单

请在对应目录放入你的真实实验结果：

```text
evidence/
├── logs/          # ros2 topic echo、ros2 doctor、controller 日志
├── screenshots/   # 直线/旋转/方形轨迹、/odom、TF tree、RViz
└── rosbag/        # 可选：运动过程 rosbag
```

## 必须记录的命令输出

```bash
ros2 topic echo /odom --once
ros2 topic echo /joint_states --once
ros2 run tf2_ros tf2_echo odom base_link
ros2 run tf2_tools view_frames
ros2 control list_controllers
```

## 建议截图

1. `ros2 run tf2_tools view_frames` 生成的 TF tree。
2. RViz 中显示 `/odom` 和 TF。
3. 方形轨迹的位移曲线，或 `/odom` 的 x/y 轨迹。
4. watchdog 超时后 `/cmd_vel` 变 0 的日志。
