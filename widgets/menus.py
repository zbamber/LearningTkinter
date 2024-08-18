import tkinter as tk
from tkinter import ttk

# docs: https://www.tutorialspoint.com/python/tk_menu.htm

app = tk.Tk()
app.geometry('600x400')
app.title('Menu')

menu = tk.Menu(app)
fileMenu = tk.Menu(menu, tearoff=False)
fileMenu.add_command(label='New', command=lambda: print('new File'))
fileMenu.add_command(label='Open', command=lambda: print('open File'))
fileMenu.add_separator()
menu.add_cascade(label='File', menu=fileMenu)

helpCheckString = tk.StringVar()
helpMenu = tk.Menu(menu, tearoff=False)
helpMenu.add_command(label='Help entry', command=lambda: print(helpCheckString.get()))
helpMenu.add_checkbutton(label='check', onvalue='on', offvalue='off', variable=helpCheckString)

menu.add_cascade(label='help', menu=helpMenu)

anotherMenu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label='another menu', menu=anotherMenu)

subMenu = tk.Menu(menu, tearoff=False)
subMenu.add_command(label='sub sub sub subs ubs')
anotherMenu.add_cascade(label='more stuff', menu=subMenu)

app.configure(menu=menu)

menuButton = ttk.Menubutton(app, text='Menu Button')
menuButton.pack()

buttonSubMenu = tk.Menu(menuButton, tearoff=False)
buttonSubMenu.add_command(label='entry 1', command=lambda: print('test 1'))
buttonSubMenu.add_command(label='check 1')
menuButton.configure(menu=buttonSubMenu)


app.mainloop()