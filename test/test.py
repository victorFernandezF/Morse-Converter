import tkinter as tk

root = tk.Tk()

def show_it(event):
    text = write_me.get('1.0','end') #get the text
    write_me.delete('1.0','end') #delet the text
    write_me.index('insert')
    
    show_me.config(state='normal')
    show_me.insert('end', text)
    show_me.config(state='disabled')

write_me = tk.Text(root)
write_me.pack(side='left')
write_me.bind('<Return>', show_it)

show_me = tk.Text(root,state='disabled')
show_me.pack(side='right')

root.mailoop()