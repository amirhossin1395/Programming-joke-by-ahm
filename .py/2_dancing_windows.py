import tkinter as tk
import random
import math

root = tk.Tk()
root.withdraw()
windows = []
t = 0

def spawn():
    win = tk.Toplevel(root)
    win.geometry("100x100")
    win.configure(bg='black')
    tk.Label(win, text="🕺", font=("Arial", 30), bg='black').pack(expand=True)
    windows.append(win)
    win.after(300, spawn)

def dance():
    global t
    t += 1
    for win in windows:
        try:
            x = 400 + 300 * math.sin(t * 0.1)
            y = 300 + 200 * math.cos(t * 0.15)
            win.geometry(f"+{int(x)}+{int(y)}")
        except:
            pass
    root.after(50, dance)

spawn()
dance()
root.mainloop()