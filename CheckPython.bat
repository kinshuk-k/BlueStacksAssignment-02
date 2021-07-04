@echo off
echo Checking Python...
python --version>temp.txt
set /p myvar=<temp.txt
echo %myvar%
del temp.txt
set version=%myvar:Python =%

If "%version%" == "Python =" ( 
echo Python is not installed..
goto installpython
goto exit
)

If "%version%" == "3.8.10" (
echo Python 3.8.10 is already installed, no further action needed.
goto exit
)

If not "%version%" == "3.8.10" (
echo Python %version% is installed.
goto installpython
goto exit
)

:installpython
echo Downloading Python.. Please wait.
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe', 'python-3.8.10.exe')"
echo Installing Python 3.8.10. Please wait as this might take few minutes.
echo Please click on "Yes" if prompted.
pause
python-3.8.10.exe /passive InstallAllUsers=1 PrependPath=1 Include_launcher=1
echo Python 3.8.10 32-bit successfully installed.

:exit
echo Python Check complete.
pause
exit /b