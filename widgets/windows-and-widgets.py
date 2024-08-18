import tkinter as tk
from tkinter import ttk

def buttonFunction():
    print('The button was pressed')

def helloFunction():
    print('hello')

app = tk.Tk()
app.title('app widgets')
app.geometry('800x500')

label = ttk.Label(master=app, text='This is a test')
label.pack()

text = tk.Text(master=app)
text.pack()

entry = ttk.Entry(master=app)
entry.pack()

myLabel = ttk.Label(master=app, text='my label')
myLabel.pack()

button = ttk.Button(master=app, text='A button', command=buttonFunction)
button.pack()

helloButton = ttk.Button(master=app, text='hello button', command=helloFunction)
helloButton.pack()

app.mainloop()