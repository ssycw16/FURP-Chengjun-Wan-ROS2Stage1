# 传感器 TF 检查表

| 项目 | 期望 | 检查命令 | 实际结果 |
|---|---|---|---|
| odom -> base_link | 动态 TF，由 diff_drive_controller 发布 | `ros2 run tf2_ros tf2_echo odom base_link` | `【需要替换】` |
| base_link -> laser_link | 静态 TF，位于车体前上方 | `ros2 run tf2_ros tf2_echo base_link laser_link` | `【需要替换】` |
| base_link -> imu_link | 静态 TF，安装方向正确 | `ros2 run tf2_ros tf2_echo base_link imu_link` | `【需要替换】` |
| `/scan.frame_id` | 等于 laser_link | `ros2 topic echo /scan --once` | `【需要替换】` |
| `/imu.frame_id` | 等于 imu_link | `ros2 topic echo /imu --once` | `【需要替换】` |
| `/odom.child_frame_id` | 等于 base_link | `ros2 topic echo /odom --once` | `【需要替换】` |

## 检查流程

```bash
ros2 run tf2_tools view_frames
ros2 run tf2_ros tf2_echo base_link laser_link
ros2 run tf2_ros tf2_echo base_link imu_link
ros2 topic echo /scan --once
ros2 topic echo /imu --once
ros2 topic echo /odom --once
```

如果某个 frame 断裂，先检查 URDF 中对应的 fixed joint、`robot_state_publisher` 和静态 TF 是否启动。
