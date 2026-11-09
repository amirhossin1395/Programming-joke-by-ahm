import os
import time

base = "AHM_Prank_Folders"
if not os.path.exists(base):
    os.makedirs(base)

os.chdir(base)
print("ساخت پوشه‌های بی‌نهایت شروع شد... (Ctrl+C برای توقف)")

try:
    while True:
        os.makedirs("AHM", exist_ok=True)
        os.chdir("AHM")
except KeyboardInterrupt:
    print("\nمتوقف شد. پاک کردن پوشه‌ها ممکنه سخت باشه! 😂")