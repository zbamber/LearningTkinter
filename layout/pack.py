import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry('600x400')
app.title('Pack')

label1 = ttk.Label(app, text='First Label', background='red')
label2 = ttk.Label(app, text='Second Label', background='blue')
label3 = ttk.Label(app, text='Last of the Labels', background='green')
button = ttk.Button(app, text='Button')

label1.pack(expand=True, fill='both', padx=10, pady=10)
label2.pack(expand=True, fill='both', side='left')  
label3.pack(expand=True, fill='both')
button.pack(expand=True, fill='both')

app.mainloop()