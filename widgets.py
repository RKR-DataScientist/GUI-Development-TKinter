from tkinter import *

# creating root window
root = Tk()

#Frame inside root window
frame = Frame(root)

# Geometry method
frame.pack()

# button inside frame
button = Button(frame, text=" Click Here")
button.pack()

# Tkinten event loop
root.mainloop()