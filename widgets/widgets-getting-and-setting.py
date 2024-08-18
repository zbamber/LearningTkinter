import tkinter as tk
from tkinter import ttk

def buttonFunction():
    contents = entry.get()
    label['text'] = contents
    entry['state'] = 'disabled'

def resetButtonFunction():
    label['text'] = 'some text'
    entry['state'] = 'enabled'
    entry['text'] = 'this is a test'

app = tk.Tk()
app.title('getting and setting widgets')

label = ttk.Label(master=app, text='whatever i want')
label.pack()

entry = ttk.Entry(master=app)
entry.pack()

button = ttk.Button(master=app,command=buttonFunction, text='submit')
button.pack()

resetButton = ttk.Button(master=app,text='reset', command=resetButtonFunction)
resetButton.pack()

app.mainloop()