import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

app = tk.Tk()
app.title('Sliders')

# #Slider
# scaleFloat = tk.DoubleVar(value=15)
# scale = ttk.Scale(app, command=lambda value: progress.stop(), from_=0, to=30, length=300, orient='vertical', variable=scaleFloat)
# scale.pack()

# #Progress bar
# progress = ttk.Progressbar(app, variable=scaleFloat, maximum=30, mode='determinate', length=400)
# progress.pack()
# # progress.start()

# #Scrolled text
# scrolledText = scrolledtext.ScrolledText(app)
# scrolledText.pack()

exerciseInt = tk.IntVar()
exerciseProgress = ttk.Progressbar(app, orient='vertical', maximum=100, variable=exerciseInt)
exerciseProgress.pack()
exerciseProgress.start()

exerciseLabel = ttk.Label(app, textvariable=exerciseInt)
exerciseLabel.pack()

exerciseSlider = ttk.Scale(app, variable=exerciseInt, from_=0, to=100)
exerciseSlider.pack()

app.mainloop()