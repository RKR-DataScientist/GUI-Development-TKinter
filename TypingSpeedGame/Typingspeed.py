from tkinter import *
import random
from tkinter import messagebox

def WordSlider():
    global count, sliderwords
    text = 'Welcome to Typing Speed Increaser Game'
    if(count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(150, WordSlider)

def time():
    global timeleft,score, miss
    if (timeleft >= 11):
        pass
    else:
        timecount.configure(fg='red')

    if (timeleft > 0):
        timeleft -= 1
        timecount.configure(text = timeleft)
        timecount.after(1000, time)
    else:
        playdetail.configure(text="Hit = {} | Miss = {} | Total Score = {}".format(score, miss, score-miss))
        msg = messagebox.askretrycancel('Notification', 'Play Again : Hit Enter')
        if (msg==True):
            score = 0
            miss = 0
            timeleft = 10
            scorecount.configure(text=score)
            timecount.configure(text=timeleft)
            wordlabel.configure(text=words[0])
            playdetail.configure(text="")


    
def StartGame(event):
    global score, miss
    if (timeleft == 10):
        time()
    playdetail.configure(text="")
    input = wordentry.get()
    if (input == wordlabel['text']):
        score += 1
        scorecount.configure(text=score)
    else:
        print('Not Matched')
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0,END)


#------------------ Root Window Configuration ---------#
root = Tk()
root.geometry("800x600+400+100")
root.configure(bg="powder blue")
root.title(" Typing Speed Game")
root.iconbitmap('Cool.ico')

#----------Variable----------#
score = 0
miss = 0
timeleft = 10
count = 0
sliderwords = ''
words = ['ability','able','about','above','accept','according','account','across','act','action','activity','actually','add','address']


#-------------Labels fields------------#
fontlabel = Label(root, text='', font=('airal',25,'italic bold'),bg='powder blue', fg='red', width=40)
fontlabel.place(x=10, y=10)
WordSlider()

random.shuffle(words)
wordlabel = Label(root, text=words[0], font=('airal',40,'italic bold'),bg='powder blue', fg='red', justify=CENTER)
wordlabel.place(x=330, y=200)

scoreboard = Label(root, text='Your Score', font=('airal',25,'italic bold'),bg='powder blue', fg='blue')
scoreboard.place(x=10, y=100)

scorecount = Label(root, text=score, font=('airal',25,'italic bold'),bg='powder blue', fg='white')
scorecount.place(x=50, y=150)

timeboard = Label(root, text='Time Left', font=('airal',25,'italic bold'),bg='powder blue', fg='blue')
timeboard.place(x=600, y=100)


timecount = Label(root, text=timeleft, font=('airal',25,'italic bold'),bg='powder blue', fg='white')
timecount.place(x=670, y=150)

playdetail = Label(root, text='Type Word ans Hit Enter Button', font=('airal',25,'italic bold'),bg='powder blue', fg='gray')
playdetail.place(x=150, y=500)


#-------- Entry Field--------------#
wordentry = Entry(root, font=('airal',27,'italic bold'), bd=10, justify=CENTER )
wordentry.place(x= 200, y= 330)
wordentry.focus_set()

#------------ Binding Enter Button -----------#
root.bind('<Return>', StartGame)



root.mainloop()