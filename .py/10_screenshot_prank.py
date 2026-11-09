import pyautogui
import time
import os

time.sleep(2)
# گرفتن اسکرین‌شات و ذخیره در پوشه
screenshot = pyautogui.screenshot()
screenshot.save("screenshot_prank.png")
print("اسکرین‌شات گرفته شد و در پوشه ذخیره شد! (این یه شوخیه، هیچی فرستاده نشد)")