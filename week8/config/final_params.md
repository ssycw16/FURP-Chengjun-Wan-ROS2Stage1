# 最终参数汇总

## 底盘控制

文件：`week3/carter_bringup/config/carter_controllers.yaml`

| 参数 | 最终值 |
|---|---|
| wheel separation | 0.35 m |
| wheel radius | 0.05 m |
| max linear velocity | 0.5 m/s |
| max angular velocity | 1.0 rad/s |
| cmd_vel timeout | 0.5 s |

## EKF

文件：`week4/config/ekf.yaml`

- world frame：`odom`
- odom frame：`odom`
- base link frame：`base_link`
- two_d_mode：true

## SLAM / 地图

文件：`week5/config/slam_toolbox_mapping.yaml`

- resolution：0.05 m/pixel
- max range：12.0 m
- map frame：`map`
- odom frame：`odom`

## Nav2

文件：`week6/config/nav2_params.yaml`

- max_vel_x：0.5 m/s
- max_vel_theta：1.0 rad/s
- inflation radius：0.35 m
- cost scaling factor：3.0

## 室外

文件：`week7/config/robot_localization_global.yaml`

- world frame：`map`
- odom1：`/odometry/gps`

## 调参记录

每次修改参数后，请把改动、原因和实验结果追加到 `week8/config/tuning_log.md`。
