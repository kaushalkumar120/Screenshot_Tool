import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui, datetime

root = tk.Tk()
root.title("Screenshot Tool")
root.geometry("300x200")

save_path = ""

def set_folder():
    global save_path
    save_path = filedialog.askdirectory()

def save(img):
    if not img:
        messagebox.showerror("Error", "No Screenshot")
        return
    name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{save_path}/shot_{name}.png" if save_path else f"shot_{name}.png"
    img.save(path)
    messagebox.showinfo("Saved", path)

def full():
    root.withdraw()
    root.after(200, lambda: show(pyautogui.screenshot()))

def area():
    root.withdraw()
    x1, y1 = pyautogui.position()
    messagebox.showinfo("Select", "Move mouse & press OK")
    x2, y2 = pyautogui.position()
    show(pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1)))

def show(img):
    root.deiconify()
    save(img)

tk.Button(root, text="Full Screen", command=full).pack(pady=10)
tk.Button(root, text="Select Area", command=area).pack(pady=10)
tk.Button(root, text="Set Folder", command=set_folder).pack(pady=10)

root.mainloop()