# rosbag

可选。记录导航过程：

```bash
ros2 bag record /cmd_vel /odom /scan /tf /tf_static \
  /global_costmap/costmap_raw /local_costmap/costmap_raw \
  -o evidence/rosbag/nav_test_bag
```
