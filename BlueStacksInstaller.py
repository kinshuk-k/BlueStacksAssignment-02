import sys
import subprocess

#Installing pyautogui, pywinauto packages
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pywinauto'])

import pyautogui
import time
from pywinauto.application import Application

#Downloading BlueStacks 5 Installer
subprocess.run(["powershell", "-Command", "(New-Object Net.WebClient).DownloadFile('https://cdn3.bluestacks.com/downloads/windows/nxt/5.1.0.1129/e854d27339a15f21d2c1d06addfc8abd/BlueStacksMicroInstaller_5.1.0.1129_native.exe?filename=BlueStacksInstaller_5.1.0.1129_native_e9cb8692aaba4ddf18cbbb9256ea25ce_0.exe', 'BlueStacksInstaller_5.exe')"])
#Installing BlueStacks 5
BSInstall = Application(backend="uia").start(cmd_line="BlueStacksInstaller_5.exe")
time.sleep(5)
ActiveWindow = pyautogui.getActiveWindow()
pyautogui.click(ActiveWindow.left + 300, ActiveWindow.top + 400)

#If Installer fails
time.sleep(15)
pyautogui.click(ActiveWindow.left + 376, ActiveWindow.top + 278)
