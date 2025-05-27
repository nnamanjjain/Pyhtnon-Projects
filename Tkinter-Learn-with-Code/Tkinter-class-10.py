#Place Vs Grid Vs Pack

#Step-1: Import Tkinter
from tkinter import *

#Step-2: GUI Interaction
window= Tk()

#Step-3: Input
window.title("Sample")
window.geometry("500x500")
button=Button(window,text="Button-1", width=20)
button.place(x=200, y=100)

#Step-4: Mainloop
mainloop()