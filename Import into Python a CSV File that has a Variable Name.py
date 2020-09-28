# Import into Python a CSV File that has a Variable Name
# https://datatofish.com/import-into-python-a-csv-file-that-has-a-variable-name/

import pandas as pd
from pandas import DataFrame
import tkinter as tk 
 
root= tk.Tk()
  
canvas1 = tk.Canvas(root, width = 300, height = 300) # create the canvas
canvas1.pack()
  
entry1 = tk.Entry (root) # create the entry box
canvas1.create_window(150, 100, window=entry1)
  
def insert_number(): # add a function/command to be called by the button (i.e., button1 below)
    global x1 # add 'global' before the variable x1, so that you can use that variable outside of the command/function if ever needed 
    x1 = str(entry1.get()) # store the data input by the user as a variable x1 
 
    PATH = r'C:\Users\Ron\Desktop\Import into Python\Sales_' + x1 + '.csv' #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.csv'
    read_sales = pd.read_csv (PATH)   #read the csv file using the 'PATH' varibale 
    df = DataFrame(read_sales,columns=['Client Name','Country','Product','Purchase Price','Date'])  # assign column names
    print (df)
 
button1 = tk.Button (root, text='Input date to import file (ddmmyyyy) ',command=insert_number, bg='green', fg='white') # button to call the 'insert_number' command above 
canvas1.create_window(150, 140, window=button1)
  
root.mainloop()