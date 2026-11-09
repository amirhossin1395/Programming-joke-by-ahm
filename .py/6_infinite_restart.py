import sys
import time

print("برنامه در حال اجراست...")
time.sleep(1)
print("خطا! ریستارت در 3 ثانیه...")
time.sleep(3)
# با اجرای دوباره برنامه، حلقه بی‌نهایت ایجاد میشه
import os
os.system(f'python "{sys.argv[0]}"')