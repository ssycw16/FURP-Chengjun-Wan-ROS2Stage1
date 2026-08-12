# FURP-Chengjun-Wan-ROS2Stage1
FURP ROS2机器人科研项目

## ROS2 Carter Bootcamp 作业（Week 3 - Week 8）

每周作业已整理为独立目录，可直接在虚拟机中拉取仓库后运行。

| 周次 | 目录 | 内容 |
| --- | --- | --- |
| Week 3 | [week3/](week3/README.md) | Carter 底盘 bringup、diff_drive_controller、fake hardware、运动脚本 |
| Week 4 | [week4/](week4/README.md) | LiDAR/IMU、robot_localization EKF、rosbag 录制、odom 对比 |
| Week 5 | [week5/](week5/README.md) | SLAM Toolbox 建图、地图文件、质量报告 |
| Week 6 | [week6/](week6/README.md) | Nav2 参数、单点/多点导航、动态避障 |
| Week 7 | [week7/](week7/README.md) | 室外 waypoint、GPS/RTK、航位推算降级方案 |
| Week 8 | [week8/](week8/README.md) | Capstone 集成、full bringup、最终报告与复现说明 |

### 快速开始（Ubuntu 22.04 + ROS 2 Humble）

```bash
source /opt/ros/humble/setup.bash
mkdir -p ~/ros2_ws/src
cp -r week3/carter_bringup ~/ros2_ws/src/
cd ~/ros2_ws
colcon build --symlink-install --packages-select carter_bringup
source install/setup.bash
ros2 launch carter_bringup fake_hardware.launch.py
```

各周详细命令见对应目录的 README；环境依赖见 [docs/environment.md](docs/environment.md)，提交检查见 [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)。
