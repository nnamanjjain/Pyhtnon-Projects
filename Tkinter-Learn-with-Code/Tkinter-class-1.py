#Tkinter Class Notes:

#1. HELLO World using Tkinter

#Step-1: Import Tkinter
from tkinter import *

#Step-2: GUI Interaction
window= Tk()

#Step-3: Input
inp= Label(window,text= "HELLO WORLD!")
inp.pack()

#Step-4: Mainloop
mainloop()