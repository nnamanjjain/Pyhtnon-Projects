#Menu-Bar:

#Step-1: Import Tkinter
from tkinter import *

#Step-2: GUI Interaction
window= Tk()

#Step-3: Input
window.title("Sample")
window.geometry("500x500")

menu1=Menu(window)
file=Menu(menu1, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As..")
file.add_separator()
file.add_command(label="Exit", command=window.quit)
menu1.add_cascade(label="FILE", menu=file)
window.config(menu=menu1)

#Step-4: Mainloop
mainloop()