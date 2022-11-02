from ast import If
from errno import EAGAIN
from tkinter import *
from tkinter import ttk
import morse_dict

win= Tk()

#Set the window.
win.geometry("750x502")
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
        if i != ' ' and i != '\n':
            word += i
        elif word not in morse_dict.morse_to_letter:
            res = "Invalid characters inserted."
        else:
           res = res + morse_dict.morse_to_letter[word]
           word = ""
    print(res)
    result.configure(state='normal')
    result.config(background="white")
    result.delete(1.0, END)
    result.insert(INSERT, res)
    result.configure(state='disabled')


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
            res += '/ '
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
    res += space
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
    opcion.set(None)
    btn_reset.pack_forget()
    btn_text.pack_forget()

#Label with the name
info=Label(win, text="MORSE CODE TRANSLATOR", font=("Helvetica 18 bold"))
info.pack()

# Label and radio to selec options
enter=Label(win, text="Choose an option:", font=("arial 14"))
enter.pack(pady =1)

# Function to manage the radiobutton
opcion = IntVar()
def selec():
    if opcion.get() == 1:
        btn_text.config(command=translate)
        btn_text.pack(pady=5)
        btn_reset.pack(pady=5)
        enter.config(text="Insert your text here:")
    else:
        btn_text.config(command=morse_to_text)
        btn_text.pack(pady=5)
        btn_reset.pack(pady=5)
        enter.config(text="Insert your morse code here:")

Radiobutton(win, text="Translate text to morse code", variable=opcion, value=1, command=selec).pack()
Radiobutton(win, text="Translate morse code to text", variable=opcion, value=2, command=selec).pack()

# Info label
enter=Label(win, text="Insert your text here:", font=("arial 12"))
enter.pack()

# Entry where user enters a word
entry = Text(win, width="60", height="6", state='normal', font=("arial 9"))
entry.focus_set()
entry.pack()

# Info label
lres=Label(win, text="Your result:", font=("arial 12"))
lres.pack(pady=2)
dash_info=Label(win, text="( / is the words separator)", font=("arial 10"))
dash_info.pack(pady=2)

# Textarea for the result
result = Text(win, width="47", height="7", state='disabled', font=("arial 12"))
result.config(background="gainsboro")
result.pack()

#Create a Button witch calls the function.
btn_text = ttk.Button(win, text= "TRANSLATE",width=70, command= translate)
btn_text.pack_forget()

# Button witch restart.
btn_reset = ttk.Button(win, text= "RESET",width= 70, command= restart)
btn_reset.pack_forget()

win.mainloop()
