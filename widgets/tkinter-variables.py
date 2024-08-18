import tkinter as tk
from tkinter import ttk

def buttonFunction():
    print(stringVar.get())
    stringVar.set('button pressed')

app = tk.Tk()
app.title('tkinter variables')

#create the tkinter variable
stringVar = tk.StringVar()
anotherStringVar = tk.StringVar(value='test')

label = ttk.Label(master=app, text='start text', textvariable=stringVar)
label.pack()

entry = ttk.Entry(master=app, textvariable=stringVar)
entry.pack()

button = ttk.Button(master=app, text='button', command=buttonFunction)
button.pack()

entryField = ttk.Entry(master=app, textvariable=anotherStringVar)
entryField.pack()

entryField2 = ttk.Entry(master=app, textvariable=anotherStringVar)
entryField2.pack()

label2 = ttk.Label(master=app, textvariable=anotherStringVar)
label2.pack()

app.mainloop()