import tkinter as tk
import random
import threading
import time

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='black')

label = tk.Label(root, text="SYSTEM ERROR", font=("Arial", 40), bg='black', fg='red')
label.pack(expand=True)

messages = ["SYSTEM ERROR", "HACKED!", "DELETING FILES...", "ACCESS DENIED", "CRITICAL FAILURE"]
colors = ["red", "green", "yellow", "cyan", "magenta"]

def change():
    while True:
        try:
            label.config(text=random.choice(messages), fg=random.choice(colors))
            time.sleep(0.1) # هر 0.1 ثانیه عوض میشه
        except:
            break

threading.Thread(target=change, daemon=True).start()
root.bind('<Escape>', lambda e: root.destroy())
root.mainloop()