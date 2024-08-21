import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title('Pack parenting')
app.geometry('400x600')

topFrame = ttk.Frame(app)
label1 = ttk.Label(topFrame, text='First Label', background='red')
label2 = ttk.Label(topFrame, text='Second Label', background='blue')

label3 = ttk.Label(app, text='Another Label', background='green')

bottomFrame = ttk.Frame(app)
label4 = ttk.Label(bottomFrame, text='Last of the labels', background='orange')
button1 = ttk.Button(bottomFrame, text='A button')
button2 = ttk.Button(bottomFrame, text='Another button')

label1.pack(fill='both', expand=True)
label2.pack(fill='both', expand=True)
topFrame.pack(fill='both', expand=True)

sideFrame = ttk.Frame(bottomFrame)
button3 = ttk.Button(sideFrame, text='Button 3')
button4 = ttk.Button(sideFrame, text='Button 4')
button5 = ttk.Button(sideFrame, text='Button 5')


label3.pack(expand=True)

button3.pack(expand=True, fill='both')
button4.pack(expand=True, fill='both')
button5.pack(expand=True, fill='both')
sideFrame.pack(side='right', expand=True, fill='both')

button1.pack(side='left', expand=True, fill='both')
label4.pack(side='left', expand=True, fill='both')
button2.pack(side='left', expand=True, fill='both')
bottomFrame.pack(expand=True, fill='both', padx=10, pady=10)




app.mainloop()