import webbrowser
import time

print("در حال باز کردن 100 تب...")
for i in range(100):
    webbrowser.open("https://www.google.com")
    time.sleep(0.5)
print("تمام شد! 😂")