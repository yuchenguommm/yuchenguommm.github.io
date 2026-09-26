@echo off
REM ====== Refresh the visitor map data from GoatCounter ======
REM Run daily by the scheduled task "visitors_update". Output is appended to
REM scripts\visitors_update.log so a failed run can be diagnosed afterwards.
cd /d D:\yuchenguommm.github.io

set LOG=scripts\visitors_update.log
call :run >> "%LOG%" 2>&1
set RC=%ERRORLEVEL%
if not "%RC%"=="0" echo [%DATE:~-10% %TIME%] FAILED with exit code %RC% >> "%LOG%"
exit /b %RC%

:run
echo.
echo ===== %DATE:~-10% %TIME% =====

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
if errorlevel 1 (
  echo Stats fetch failed.
  exit /b 1
)

git add _data\visitor_stats.yml
git diff --cached --quiet
if not errorlevel 1 (
  echo No changes to commit.
  exit /b 0
)
git commit -m "auto update visitor stats"
if errorlevel 1 (
  echo Commit failed.
  exit /b 1
)
git push origin master
if errorlevel 1 (
  echo Push failed - will retry on the next scheduled run.
  exit /b 1
)
echo Done.
exit /b 0
