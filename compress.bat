@echo off
title Compression des templates...
cd %~dp0\templates
python %~dp0\compress.py
pause
exit /b