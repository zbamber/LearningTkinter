import tkinter as tk
from tkinter import ttk

def buttonFunction(entryString):
    print('a button was pressed')
    print(entryString.get())


app = tk.Tk()
app.title('buttons, functions and arguments')

entryString = tk.StringVar(value='test')
entry = ttk.Entry(app, textvariable=entryString)
entry.pack()

button = ttk.Button(app, text='button', command=lambda:buttonFunction(entryString=entryString))
button.pack()

app.mainloop()