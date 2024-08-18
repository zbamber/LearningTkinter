import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry('600x400')
app.title('Canvas')

canvas = tk.Canvas(app, background='white')
canvas.pack()

# #Important! the coordinates are relative to the origin being the top left corner of the canvas not the window
# canvas.create_rectangle((50,20,100,200), fill='blue', width=10, outline='cyan')
# canvas.create_line(0,0,600,400)
# #Polygon is very versatile so i will explain how to use
# #canvas.create_polygon(x1,y1,x2,y2,x3,y3) etc to mark each verticeeee
# #passing the coordinates as a tuple also works e.g canvas.create_polygon((x1,y1,x2,y2,x3,y3))
# canvas.create_polygon(0,0,100,200,300,50)

# #PIE CHART?
# canvas.create_oval((200,10,300,110), fill='green')
# canvas.create_arc((200,10,300,110), fill='red', start=45, extent=45)

# canvas.create_text((100,200), text='Some text')

# canvas.create_window((50, 100), window=ttk.Label(app, text='some text in the canvas'))
MBPressed = False
def onMBPressed():
    global MBPressed
    MBPressed = True
    print(f'set to: {MBPressed}')
def onMBReleased():
    global MBPressed
    MBPressed = False
    print(f'set to: {MBPressed}')
def handleDrawing(event, MBPressed):
    print(MBPressed)
    if MBPressed == True:
        canvas.create_oval((event.x, event.y, event.x + 2, event.y + 2))
    
canvas.bind('<Button>', lambda event: onMBPressed())
canvas.bind('<ButtonRelease>', lambda event: onMBReleased())
canvas.bind('<Motion>', lambda event: handleDrawing(event=event, MBPressed=MBPressed))


app.mainloop()