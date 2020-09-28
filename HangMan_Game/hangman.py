#-------------Python === Main Code for Hangman-----------\
def hangman():
    global ran_word, stars, len_word, n_stars, temps,total_word
    user_input = input1.get()
    entry1.delete(0, END)

    if(total_word > 0):
        if(user_input in ran_word):
            for i in range(len_word):
                if(ran_word[i]==user_input  and stars[i]=='*'):
                    stars.pop(i)
                    stars.insert(i, ran_word[i])
                    xx = ''.join(stars)
                    word_list = list(ran_word)
                    word_list.pop(i)
                    word_list.insert(i, "*")
                    word_label.configure(text=xx)

                    if(xx == temps):
                        ans_label.configure(text = 'Congratullations :  You won the Game..')
                        res_pop = messagebox.askyesno("Notification",' You win, Do you want to Play Again' )
                        if (res_pop == True):
                            chooseword()
                        else:
                            root.destroy()  
                    else:
                        break      
        else:
            total_word -= 1
            leftchange_label.configure(text = 'Left = {}'.format(total_word))           
    if(total_word <= 0):
        ans_label.configure(text = 'Opps :  You Lost your Game Chance..')
        res_pop = messagebox.askyesno("Notification",' You Lost, Do you want to Play Again' )
        if (res_pop == True):
            chooseword()
        else:
            root.destroy()
                    
                    
                    
def click(event):
    hangman()
        






from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.geometry('800x500+300+100') #height*width + X-axis + Y-axis
root.configure(bg='cyan') # to change background color
root.iconbitmap('hangman.ico') 
root.title(" Hangman Game ")
#------------ Labels ----------------------\

intro_label = Label(root, text = ' Welcome to HangMan Game', font=('arial', 30, 'underline bold'), bg ='cyan')
intro_label.place(x=100, y=0)

word_label = Label(root, text = ' ', font=('arial', 40, ' bold'), bg ='cyan')
word_label.place(x=300, y=200)

leftchange_label = Label(root, text = ' ', font=('arial', 25, ' bold'), bg ='cyan')
leftchange_label.place(x=650, y=150)

ans_label = Label(root, text = ' Congratullation : You Won... ', font=('arial', 20, ' bold'), bg ='cyan')
ans_label.place(x=150, y=450)

#------------ Entry Label-------------------\
input1 = StringVar() # To store the input from user
entry1 = Entry(root, textvariable=input1, relief=RIDGE, bd=5, bg='green', fg='white', justify='center', font=('arial', 25, ' bold'))
entry1.focus_set()
entry1.place(x=210, y=270)

#------------------- Button-----------\
btn1 = Button(root, text='Submit', font=('arial', 15, ' bold'), width = 10, bd=5, bg='white', activebackground='black', activeforeground='red', command = hangman)
btn1.place(x=320, y=340)
root.bind("<Return>", click)

#------------ Python Code === World Select Function--------\
wordlist = ['blue','brown', 'cyan', 'dark', 'gold','gray','green','rainbow','red','rose','white','yellow']

def chooseword():
    global ran_word, stars, len_word, n_stars, temps, total_word
    ran_word = random.choice(wordlist)
    temps = ran_word
    stars = ["*" for i in ran_word]
    len_word = len(ran_word)
    total_word = len_word
    leftchange_label.configure(text='left = {}'.format(total_word))
    n_stars = ''
    for i in stars:
        n_stars += i+' '
    word_label.configure(text = n_stars)
    ans_label.config(text='')
chooseword()
root.mainloop() # It will hold the window

