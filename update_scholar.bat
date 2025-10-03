@echo off
REM ====== 切换到仓库目录 ======
cd /d D:\yuchenguommm.github.io

REM ====== 运行 Python 脚本，更新 scholar.png ======
python scripts\update_scholar.py

REM ====== 提交并推送到 GitHub ======
git add images\scholar.png
git commit -m "auto update scholar"
git push origin master
