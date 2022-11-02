from ast import If
from errno import EAGAIN
from tkinter import *
from tkinter import ttk
import morse_dict

win= Tk()

#Set the window.
win.geometry("750x410")
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
    if c == '"':
        return 'quot'
    if c == ' ':
        return 'sp'
    return 0
def morse_to_text():
    global entry
    string= entry.get("1.0",END)
    word = ""
    res = ""
    i = 0
    for i in string:
        if i != ' ':
            word += i
        else:
            res = res + morse_dict.morse_to_letter[word]
            word = ""
    print(res)


# Function that convert text in morse
def translate():
    global entry
    string= entry.get("1.0",END)
    res = ""
    space = ' '
    i = 0
    string = string.lower()
    if string == "sos":
        info.configure(text="ARE YOU OKAY?")
    while(i < len(string) - 1):
        aux = check_sign(string[i])
        alnum = string[i].isalnum()
        if alnum == 0 and aux == 0:
            res = "Non valid characters inserted"
            break
        elif (aux == 'sp'):
            res += ' / '
            dash_info.configure(text="( / is the separator between words)")
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
    result.config(background="white")
    result.delete(1.0, END)
    result.insert(INSERT, res)
    result.configure(state='disabled')
    if string != 'sos':
        info.configure(text="MORSE CODE TRANSLATOR")

def restart():
    entry.delete(1.0, END)
    result.configure(state='normal')
    result.delete(1.0, END)
    result.configure(state='disabled')
    info.configure(text="MORSE CODE TRANSLATOR")
    result.config(background="gainsboro")
#Label with the name
info=Label(win, text="MORSE CODE TRANSLATOR", font=("Helvetica 18 bold"))
info.pack()

# Info label
enter=Label(win, text="Insert your text here:", font=("arial 12"))
enter.pack()

# Entry where user enters a word
entry = Text(win, width="60", height="6", state='normal', font=("arial 9"))
entry.focus_set()
entry.pack()

# Info label
lres=Label(win, text="Your result:", font=("arial 12"))
lres.pack()
dash_info=Label(win, text="", font=("arial 10"))
dash_info.pack()

# Textarea for the result
result = Text(win, width="47", height="7", state='disabled', font=("arial 12"))
result.config(background="gainsboro")
result.pack()

#Create a Button witch calls the function.
ttk.Button(win, text= "TRANSLATE",width=70, command= translate).pack(pady=5)

# Button witch restart.
ttk.Button(win, text= "RESET",width= 70, command= restart).pack(pady=5)
win.mainloop()
