from tkinter import *
from tkinter.messagebox import *
import math as m
from audio_helper import PlayAudio
import threading

#Object of Audio
ob = PlayAudio()

# Css Area useful Varible
font = ('verdana',15,'bold' )

# Important Fuction

def all_clear():
    enrtylabel.delete(0, END)

def clear():
    ex = enrtylabel.get()
    ex = ex[0:len(ex)-1]
    enrtylabel.delete(0, END)
    enrtylabel.insert(0, ex)

def click_btn_function(event):
    print("Btn Clicked")
    b = event.widget
    text = b['text']
    print(text)
    t = threading.Thread(target=ob.speak, args=(text,))
    t.start()

    if text == 'x':
        enrtylabel.insert(END, "*")
        return

    if text == '=':
        try:
            ex = enrtylabel.get()
            ans = eval(ex)
            enrtylabel.delete(0, END)
            enrtylabel.insert(0, ans)

        except Exception as e:
            print("Error..", e)
            showerror("Error",e)
        return

    enrtylabel.insert(END, text)

def clickenter(event):
    print("Hello Enter key")
    E_obj = Event()
    E_obj.widget = equalBtn
    click_btn_function(E_obj)



# Creating a window
window = Tk()
window.title(' My Calculator')
window.geometry('300x500')
window.iconbitmap()
window.title('Calculator')

#picture label
pic = PhotoImage(file='B:\DATA_SCIENCE\PYTHON\Python_Project\calculator\img\calculator.png')
headpiclabel = Label(window, image=pic)
headpiclabel.pack(side =TOP, pady=10)

# heading Label
headtitle = Label(window, text =' My Calculator', font = font, underline = 2)
headtitle.pack(side = TOP)

# Entry Label
enrtylabel = Entry(window, font=font, justify = CENTER )
enrtylabel.pack(side=TOP, pady=10, fill= X, padx=10)

# Buttons Frame
button_frame = Frame(window)
button_frame.pack(side=TOP, padx=10)
temp = 1
for i in range(0,3):
    for j in range(0,3):
        btn = Button(button_frame, text=str(temp),padx=3,pady=3,width=3, font=font, relief = 'ridge' )
        btn.grid(row = i, column = j)
        temp+=1
        btn.bind('<Button-1>', click_btn_function) #<Button-1> means on mouse right click
# BUtton Outside the frame       
zerobtn = Button(button_frame, text='0',font=font, relief = 'ridge',width=3, activebackground='black',activeforeground='white')
zerobtn.grid(row=3, column=0,) 

dotBtn = Button(button_frame, text='.', font=font, width=3, relief='ridge', activebackground='black',
                activeforeground='white')
dotBtn.grid(row=3, column=1)

equalBtn = Button(button_frame, text='=', font=font, width=3, relief='ridge', activebackground='black',
                  activeforeground='white')
equalBtn.grid(row=3, column=2)

plusBtn = Button(button_frame, text='+', font=font, width=3, relief='ridge', activebackground='orange',
                 activeforeground='white')
plusBtn.grid(row=0, column=3)

minusBtn = Button(button_frame, text='-', font=font, width=3, relief='ridge', activebackground='orange',
                  activeforeground='white')
minusBtn.grid(row=1, column=3)

multBtn = Button(button_frame, text='x', font=font, width=3, relief='ridge', activebackground='orange',
                 activeforeground='white')
multBtn.grid(row=2, column=3)

divideBtn = Button(button_frame, text='/', font=font, width=3, relief='ridge', activebackground='orange',
                   activeforeground='white')
divideBtn.grid(row=3, column=3)

clearBtn = Button(button_frame, text='<--', font=font, width=8, relief='ridge', activebackground='orange',
                  activeforeground='white', command = clear )
clearBtn.grid(row=4, column=0, columnspan=2)

allClearBtn = Button(button_frame, text='AC', font=font, width=8, relief='ridge', activebackground='orange',
                     activeforeground='white', command = all_clear)
allClearBtn.grid(row=4, column=2, columnspan=2)

# binding all btns
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
zerobtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)

# Let's bind textfield to serve enter key, Whenever anybody will click eter automatically press "=" fucntion


enrtylabel.bind('<Return>', clickenter)

###################-------Scitific Coding------------###########
#.........Sci-fic Buttons

scFrame = Frame(window)

sqrtBtn = Button(scFrame, text='√', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
sqrtBtn.grid(row=0, column=0)

powBtn = Button(scFrame, text='^', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
powBtn.grid(row=0, column=1)

factBtn = Button(scFrame, text='x!', font=font, width=5, relief='ridge', activebackground='orange',
                 activeforeground='white')
factBtn.grid(row=0, column=2)

radBtn = Button(scFrame, text='toRad', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
radBtn.grid(row=0, column=3)

degBtn = Button(scFrame, text='toDeg', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
degBtn.grid(row=1, column=0)

sinBtn = Button(scFrame, text='sinθ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
sinBtn.grid(row=1, column=1)

cosBtn = Button(scFrame, text='cosθ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
cosBtn.grid(row=1, column=2)

tanBtn = Button(scFrame, text='tanθ', font=font, width=5, relief='ridge', activebackground='orange',
                activeforeground='white')
tanBtn.grid(row=1, column=3)


#-------------Function 
normalcalc = True  # keeping True bcz, by default calculator is in normal mode

def calculate_sc(event):
    print('btn..')
    btn = event.widget
    text = btn['text']
    print(text)
    ex = enrtylabel.get()
    answer = ''
    if text == 'toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))


    elif text == 'toRad':
        print('radian')
        answer = str(m.radians(float(ex)))

    elif text == 'x!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text == 'sinθ':
        print("cal sin")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosθ':
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanθ':
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '√':
        print('sqrt')
        answer = m.sqrt(int(ex))
    elif text == '^':
        print('pow')
        base, pow = ex.split(',')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))

    enrtylabel.delete(0, END)
    enrtylabel.insert(0, answer)

def sc_click():
    global normalcalc
    print("Clicked")
    if normalcalc:
        # Need to show Scientific..
        button_frame.pack_forget()
        #now let's add sci-fic frame
        scFrame.pack(side=TOP, pady=10)
        button_frame.pack(side=TOP)
        window.geometry('400x600')
        print("Show sc")
        normalcalc = False  # if we are showing sci-fic, then close it

    else:
        print("Showing Normal")
        scFrame.pack_forget()
        window.geometry('400x600')
        normalcalc = True




# binding sc buttons
sqrtBtn.bind("<Button-1>", calculate_sc)
powBtn.bind("<Button-1>", calculate_sc)
factBtn.bind("<Button-1>", calculate_sc)
radBtn.bind("<Button-1>", calculate_sc)
degBtn.bind("<Button-1>", calculate_sc)
sinBtn.bind("<Button-1>", calculate_sc)
cosBtn.bind("<Button-1>", calculate_sc)
tanBtn.bind("<Button-1>", calculate_sc)

#-------END Fucntion

menubar = Menu(window)
mode = Menu(menubar, tearoff=0 ) #tearoff is to remove lining
#mode.add_command(label = "Scientific Calculator",command=sc_click)
mode.add_checkbutton(label = "Scientific Calculator",command=sc_click)
menubar.add_cascade(label="Mode", menu=mode)
window.config(menu=menubar)



window.mainloop()