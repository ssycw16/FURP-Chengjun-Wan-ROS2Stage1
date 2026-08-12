# 环境配置

## 推荐环境

- Ubuntu 22.04（课程使用 Linux2Go）
- ROS 2 Humble
- Carter 差速底盘或对应仿真/fake hardware
- Python 3.10+
- colcon

## 安装 ROS 2 Humble

```bash
sudo apt update
sudo apt install -y ros-humble-desktop
sudo apt install -y ros-humble-ros2-control ros-humble-ros2-controllers
sudo apt install -y ros-humble-diff-drive-controller ros-humble-mock-components
sudo apt install -y ros-humble-xacro ros-humble-robot-state-publisher
sudo apt install -y ros-humble-slam-toolbox ros-humble-nav2-bringup
sudo apt install -y ros-humble-robot-localization ros-humble-map-server
sudo apt install -y ros-humble-tf2-tools ros-humble-rosbag2
sudo apt install -y ros-humble-navigation2
```

如果无法安装，请优先检查：

```bash
echo $ROS_DISTRO
source /opt/ros/humble/setup.bash
ros2 doctor
```

## 创建 workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

## 每次新终端必做

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
export ROS_DOMAIN_ID=0
```

## 常见问题

1. `package not found`：检查 `AMENT_PREFIX_PATH` 和 `colcon build` 后是否 `source install/setup.bash`。
2. 权限问题：真机串口通常需要将用户加入 `dialout` 组，`sudo usermod -aG dialout $USER` 后重新登录。
3. 时间同步问题：EKF 和 bag 回放前确保 `use_sim_time` 与实际运行模式一致。
4. TF 断裂：优先查看 `ros2 run tf2_tools view_frames` 和 `ros2 topic echo /tf_static`。
