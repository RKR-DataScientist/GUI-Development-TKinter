from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import messagebox as mb #import tkinter.messagebox as mb
import tkinter.ttk as ttk

# import model for database connectivity
import mysql.connector as con

# Now let's do connectivity
db_connection = con.connect(
    host = "localhost",
    user = "root",
    password= "root"
)
print("Data base connected successfull")

# Let create the GUI interface
class StudentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        self.geometry("800x700+315+50")

        # Let's create labels for title text and entry
        self.lblTitle = tk.Label(self, text="Student Managment System", font=("Helvetica", 16), bg="yellow", fg="green")
        self.lblFName = tk.Label(self, text="Enter FirstName:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblLName = tk.Label(self, text="Enter LastName:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblContactNo = tk.Label(self, text="Enter Contact No:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblCity = tk.Label(self, text="Enter City:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblState = tk.Label(self, text="Enter State:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblDOB = tk.Label(self, text="Choose Date of Birth:", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblSelect = tk.Label(self, text="Please select one record below to update or delete", font=("Helvetica", 10), bg="blue", fg="yellow")  
        self.lblSearch = tk.Label(self, text="Please Enter Roll No:",font=("Helvetica", 10), bg="blue", fg="yellow")

        # Let's Create Entry field For the Labels
        self.entFName = tk.Entry(self)  
        self.entLName = tk.Entry(self)  
        self.entContact = tk.Entry(self)  
        self.entCity = tk.Entry(self)  
        self.entState = tk.Entry(self) 
        self.calDOB = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2, year=1950,locale='en_US', date_pattern='y-mm-dd')  
        #self.entDOB = tk.Entry(self)  
        self.entSearch = tk.Entry(self)

        # Let's create the BUTTONS for actions
        self.btn_register = tk.Button(self, text="Register", font=("Helvetica", 11), bg="yellow", fg="blue",  
                            command=self.register_student)  
        self.btn_update = tk.Button(self,text="Update",font=("Helvetica",11),bg="yellow", fg="blue",
                            command=self.update_student_data)  
        self.btn_delete = tk.Button(self, text="Delete", font=("Helvetica", 11), bg="yellow", fg="blue",  
                            command=self.delete_student_data)  
        self.btn_clear = tk.Button(self, text="Clear", font=("Helvetica", 11), bg="yellow", fg="blue",  
                            command=self.clear_form)  
        self.btn_show_all = tk.Button(self, text="Show All", font=("Helvetica", 11), bg="yellow", fg="blue",  
                            command=self.load_student_data)  
        self.btn_search = tk.Button(self, text="Search", font=("Helvetica", 11), bg="yellow", fg="blue",  
                            command=self.show_search_record)  
        self.btn_exit = tk.Button(self, text="Exit", font=("Helvetica", 16), bg="yellow", fg="blue",
                            command=self.exit) 

        # Let's create the TABLE Columns Name for detail
        columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7")  
        self.tvStudent= ttk.Treeview(self,show="headings",height="5", columns=columns)  
        self.tvStudent.heading('#1', text='RollNo', anchor='center')  
        self.tvStudent.column('#1', width=60, anchor='center', stretch=False)  
        self.tvStudent.heading('#2', text='FirstName', anchor='center')  
        self.tvStudent.column('#2', width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#3', text='LastName', anchor='center')  
        self.tvStudent.column('#3',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#4', text='City', anchor='center')  
        self.tvStudent.column('#4',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#5', text='State', anchor='center')  
        self.tvStudent.column('#5',width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#6', text='PhoneNumber', anchor='center')  
        self.tvStudent.column('#6', width=10, anchor='center', stretch=True)  
        self.tvStudent.heading('#7', text='Date of Birth', anchor='center')  
        self.tvStudent.column('#7', width=10, anchor='center', stretch=True)


        #Scroll bars are set up below considering placement position(x&y) ,height and width of treeview widget
        vsb= ttk.Scrollbar(self, orient=tk.VERTICAL,command=self.tvStudent.yview)  
        vsb.place(x=40 + 640 + 1, y=310, height=180 + 20)  
        self.tvStudent.configure(yscroll=vsb.set)  
        hsb = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tvStudent.xview)  
        hsb.place(x=40 , y=310+200+1, width=620 + 20)  
        self.tvStudent.configure(xscroll=hsb.set)  
        self.tvStudent.bind("<<TreeviewSelect>>", self.show_selected_record)  
        self.lblTitle.place(x=280, y=30, height=27, width=300)  
        self.lblFName.place(x=175, y=70, height=23, width=100)  
        self.lblLName.place(x=175, y=100, height=23, width=100)  
        self.lblContactNo.place(x=171, y=129, height=23, width=104)  
        self.lblCity.place(x=210, y=158, height=23, width=65)  
        self.lblState.place(x=205, y=187, height=23, width=71)  
        self.lblDOB.place(x=148, y=217, height=23, width=128)  
        self.lblSelect.place(x=150, y=280, height=23, width=400)  
        self.lblSearch.place(x=174, y=560, height=23, width=134)  
        self.entFName.place(x=277, y=72, height=21, width=186)  
        self.entLName.place(x=277, y=100, height=21, width=186)  
        self.entContact.place(x=277, y=129, height=21, width=186)  
        self.entCity.place(x=277, y=158, height=21, width=186)  
        self.entState.place(x=278, y=188, height=21, width=186)  
        self.calDOB.place(x=278, y=218, height=21, width=186)  
        self.entSearch.place(x=310, y=560, height=21, width=186)  
        self.btn_register.place(x=290, y=245, height=25, width=76)  
        self.btn_update.place(x=370, y=245, height=25, width=76)  
        self.btn_delete.place(x=460, y=245, height=25, width=76)  
        self.btn_clear.place(x=548, y=245, height=25, width=76)  
        self.btn_show_all.place(x=630, y=245, height=25, width=76)  
        self.btn_search.place(x=498, y=558, height=26, width=60)  
        self.btn_exit.place(x=320, y=610, height=31, width=60)  
        self.tvStudent.place(x=40, y=310, height=200, width=640)

        self.create_table()  
        self.load_student_data()

if __name__ == "__main__":
    app = StudentApp()
    app.mainloop()
