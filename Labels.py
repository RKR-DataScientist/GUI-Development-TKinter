from tkinter import *

# Root Window
root = Tk()

# Window size, It will fix the window at same place
root.geometry("450x300")

# Lebals
user = Label(root, text=" Username")
user.place(x=40, y=60) # X from vertical, Y from horizontal
  
user_name_input_area = Entry(root, width = 30)
user_name_input_area.place(x = 110, y = 60) 


#the label for user_password   
user_password = Label(root,  text = "Password")
user_password.place(x = 40, y = 100) 
    
user_password_entry_area = Entry(root, width = 30)
user_password_entry_area.place(x = 110, y = 100) 

submit_button = Button(root,  text = "Submit")
submit_button.place(x = 150, y = 150) 

root.mainloop()