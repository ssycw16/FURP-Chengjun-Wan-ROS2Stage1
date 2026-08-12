# 复现实验说明

## 环境

- Ubuntu 22.04
- ROS 2 Humble
- Linux2Go 或等价虚拟机/真机环境
- Carter 差速底盘或 fake hardware

## 1. 安装依赖

```bash
sudo apt update
sudo apt install -y \
  ros-humble-ros2-control \
  ros-humble-ros2-controllers \
  ros-humble-diff-drive-controller \
  ros-humble-mock-components \
  ros-humble-robot-state-publisher \
  ros-humble-xacro \
  ros-humble-slam-toolbox \
  ros-humble-nav2-bringup \
  ros-humble-robot-localization \
  ros-humble-tf2-tools \
  ros-humble-rosbag2
```

## 2. 构建 Week 3 package

```bash
source /opt/ros/humble/setup.bash
mkdir -p ~/ros2_ws/src
cp -r week3/carter_bringup ~/ros2_ws/src/
cd ~/ros2_ws
colcon build --symlink-install --packages-select carter_bringup
source install/setup.bash
```

## 3. 运行完整系统

```bash
ros2 launch week8/launch/full_bringup.launch.py
```

## 4. 验证系统

```bash
ros2 node list
ros2 topic list
ros2 run tf2_tools view_frames
ros2 topic echo /odometry/filtered --once
```

## 5. 记录数据

```bash
bash week8/scripts/collect_evidence.sh
```

## 6. 建图复现

```bash
ros2 launch week5/launch/mapping.launch.py
# 在环境中移动机器人
cd week5
bash scripts/save_map.sh maps/map
```

## 7. 导航复现

```bash
ros2 launch week6/launch/navigation.launch.py
python3 week6/scripts/send_goal.py 1.0 2.0 1.57
```

## 8. 注意事项

- 真机测试前必须完成 Week 7 safety checklist。
- 如果使用 rosbag 回放，所有节点必须使用一致的 `use_sim_time`。
- 大 bag 和视频不要直接提交到普通 GitHub 仓库。
