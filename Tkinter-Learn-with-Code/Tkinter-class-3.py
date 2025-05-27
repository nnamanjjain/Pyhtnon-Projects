#Entry-Box, Grid Layout:

#Step-1: Import Tkinter
from tkinter import *

#Step-2: GUI Interaction
window= Tk()

#Step-3: Input
window.title("Sample")
window.geometry("500x500")

label1=Label(window, text="E-mail:")
label2=Label(window, text="Password:")
e1=Entry(window, width=40, borderwidth=5)
e2=Entry(window, width=40, borderwidth=5)
label1.grid(row=0, column=1)
label2.grid(row=1, column=1)
e1.grid(row=0, column=2)
e2.grid(row=1, column=2)

#Step-4: Mainloop
mainloop()