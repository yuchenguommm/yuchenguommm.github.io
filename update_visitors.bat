@echo off
REM ====== Refresh the visitor map data from GoatCounter ======
cd /d D:\yuchenguommm.github.io

REM Credentials live in scripts\goatcounter.env, which is git-ignored.
REM One KEY=VALUE per line, no quotes, no "set" prefix:
REM   GOATCOUNTER_CODE=yourcode
REM   GOATCOUNTER_TOKEN=yourapitoken
if not exist scripts\goatcounter.env (
  echo Missing scripts\goatcounter.env - see the comments in this file.
  exit /b 1
)
for /f "usebackq eol=# tokens=1,* delims==" %%a in ("scripts\goatcounter.env") do set "%%a=%%b"

python scripts\update_visitor_stats.py
if errorlevel 1 exit /b 1

git add _data\visitor_stats.yml
git diff --cached --quiet
if not errorlevel 1 (
  echo No changes to commit.
  exit /b 0
)
git commit -m "auto update visitor stats"
git push origin master
