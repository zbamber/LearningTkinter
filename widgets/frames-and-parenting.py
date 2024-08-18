import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry('600x400')
app.title('Frames and Parenting')

frame = ttk.Frame(app, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
#Stop the parent collapsing on its children
frame.pack_propagate(False)
frame.pack(side='left')

label = ttk.Label(frame, text='label in frame')
label.pack()

button = ttk.Button(frame, text='button in a frame')
button.pack()

label2 = ttk.Label(app, text='label outside the frame')
label2.pack(side='left')

exerciseframe = ttk.Frame(app, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
#Stop the parent collapsing on its children
exerciseframe.pack_propagate(False)
exerciseframe.pack(side='left')

exerciselabel = ttk.Label(exerciseframe, text='label in frame')
exerciselabel.pack()

exercisebutton = ttk.Button(exerciseframe, text='button in a frame')
exercisebutton.pack()


app.mainloop()