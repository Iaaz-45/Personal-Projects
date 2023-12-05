import tkinter as tk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

def generate(message):
    return tk.Label(root, text=f"HI {message}").pack()

root = tk.Tk()
root.title("Cum")

window_width = 600
window_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.minsize(window_width, window_height)

message = tk.Label(root, text="Hello, World!")
message.pack()

btn = tk.Button(root, text="Generate", command=lambda: generate("hello")).pack()

root.mainloop()