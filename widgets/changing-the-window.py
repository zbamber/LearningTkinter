import tkinter as tk
from tkinter import ttk

app = tk.Tk()
# app.geometry('600x400+200+200') #The + indicates the relative position of the window when it loads
app.title('More on the window')
# app.iconbitmap('anImage.ico') will add an image instead of the tkinter logo in the top left

app.geometry(f'600x400+{int(app.winfo_screenwidth() / 2)-300}+{int(app.winfo_screenheight() / 2)-200}')


# app.minsize(200,200)
# app.maxsize(800,800)

app.resizable(True,True)

print(app.winfo_screenwidth())
print(app.winfo_screenheight())

# # app.attributes('-alpha', 0.5) to make it see through
app.attributes('-topmost',True)


# #security event
app.bind('<Escape>', lambda event: app.quit())

# app.attributes('-disable', True)

# app.attributes('-fullscreen', True)

app.overrideredirect(True)
grip = ttk.Sizegrip(app)
grip.place(relx=1.0, rely=1.0, anchor='se')

app.mainloop()