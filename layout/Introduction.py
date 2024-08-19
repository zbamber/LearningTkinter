import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title('Layout intro')
app.geometry('600x400')

label1 = ttk.Label(app, text='Label1', background='red')
label2 = ttk.Label(app, text='Label2', background='blue')

# #Pack
# label1.pack(side='left', expand=True, fill='both')
# label2.pack(side='left', expand=True, fill='both')


# #Grid
# app.columnconfigure(0,weight=1)
# app.columnconfigure(1,weight=1)
# app.columnconfigure(2,weight=2)
# app.rowconfigure(0,weight=1)
# app.rowconfigure(1,weight=1)

# label1.grid(row=0,column=2, sticky='nsew')
# label2.grid(row=1, column=1, sticky='nsew', columnspan=2)

#Place
label1.place(x=100, y=100, width=200, height=100)
label2.place(relx=0.5, rely=0.5, relwidth=1, anchor='center')


app.mainloop()