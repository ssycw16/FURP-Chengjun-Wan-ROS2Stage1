# 提交前检查清单

## 通用

- [ ] 在 `docs/environment.md` 中按实际环境确认依赖。
- [ ] 在各周报告标题填写小组名、成员和日期。
- [ ] 将所有 `【需要替换】` 替换为真实内容。
- [ ] 按 [docs/github-upload.md](docs/github-upload.md) 上传 GitHub。
- [ ] 确认没有提交 `build/`、`install/`、`log/`、`__pycache__/`。

## Week 3

- [x] `carter_bringup` package、launch、controllers、脚本。
- [ ] 放入直线运动截图、旋转截图、方形轨迹截图。
- [ ] 放入 `/odom`、`/joint_states`、TF tree 输出。
- [ ] 可选：放入运动 rosbag。
- [ ] 在 `week3/report/week3_report.md` 填写实测结果和排查过程。

## Week 4

- [x] `ekf.yaml`、`ekf.launch.py`、rosbag 记录脚本、odom 对比脚本。
- [ ] 放入 Carter 运动 rosbag。
- [ ] 放入 RViz LiDAR 截图和 raw/filtered odometry 对比图。
- [ ] 完成 [sensor_tf_checklist.md](week4/config/sensor_tf_checklist.md)。

## Week 5

- [x] mapping launch、SLAM 参数、示例地图、质量报告模板。
- [ ] 放入真实建图 rosbag。
- [ ] 用 `map_saver_cli` 替换 `maps/map.pgm` 和 `maps/map.yaml`。
- [ ] 放入 RViz 地图截图和建图轨迹截图。
- [ ] 填写地图质量报告和失败案例分析。

## Week 6

- [x] Nav2 参数、navigation launch、单点/多点 goal 脚本、动态障碍测试脚本。
- [ ] 放入 initial pose、单点、多点、动态障碍截图。
- [ ] 放入 Nav2 日志和动态障碍 CSV。
- [ ] 可选：放入导航 rosbag。
- [ ] 填写失败案例和 root-cause 分析。

## Week 7

- [x] waypoint 文件、GPS/RTK 配置、死推算降级脚本、安全 checklist。
- [ ] 放入室外 bag 或演示视频。
- [ ] 放入 GPS 离线分析 CSV 和测试日志。
- [ ] 按 `safety/outdoor_safety_checklist.md` 完成勾选。
- [ ] 填写失败案例分析。

## Week 8

- [x] full bringup、final report 模板、复现说明、证据收集脚本。
- [ ] 填写 [final_report.md](week8/docs/final_report.md)。
- [ ] 填写 [reproduction.md](week8/docs/reproduction.md)。
- [ ] 放入最终截图、日志、rosbag 和演示视频。
- [ ] 完成一次系统 check：`bash week8/scripts/check_system.sh`。
