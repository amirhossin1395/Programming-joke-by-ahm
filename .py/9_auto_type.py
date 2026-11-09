import pyautogui
import time

time.sleep(3) # 3 ثانیه فرصت برای رفتن به Notepad
text = "HACKED BY AHM! 😂 " * 50
for char in text:
    pyautogui.typewrite(char)
    time.sleep(0.05)