from tkinter import *
from tkinter import messagebox
import random

secret = random.randint(1, 8)

window = Tk()
window.wm_title("Guess the Number")
window.geometry("1010x150")

# TODO: Create button functions to handle buttons 1-8


def clickOne():
    blank.configure(state = 'normal')
    blank.delete(0, 'end')
    if secret == 1:
        Ans = "Found It!"
    else:
        Ans = "Missed!"
    blank.insert(0, Ans)
    blank.configure(state = 'readonly')

def clickTwo():
    blank.configure(state = 'normal')
    blank.delete(0, 'end')
    if secret == 2:
        Ans = "Found It!"
    else:
        Ans = "Missed!"
    blank.insert(0, Ans)
    blank.configure(state = 'readonly')

def clickThree():
    blank.configure(state = 'normal')
    blank.delete(0, 'end')
    if secret == 3:
        Ans = "Found It!"
    else:
        Ans = "Missed!"
    blank.insert(0, Ans)
    blank.configure(state = 'readonly')

def clickFour():
    blank.configure(state = 'normal')
    blank.delete(0, 'end')
    if secret == 4:
        Ans = "Found It!"
    else:
        Ans = "Missed!"
    blank.insert(0, Ans)
    blank.configure(state = 'readonly')

def clickFive():
    blank.configure(state = 'normal')
    blank.delete(0, 'end')
    if secret == 5:
        Ans = "Found It!"
    else:
        Ans = "Missed!"
    blank.insert(0, Ans)
    blank.configure(state = 'readonly')

def clickSix():
    blank.configure(state = 'normal')
    blank.delete(0, 'end')
    if secret == 6:
        Ans = "Found It!"
    else:
        Ans = "Missed!"
    blank.insert(0, Ans)
    blank.configure(state = 'readonly') 

def clickSeven():
    blank.configure(state = 'normal')
    blank.delete(0, 'end')
    if secret == 7:
        Ans = "Found It!"
    else:
        Ans = "Missed!"
    blank.insert(0, Ans)
    blank.configure(state = 'readonly')

def clickEight():
    blank.configure(state = 'normal')
    blank.delete(0, 'end')
    if secret == 8:
        Ans = "Found It!"
    else:
        Ans = "Missed!"
    blank.insert(0, Ans)
    blank.configure(state = 'readonly')

def exit():
    if messagebox.askokcancel('Quit', 'You are about to quit, is that OK?'):
        window.destroy()

        

# TODO: display buttons 1-8 that use the button functions


b1 = Button(window, text='1', width=12, command=clickOne)
b1.place(x=100, y=25)
b1 = Button(window, text='2', width=12, command=clickTwo)
b1.place(x=200, y=25)
b1 = Button(window, text='3', width=12, command=clickThree)
b1.place(x=300, y=25)
b1 = Button(window, text='4', width=12, command=clickFour)
b1.place(x=400, y=25)
b1 = Button(window, text='5', width=12, command=clickFive)
b1.place(x=500, y=25)
b1 = Button(window, text='6', width=12, command=clickSix)
b1.place(x=600, y=25)
b1 = Button(window, text='7', width=12, command=clickSeven)
b1.place(x=700, y=25)
b1 = Button(window, text='8', width=12, command=clickEight)
b1.place(x=800, y=25)

# TODO: Create the status text field
blank = Entry(window)
blank.place(x=400, y=55)
blank.configure(state = 'readonly')
# TODO: Create the Exit button that uses window.destroy
b1 = Button(window, text='Exit', width=12, command=exit)
b1.place(x=400, y=75)

window.mainloop()
