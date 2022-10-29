from ast import If
from tkinter import *
from tkinter import ttk
import morse_dict

win= Tk()

#Set the size of the windows.
win.geometry("750x150")
win.title("Morse Translator")

# Function that convert text in morse
def traslate():
    global entry
    string= entry.get()
    res = ""
    j = 1
    i = 0
    if string == 'sos':
        info.configure(text="¿Estas bien?")
    
    while(i < len(string)):
        if string[i] == 'c' and string[i +1] and string[i + 1] == 'h':
            res = res + morse_dict.morse_letter['mch']
            res = res + '   '
            i += 1
        elif string[i] == '':
            res = "Solo una palabra, por favor."
        else:
            res = res + morse_dict.morse_letter['m'+string[i]]
            res = res + '   '
        i=i+1
    label.configure(text=res)

#Label info
info=Label(win, text="Introduce texto para convertirlo en morse", font=("Courier 18 bold"))
info.pack()

#Create an Input to get the word from the user.
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

# Empty label where the translation will be shown.
label=Label(win, text="", font=("Courier 12"))
label.pack()

#Create a Button witch calls the function.
ttk.Button(win, text= "TRADUCIR",width= 20, command= traslate).pack(pady=20)

win.mainloop()
