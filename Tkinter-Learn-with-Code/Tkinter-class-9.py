#Check BOX

#Step-1: Import Tkinter
from tkinter import *

#Step-2: GUI Interaction
window= Tk()

#Step-3: Input
window.title("Sample")
window.geometry("500x500")

chb_btn1=Checkbutton(window, text="apple", onvalue=1, offvalue=0, height=2, width=10)
chb_btn2=Checkbutton(window, text="plum", onvalue=1, offvalue=0, height=2, width=10)
chb_btn3=Checkbutton(window, text="mango", onvalue=1, offvalue=0, height=2, width=10)
chb_btn1.pack()
chb_btn2.pack()
chb_btn3.pack()

#Step-4: Mainloop
mainloop()