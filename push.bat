@echo off
title Mise en ligne global...
set /p "message=Message : "
git add .
git commit -m "%message%"
git push origin main
pause
exit /b