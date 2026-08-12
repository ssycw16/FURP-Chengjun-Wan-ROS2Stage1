# Week 3 - Carter 底盘 bringup 与差速控制

## 本周提交要求

- 直线运动演示
- 原地旋转演示
- 小方形轨迹演示
- 稳定 `/odom`
- 有效 `/tf`
- 安全停止行为

## 内容

```text
week3/
├── README.md
├── carter_bringup/              # 可构建的 ROS 2 package
├── evidence/                    # 放入截图、日志、rosbag
└── report/
    └── week3_report.md
```

## 构建

```bash
source /opt/ros/humble/setup.bash
mkdir -p ~/ros2_ws/src
cp -r week3/carter_bringup ~/ros2_ws/src/
cd ~/ros2_ws
colcon build --symlink-install --packages-select carter_bringup
source install/setup.bash
```

## 运行

启动 fake hardware 底盘与控制器：

```bash
ros2 launch carter_bringup fake_hardware.launch.py
```

在另一个终端运行：

```bash
# 直线前进
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2}, angular: {z: 0.0}}"
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0}, angular: {z: 0.0}}"

# 原地旋转
ros2 run carter_bringup rotate_in_place --ros-args -p direction:=left -p angle:=3.14159

# 小方形轨迹
ros2 run carter_bringup square_trajectory --ros-args -p side_length:=0.6 -p linear_speed:=0.2
```

## 检查底盘状态

```bash
ros2 topic echo /odom --once
ros2 topic echo /joint_states --once
ros2 run tf2_tools view_frames
ros2 run tf2_ros tf2_echo odom base_link
ros2 run carter_bringup check_odom_tf
```

## 安全停止与 watchdog

启动 watchdog 后，当 `/cmd_vel` 超过 0.5 秒没有新速度指令时，会自动发布零速度：

```bash
ros2 run carter_bringup cmd_vel_watchdog
```

真机测试前必须确认急停按钮、串口权限、速度限制和测试区域安全。

## 证据清单

见 [evidence/README.md](evidence/README.md)。截图、日志和 bag 请使用你的真实实验结果替换。
