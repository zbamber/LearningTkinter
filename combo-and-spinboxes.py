import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry('600x400')
app.title('Combo and Spin')

#Combobox
items = ['Ice cream', 'Pizza', 'Brocolli']
foodString = tk.StringVar(value=items[0])
combo = ttk.Combobox(app, textvariable=foodString)
combo['values'] = items
combo.pack()

combo.bind('<<ComboboxSelected>>', lambda event: comboLabel.configure(text=f'Selected Value: {foodString.get()}'))
comboLabel = ttk.Label(app, text='Selected value:')
comboLabel.pack()

#Spinbox
spinInt = tk.IntVar(value=12)
spin = ttk.Spinbox(app, from_=3, to=20, increment=3, textvariable=spinInt)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
spin.pack()

#Exercise
exerciseValues = ['A', 'B', 'C', 'D', 'E']
exerciseSpinString = tk.StringVar()
exerciseSpin = ttk.Spinbox(app, textvariable=exerciseSpinString, values=exerciseValues)
exerciseSpin.bind('<<Decrement>>', lambda event: print(exerciseSpinString.get()))
exerciseSpin.pack()




app.mainloop()