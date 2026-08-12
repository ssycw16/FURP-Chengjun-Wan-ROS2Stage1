# maps

`map.pgm` 是一张由 `generate_example_map.py` 生成的示例室内地图，便于在无真机数据时验证 Week 6 流程。

正式提交建议使用真实建图结果：

```bash
cd week5
bash scripts/save_map.sh maps/map
```

替换后请重新检查 `map.yaml` 的 `resolution` 和 `origin` 是否与 SLAM 输出一致。
