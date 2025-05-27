#PACK Vs GRID:

#Step-1: Import Tkinter
from tkinter import *

#Step-2: GUI Interaction
window= Tk()

#Step-3: Input
window.title("Sample")
window.geometry("500x500")
label1=Label(window, bg="red", text="Label-1", fg="white")
label2=Label(window, bg="green", text="Label-2", fg="white")
label3=Label(window, bg="blue", text="Label-3", fg="white")

label1.pack(side=TOP, fill=X, expand=False)
label2.pack(side=RIGHT, fill=Y, expand=False)
label3.pack(side=LEFT, fill=Y, expand=False)

#Step-4: Mainloop
mainloop()