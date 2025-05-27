#Message-BOX:

#Step-1: Import Tkinter
from tkinter import *
import tkinter.messagebox

#Step-2: GUI Interaction
window= Tk()

#Step-3: Input
window.title("Sample")
window.geometry("500x500")
'''
#1. PreDefined MessageBox:
tkinter.messagebox.showinfo("Info","Running Out of Time!")
tkinter.messagebox.showwarning("Warning","Running Out of Time!")
tkinter.messagebox.showerror("Error","Running Out of Time!")

ques=tkinter.messagebox.askyesno("Weather","Will It Rain?")
if ques==True:
    print("Take an Umbrella.")
else:
    print("OK")
'''

#2. Custom MessageBox:

message1=Message(window, text="Python")

var=StringVar()
var.set("Welcome")
message2=Message(window, textvariable=var, relief=RAISED,padx=20, pady=20)

var1=StringVar()
ent_var=StringVar()

def insert():
    result=ent_var.get()
    var1.set(result)

message3=Message(window, textvariable=var1, relief=RAISED,padx=20, pady=20)
entry=Entry(window, textvariable=ent_var)
button=Button(window, text="OK", command=insert)

message1.pack()
message2.pack()
message3.pack()
entry.pack()
button.pack()
#Step-4: Mainloop
mainloop()