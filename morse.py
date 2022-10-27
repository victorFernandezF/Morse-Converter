#Import the required Libraries
from ast import If
from tkinter import *
from tkinter import ttk


morse = dict(
    a = '. -',
    b = '— · · ·',
    c = '— · — ·',
    ch = '— — — —',
    d = '— · ·',
    e = '.',
    f = '· · — ·',
    g = '— — ·',
    h = '· · · ·',
    i = '. .',
    j = '· — — —',
    k = '— · —',
    l = '· — · ·',
    m = '— —',
    n = '— ·',
    ñ = '— — · — —',
    o = '— — —',
    p = '. — — .',
    q = '— — · —',
    r = '· — ·',
    s = '·  · ·',
    t = '—',
    u = '· · —',
    v = '· · · —',
    w = '· — —',
    x = '— · · —',
    y = '— · — —',
    z = '— — · ·'
    )
#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x150")

def display_text():
    global entry
    string= entry.get()
    res = ""
    check = 0
    for i in string:
        if i == ' ':
            res = "Solo una palabra por favor"
            check = 1
        if check == 0:
            res = res + morse[i]
            res = res + "  "
    label.configure(text=res)

#Label info
info=Label(win, text="Introduce texto para convertirlo en morse", font=("Courier 18 bold"))
info.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 17"))
label.pack()
#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()