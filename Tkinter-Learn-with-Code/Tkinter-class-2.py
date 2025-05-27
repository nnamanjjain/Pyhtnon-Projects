#2. Basic Modifications, Frames, Buttons:

#Step-1: Import Tkinter
from tkinter import *

#Step-2: GUI Interaction
window= Tk()

#Step-3: Input
'''
inp= Label(window,text= "HELLO WORLD!")
inp.pack()
'''
window.title("Sample")
#window.config(bg="green")
window.geometry("500x500")

frame1=Frame(window, bg="red", width=300, height=100, cursor='dot')
frame2=Frame(window, bg="green", width=300, height=100, cursor='dotbox')
button1=Button(frame1, text="Button-1", bg="blue")
button2=Button(frame2, text="Button-2", bg="green")
button3=Button(frame1, text="Button-3", bg="red")
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
button2.pack()
button3.pack()

#Step-4: Mainloop
mainloop()