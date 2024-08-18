import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    miles = float(entry.get()) * 1.609
    output.configure(text= f'{miles}miles')

app = ttk.Window(themename='darkly')
app.title('demo')
app.geometry('300x150')
app.attributes('-topmost', True)


titleLbl = ttk.Label(master=app, text='Miles to Kilometres', font='Calibri 24 bold')
titleLbl.pack()

inputField = ttk.Frame(master=app)
entry = ttk.Entry(master=inputField)
submitBtn = ttk.Button(master=inputField, text='convert',command=convert)
entry.pack(side='left', padx=10)
submitBtn.pack()
inputField.pack()

output = ttk.Label(master=app, text='', font='Calibri 24')
output.pack()

app.mainloop()
