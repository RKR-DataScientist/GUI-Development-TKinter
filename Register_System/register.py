from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

# Let's create class for the registration
class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700")
        self.root.title(" Registration Link")
        self.root.config(bg="white")
        
        #----Background image -----#
        self.bg = ImageTk.PhotoImage(file='images/NewsletterSignupBackground.jpg')
        bg = Label(self.root, image=self.bg).place(x=250, y = 0, relwidth=1, relheight=1)

        #----Left image -----#
        self.bg = ImageTk.PhotoImage(file='images/let_image.jpg')
        bg = Label(self.root, image=self.bg).place(x=80, y = 100, width=400, height=500)
        
        # ------ Registration frame-----#
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text=" REGISTER HERE", font=("time new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=30)

        #---User Entry Field----#-----Row 1
        #self.var_fname = StringVar() , Put this in input field = textvariable=self.var_fname
        f_name = Label(frame1, text=" First Name", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.inp_fname = Entry(frame1, font=("time new roman", 15), bg="lightgray",)
        self.inp_fname.place(x=50, y=130, width=250)

        l_name = Label(frame1, text=" Last Name", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.inp_lname = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.inp_lname.place(x=370, y=130, width=250)


        #---Contact No & Email----#-------------Row 2
        contact = Label(frame1, text=" Contact Number", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.inp_contact = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.inp_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text=" Email ID", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.inp_email = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.inp_email.place(x=370, y=200, width=250)

        #---Security----#-------Row 4
        question = Label(frame1, text=" Security Question", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.comb_que = ttk.Combobox(frame1, font=("time new roman", 13), state="readonly", justify=CENTER)
        self.comb_que["values"] = ("select", "Your first pet name", " Your brith place", " Your best friend name")
        self.comb_que.place(x=50, y=270, width=250)
        self.comb_que.current(0)

        answer = Label(frame1, text=" Security An   swer", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.inp_answer = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.inp_answer.place(x=370, y=270, width=250)

        #---Password----#-------------Row 5
        password = Label(frame1, text=" Password", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)
        self.inp_pass = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.inp_pass.place(x=50, y=340, width=250)

        cpassword = Label(frame1, text=" Confirm Password", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)
        self.inp_cpass = Entry(frame1, font=("time new roman", 15), bg="lightgray")
        self.inp_cpass.place(x=370, y=340, width=250)

        #---Term & Condition----#-------------Row 6
        self.term = IntVar()
        term = Checkbutton(frame1, text=" I Agree the Terms & Conditions", font=("time new roman", 15, "bold"), bg="white", variable = self.term, onvalue=1, offvalue=0). place(x=50, y=380)

        #---Register Button----#-------------Row 7
        self.btn = ImageTk.PhotoImage(file="images/register_button.png")
        btn_register = Button(frame1, image=self.btn,bd=0, cursor="hand2",command=self.register_data ).place(x=50, y= 420)

        btn_sign = Button(self.root, text=" Sign In", font=("times new roman", 20, "bold"),bg="green", bd=0, cursor="hand2" ).place(x=190, y= 550, width=200)
    
    # Function to clear the all the filled data after successfully inserted
    def clear(self):
        self.inp_fname.delete(0,END), 
        self.inp_lname.delete(0,END),
        self.inp_contact.delete(0,END),
        self.inp_email.delete(0,END),
        self.comb_que.current(0),
        self.inp_answer.delete(0,END),
        self.inp_pass.delete(0,END),
        self.inp_cpass.delete(0,END),


    def register_data(self):
        if self.inp_fname.get()=="" or self.inp_lname.get()=="" or self.inp_contact.get()=="" or self.inp_email.get()=="" or self.comb_que.get()=="select" or self.inp_answer.get()=="" or self.inp_pass.get()=="" or self.inp_cpass.get()=="":
            messagebox.showerror(" Error", "All Fields are required", parent=self.root)
        elif self.inp_pass.get()!=self.inp_cpass.get():
            messagebox.showerror("Error", " Confirmed password doesn't matched",parent=self.root)
        elif self.term.get()==0:
            messagebox.showerror("Error", " Please Agree our terms and consition",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root", database="python_exercise")
                cur=con.cursor()
                cur.execute("select * from tk_register where email=%s", self.inp_email.get())
                exit_email = cur.fetchone()
                if exit_email!=None:
                    messagebox.showerror("Warning", " Email already exists, please try with other email id", parent=self.root)
                else:
                    cur.execute("insert into tk_register(fname,lname,contact,email,question,answer,password) values(%s, %s,%s, %s,%s, %s, %s)",
                                    (self.inp_fname.get(),
                                    self.inp_lname.get(),
                                    self.inp_contact.get(),
                                    self.inp_email.get(),
                                    self.comb_que.get(),
                                    self.inp_answer.get(),
                                    self.inp_pass.get(),
                                    )
                    )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Sucessful", parent=self.root)
                    self.clear()
            except Exception as er:
                messagebox.showerror("Error", f"Error due to:{str(er)}",parent=self.root)
            
        


        '''
        print(self.var_fname.get(), 
        self.inp_lname.get(),
        self.inp_contact.get(),
        self.inp_email.get(),
        self.comb_que.get(),
        self.inp_answer.get(),
        self.inp_pass.get(),
        self.inp_cpass.get()
        '''


root = Tk()
obj = Register(root)
root.mainloop()