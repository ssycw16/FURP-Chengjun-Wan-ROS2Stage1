# 上传到 GitHub

## 1. 在 GitHub 创建空仓库

在 GitHub 上新建仓库，例如 `carter-bootcamp-week3-8`，不要自动生成 README。

## 2. 初始化本地仓库

```bash
cd ~/Desktop/ROS2-Carter-Bootcamp-Submissions
git init
git add .
git commit -m "feat: Week3-8 Carter bootcamp submissions"
git branch -M main
```

## 3. 关联远程仓库并推送

```bash
git remote add origin https://github.com/<your-github-name>/carter-bootcamp-week3-8.git
git push -u origin main
```

## 4. 大文件处理

- GitHub 普通仓库建议单文件不超过 100 MB。
- 真机 rosbag、演示视频如果很大，推荐用 Git LFS、GitHub Release 或网盘链接。
- 本仓库不强制忽略 bag/视频，但上传前请确认仓库大小。

## 5. 提交前检查

- `README.md` 中替换小组名和仓库地址。
- 每个 `evidence/` 内删除占位说明，放入真实截图、日志、bag 或视频。
- 不要把 `build/`、`install/`、`log/`、`__pycache__/` 提交上去。
- 运行 `git status` 确认没有误提交大文件。
