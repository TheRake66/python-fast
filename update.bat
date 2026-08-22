@echo off
title Mise en ligne des templates...
set /p "message=Message : "
git add templates\*
git commit -m "Update templates: %message%"
git push origin main
pause
exit /b