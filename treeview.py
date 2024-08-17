import tkinter as tk
from tkinter import ttk
from random import choice

app = tk.Tk()
app.geometry('600x400')
app.title('Treeview')

firstNames = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
lastNames = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

table = ttk.Treeview(app, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First name')
table.heading('last', text='Last name')
table.heading('email', text='Email')
table.pack()
#table.insert(parent='', index=0, values=('John', 'Doe', 'johndoe@email.com'))

for i in range(100):
    first = choice(firstNames)
    last = choice(lastNames)
    email = f'{first}{last}@email.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values=data)

#to insert a new item at the end  ↓
table.insert(parent='', index=tk.END, values=('XXXX', 'YYYY', 'ZZZZ'))

#events
def itemSelect(_): #the underscore denotes that I dont care about what is being passed in because im not going to use event anyway
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])
    #table.item(table.selection())

def deleteItems(_):
    print('deleted')
    for i in table.selection():
        table.delete(i)


table.bind('<<TreeviewSelect>>', itemSelect)
table.bind('<Delete>', deleteItems)

app.mainloop()