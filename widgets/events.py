import tkinter as tk
from tkinter import ttk

def getPosition(event):
    print(f'x: {event.x} y: {event.y}')

app = tk.Tk()
app.geometry('600x500')
app.title('Event binding')

text = tk.Text(app)
text.pack()

entry = ttk.Entry(app)
entry.pack()

button = ttk.Button(app, text='a button')
button.pack()

#examples of events
app.bind('<Alt-KeyPress-a>', lambda event: print(event))
text.bind('<Motion>', getPosition)
app.bind('<KeyPress>', lambda event: print(f'{event.char} was pressed'))
entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

text.bind('<Shift-MouseWheel>', lambda event: print('MouseWheel'))

app.mainloop()