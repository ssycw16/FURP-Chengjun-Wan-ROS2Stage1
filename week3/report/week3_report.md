# Week 3 实验报告

## 小组

- 小组名：`【需要替换】`
- 成员：`【需要替换】`
- 日期：`【需要替换】`
- 硬件模式：fake hardware / 真机 / 仿真

## 1. 实验目标

验证 Carter 差速底盘能够接收 `/cmd_vel`，正确发布 `/odom` 和 `odom -> base_link` TF，并完成直线、原地旋转、方形轨迹和安全停止。

## 2. 底盘参数

| 参数 | 数值 |
|---|---|
| wheel radius | 0.05 m |
| wheel separation | 0.35 m |
| max linear velocity | 0.5 m/s |
| max angular velocity | 1.0 rad/s |
| cmd_vel timeout | 0.5 s |

## 3. 演示结果

### 3.1 直线运动

- 指令：`linear.x = 0.2 m/s`
- 实际结果：`【需要替换：位移、是否跑偏、odom 终点】`
- 截图：`evidence/screenshots/straight.png`

### 3.2 原地旋转

- 指令：`angular.z = 0.5 rad/s`
- 实际结果：`【需要替换：旋转角度、偏差、方向】`
- 截图：`evidence/screenshots/rotate.png`

### 3.3 小方形轨迹

- 边长：0.6 m
- 实际结果：`【需要替换：终点误差、各边轨迹】`
- 截图：`evidence/screenshots/square.png`

### 3.4 /odom 与 /tf

- `/odom` 频率：`【需要替换】`
- `odom -> base_link` 是否有效：是 / 否
- TF tree 截图：`evidence/screenshots/tf_tree.png`

### 3.5 安全停止

- watchdog 超时：0.5 s
- 停止后 `/cmd_vel`：`[0, 0, 0]`
- 急停测试结果：`【需要替换】`

## 4. 问题与排查

`【需要替换：至少记录一个实际遇到问题、原因、解决方式】`

示例：

- 现象：`/odom` 位移方向与前进方向相反。
- 排查：检查左右轮轴方向和编码器符号。
- 修复：调整右轮 `velocity` 符号或交换左右轮接口。
