#Drawing using Tkinter:

#Step-1: Import Tkinter
from tkinter import *

#Step-2: GUI Interaction
window= Tk()

#Step-3: Input
window.title("Sample")
#window.geometry("500x500")
c=Canvas(window, width=300, height=300)
c.create_line(0,0,300,300, fill="green", width=5, dash=(3,3))
c.create_line(0,300,300,0, fill="red", width=5, dash=(3,3))
c.create_rectangle(100,150,200,100, fill="red", outline="green",width=3)
c.pack()

#Step-4: Mainloop
mainloop()