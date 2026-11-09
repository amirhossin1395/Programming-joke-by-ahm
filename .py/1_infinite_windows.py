import tkinter as tk
import random

def spawn():
    win = tk.Toplevel(root)
    win.geometry(f"200x100+{random.randint(0, 800)}+{random.randint(0, 600)}")
    win.configure(bg='black')
    tk.Label(win, text="HACKED! 😂", font=("Arial", 16), bg='black', fg='red').pack(expand=True)
    # هر 0.5 ثانیه یه پنجره جدید
    win.after(500, spawn)

root = tk.Tk()
root.withdraw()
spawn()
root.mainloop()