import time
from tkinter import *
import sys

root = Tk()
root.title("Digital Clock")

def get_time():
    time_string = time.strftime("%I:%M:%S %p")
    clock.config(text=time_string)
    clock.after(200, get_time)

clock = Label(root, font=("time", 90, "bold"))
clock.pack()
get_time()
root.mainloop()