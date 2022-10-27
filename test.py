#Import the required Libraries
from ast import If
from tkinter import *
from tkinter import ttk


morse = dict(
    a = '. -',
    b = '— · · ·',
    c = '',
    d = '',
    e = '',
    f = '',
    g = '',
    h = '',
    i = '',
    j = '',
    k = '',
    l = '',
    m = '',
    n = '',
    o = '- - -',
    p = '',
    q = '',
    r = '',
    s = '. . .',
    t = '',
    u = '',
    v = '',
    w = '',
    x = '',
    y = '',
    z = ''
    )
#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")

def display_text():
    global entry
    string= entry.get()
    res = ""
    for i in string:
        if i == " ":
            res = res + "  "
        res = res + morse[i]
        res = res + "  "
    label.configure(text=res)


#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.config(font=('Helvatical bold',20))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()