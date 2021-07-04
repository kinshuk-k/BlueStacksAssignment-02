echo off
set /p UserInputPath=Enter current path:
cd %UserInputPath%
call CheckPython.bat
start py BlueStacksInstaller.py
