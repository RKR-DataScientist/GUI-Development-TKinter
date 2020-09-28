# ToDo GUI Application using Tkinter

from tkinter import *
from tkinter import messagebox

# global list is declare for storing all the task 
tasks_list = [] 
  
# global variable is declare for couting the task 
counter = 1

# Firstly show the Error, if user has not given any input
def InputError():
    # check for enter task field is empty or no
    if enterTaskField.get() == "":
        # show the error message
        messagebox.showerror(" Input Error ")

        return 0
    return 1


# Funcion to clear the text at the number place in displayed box
def clear_taskNumberField():
    # clear the content  of task number text field
    taskNumberField.delete(0.0, END)

# if user has given input, then after submission,
# Entry box should be clear
def clear_entrytask():
    # clear the conent of the filed entru box
    enterTask.delete(0, END)

# Function for inserting the contents from task entry field
def inserttask():
    global counter
    
    # Check for error
    value = InputError()
    if value == 0:
        return

    # get the task string concatenating
    content = enterTaskField.get() + "\n"

    # store task in the list 
    tasks_list.append(content) 

    # insert content of task entry field to the text area 
    # add task one by one in below one by one 
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content) 
  
    # incremented 
    counter += 1
  
    # function calling for deleting the content of task field 
    clear_taskField() 

# function for deleting the specified task 
def delete(): 
    global counter 
      
    # handling the empty task error 
    if len(tasks_list)==0:
        messagebox.showerror("No task") 
        return
  
    # get the task number, which is required to delete 
    number = taskNumberField.get(1.0, END) 
  
    # checking for input error when 
    # empty input in task number field 
    if number == "\n" : 
        messagebox.showerror("input error") 
        return
      
    else : 
        task_no = int(number) 
  
    # function calling for deleting the 
    # content of task number field 
    clear_taskNumberField() 
      
    # deleted specified task from the list 
    tasks_list.pop(task_no - 1) 
  
    # decremented  
    counter -= 1
      
    # whole content of text area widget is deleted 
    TextArea.delete(1.0, END) 
  
    # rewriting the task after deleting one task at a time 
    for i in range(len(tasks_list)) : 
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])








if __name__ == "__main__":

    # Let's create window'
    gui = Tk()

    # Title of window
    gui.title("TO DO APP")

    # Set configuration of window
    gui.geometry("300x400")

    # Creating Label and Entry field for entry task
    enterTask = Label(gui, text="Enter your task", bg="light green")
    enterTaskField = Entry(gui)
    submitbtn = Button(gui, text="Submit", fg="Black", bg="Red", command=inserttask)

    # Creating label for Text area for task content
    TextArea = Text(gui, height=6, width=30, font="lucida 13")

    # create a label : Delete Task Number 
    taskNumber = Label(gui, text = "Delete Task Number", bg = "blue") 
                         
    taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13") 


    # create a Delete Button and place into the root window 
    # when user press the button, the command or  
    # function affiliated to that button is executed . 
    delete = Button(gui, text = "Delete", fg = "Black", bg = "Red", command = delete)

    #create a Exit Button and place into the root window 
    # when user press the button, the command or function affiliated to that button is executed . 
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit) 


    # Let's create geometery to place the labels
    enterTask.grid(row = 0, column = 2)
    enterTaskField.grid(row = 1, column = 2, ipadx = 50) 
    submitbtn.grid(row = 2, column = 2)
    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W) 
    taskNumber.grid(row = 4, column = 2, pady = 5) 
    taskNumberField.grid(row = 5, column = 2)
    delete.grid(row = 6, column = 2, pady = 5) 
    Exit.grid(row = 7, column = 2) 

    # start the GUI  
    gui.mainloop() 