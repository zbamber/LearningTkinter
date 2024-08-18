import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry('600x400')
app.title('Tab widget')

notebook = ttk.Notebook(app)
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text='A label in tab1')
label1.pack()
button1 = ttk.Button(tab1, text='A button in tab1')
button1.pack()

tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text='A label in tab2')
label2.pack()
entry = ttk.Entry(tab2)
entry.pack()

tab3 = ttk.Frame(notebook)
exerciseButton1 = ttk.Button(tab3, text='button 1')
exerciseButton2 = ttk.Button(tab3, text='button 2')
exerciseLabel = ttk.Label(tab3, text='Some text in tab3')

notebook.add(tab1, text='tab1')
notebook.add(tab2, text='tab2')
notebook.add(tab3, text='tab3')

notebook.pack()

app.mainloop()