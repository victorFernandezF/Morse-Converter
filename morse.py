from ast import If
from errno import EAGAIN
from tkinter import *
from tkinter import ttk
import morse_dict

win= Tk()

#Set the window.
win.geometry("750x167")
win.title("Morse Code Translator")

# Check if is a sign and returns the key
def check_sign(c):
    if c == '.':
        return 'dot'
    if c == ',':
        return 'comma'
    if c == '?':
        return 'inter'
    if c == '/':
        return 'slash'
    return 0

# Function that convert text in morse
def traslate():
    global entry
    string= entry.get()
    res = ""
    space = '   '
    i = 0
    string = string.lower()
    if string == 'sos':
        info.configure(text="ARE YOU OKAY?")
    while(i < len(string)):
        aux = check_sign(string[i])
        alnum = string[i].isalnum()
        if alnum == 0 and aux == 0:
            res = "Non valid characters or more than one words inserted"
            break
            entry.delete(0, END)
        elif aux != 0:
            res += morse_dict.morse_letter[aux]
            res += space
        elif string[i] == 'c' and string[i +1] and string[i + 1] == 'h':
            res = res + morse_dict.morse_letter['mch']
            res = res + space
            i += 1
        else:
            res = res + morse_dict.morse_letter['m'+string[i]]
            res = res + space
        i = i + 1
    result.configure(state='normal')
    result.delete(0, END)
    result.insert(0, res)
    result.configure(state='readonly')
    if string != 'sos':
        info.configure(text="MORSE TRANSLATOR")

#Label with the name
info=Label(win, text="MORSE CODE TRANSLATOR", font=("Helvetica 18 bold"))
info.pack()

# Info label
enter=Label(win, text="Insert your word here", font=("arial 10"))
enter.pack()

# Entry where user enters a word
entry= Entry(win, width= 60, font=("arial 10"))
entry.focus_set()
entry.pack()

# Info label
lres=Label(win, text="Your result:", font=("arial 10"))
lres.pack()

# Entry for the result
result= Entry(win, width= 60, state='readonly', font=("arial 10") )
result.pack(pady=5)

#Create a Button witch calls the function.
ttk.Button(win, text= "TRANSLATE",width= 20, command= traslate).pack(pady=5)

win.mainloop()
