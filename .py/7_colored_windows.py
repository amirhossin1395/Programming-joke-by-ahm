import tkinter as tk
import random

root = tk.Tk()
root.withdraw()

def spawn():
    win = tk.Toplevel(root)
    win.geometry(f"150x150+{random.randint(0, 800)}+{random.randint(0, 600)}")
    color = random.choice(["red", "green", "blue", "yellow", "cyan", "magenta"])
    win.configure(bg=color)
    tk.Label(win, text="😂", font=("Arial", 30), bg=color).pack(expand=True)
    win.after(100, spawn)

spawn()
root.mainloop()