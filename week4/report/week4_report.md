# Week 4 实验报告

## 小组

- 小组名：`【需要替换】`
- 日期：`【需要替换】`

## 1. 实验目标

验证 LiDAR、IMU 和里程计数据有效，并配置 robot_localization EKF 输出 `/odometry/filtered`。

## 2. 数据记录

- bag 路径：`【需要替换】`
- bag 时长：`【需要替换】`
- bag topics：`【需要替换】`
- `/scan` 频率：`【需要替换】`

## 3. raw odometry 与 filtered odometry 对比

| 指标 | 数值 |
|---|---|
| max position diff | `【需要替换】m` |
| raw 轨迹特征 | `【需要替换：是否跳变、漂移】` |
| filtered 轨迹特征 | `【需要替换：是否平滑、是否偏移】` |
| 对比图 | `evidence/screenshots/raw_vs_filtered.png` |

结论：`【需要替换】`

## 4. 传感器 TF 检查表

结果填写在 [config/sensor_tf_checklist.md](../config/sensor_tf_checklist.md)。

## 5. RViz LiDAR 截图

- 截图：`evidence/screenshots/lidar_rviz.png`
- LiDAR frame：`【需要替换】`
- 点云/scan 是否与墙体对齐：`【需要替换】`

## 6. 问题与排查

`【需要替换：至少记录一个失败案例和 root-cause】`

示例：

- 现象：EKF 无输出。
- 排查：`ros2 node info /ekf_filter_node`，发现 `imu0` topic 不匹配。
- 修复：将 `imu0` 改为实际 `/imu/data_raw`，并确认 `frame_id`。
