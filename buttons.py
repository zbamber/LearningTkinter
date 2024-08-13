import tkinter as tk
from tkinter import ttk

def buttonFunction():
    print('a basic button')
    print(radioVar.get())

app = tk.Tk()
app.title('buttons')
app.geometry('600x400')

# the basic button other than styling this is about all you can do with it
buttonString = tk.StringVar(value='a button with string var')
button = ttk.Button(app, command=buttonFunction, textvariable=buttonString)
button.pack()

checkVar = tk.IntVar(value=10)
check1 = ttk.Checkbutton(app, text='checkbox1', command=lambda: print(checkVar.get()), variable=checkVar, onvalue=10, offvalue=5)
check1.pack()

check2 = ttk.Checkbutton(app, text='checkbox 2', command=lambda: print('test'))
check2.pack()

radioVar = tk.StringVar()
radio = ttk.Radiobutton(app, text='radio button 1', value='radio 1', variable=radioVar, command=lambda: print(radioVar.get()))
radio.pack()

radio2 = ttk.Radiobutton(app, text='radio button 2', value=2, variable=radioVar)
radio2.pack()

def handleRadioButton():
    print(exerciseCheckButtonVar.get())
    exerciseCheckButtonVar.set(False)
    

exerciseRadioVar = tk.StringVar()
exerciseCheckButtonVar = tk.BooleanVar()

exerciseRadio1 = ttk.Radiobutton(app, text='checkbutton A', value='A', command=handleRadioButton, variable=exerciseRadioVar)
exerciseRadio1.pack()

exerciseRadio2 = ttk.Radiobutton(app, text='checkbutton B', value='B', command=handleRadioButton, variable=exerciseRadioVar)
exerciseRadio2.pack()

exerciseCheckButton = ttk.Checkbutton(app, text='exercise check button', variable=exerciseCheckButtonVar, command=lambda: print(exerciseRadioVar.get()))
exerciseCheckButton.pack()

app.mainloop()