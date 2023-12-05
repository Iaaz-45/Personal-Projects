import requests
import random
import tkinter as tk
from tkinter import ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

WORDS = []
NOUNS = []
perspective = ["I", "You", "She", "He", "We", "They", "Dogs", "Cats", "Bears", "Godzillas", "Monkeys", "Cars", "Johnny"]
connectors = ["With", "Of", "For", "Out", "Off", "Out of", "a"]

def get_random_verb():
    ran = random.randrange(0, 2)
    no_s = False
    if ran == 0:
        no_s = True
    with open("Projects/Sentence Generator/verbs.txt" , "r") as file:
        WORDS = file.readlines()
    for i in range(len(WORDS)):
        WORDS[i] = WORDS[i].replace("\t", "").replace("\n", "")
        if no_s:
            WORDS[i] = WORDS[i][:len(WORDS[i]) - 1]
    return WORDS[random.randrange(0, len(WORDS))]

def get_random_noun():
    with open("Projects/Sentence Generator/nouns.txt" , "r") as file:
        NOUNS = file.readlines()
    for i in range(len(NOUNS)):
        NOUNS[i] = NOUNS[i].replace("\n", "").capitalize()
    return NOUNS[random.randrange(0, len(NOUNS))]

def sentence(u_input):
    verb = get_random_verb()
    noun = get_random_noun()
    per = perspective[random.randrange(0, len(perspective))]
    con = connectors[random.randrange(0, len(connectors))]
    sentence = [f"{per} {verb} {u_input} {con} {noun}",
                f"{per} {verb} {con} {u_input} {con} {noun}",
                f"{per} {verb} {con} {u_input} {noun}",
                f"{per} {verb} {con} {u_input}",
                f"{per} {verb} {u_input} {noun}",
                f"{per} {verb} {u_input} {noun}",]
    return tk.Label(root, text=sentence[random.randrange(0, len(sentence))]).pack()

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

message = tk.Label(root, text="Enter Word:").pack()

entry = ttk.Entry(root)
entry.pack()

def call():
    u_input = entry.get()
    sentence(u_input)

btn = tk.Button(root, text="Generate", command=call).pack()

root.mainloop()