#Project: Complete Functional Basic Calculator Using Tkinter-Python

#Step-1: Import Tkinter:
from tkinter import *

#Step-2: GUI connection
window=Tk()
window.title("Calculator")
window.geometry("230x280")

#Step-3:Inputs/ Code:

#Labeling and Entry
l1=Label(window,text="BASIC CALCULATOR",relief=RAISED,bg="green",fg="white")
l1.pack(side=TOP)
e1=Entry(window, width=33, borderwidth=5)
e1.place(x=5,y=40)

#Button
def click(num):
    res=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(res)+str(num))
b=Button(window, text="1", width=8, command=lambda:click(1))
b.place(x=5, y=80)
b=Button(window, text="2", width=8, command=lambda:click(2))
b.place(x=70, y=80)
b=Button(window, text="3", width=8,command=lambda:click(3))
b.place(x=140, y=80)
b=Button(window, text="4", width=8,command=lambda:click(4))
b.place(x=5, y=110)
b=Button(window, text="5", width=8,command=lambda:click(5))
b.place(x=70, y=110)
b=Button(window, text="6", width=8,command=lambda:click(6))
b.place(x=140, y=110)
b=Button(window, text="7", width=8,command=lambda:click(7))
b.place(x=5, y=140)
b=Button(window, text="8", width=8,command=lambda:click(8))
b.place(x=70, y=140)
b=Button(window, text="9", width=8,command=lambda:click(9))
b.place(x=140, y=140)
b=Button(window, text="0", width=8,command=lambda:click(0))
b.place(x=5, y=170)

#Calculation Logics:
def add():
    n1=e1.get()
    global i,math
    math="Add"
    i = int(n1)
    e1.delete(0, END)
def subt():
    n1=e1.get()
    global i,math
    math="Subt"
    i=int(n1)
    e1.delete(0,END)
def mult():
    n1=e1.get()
    global i,math
    math="Mult"
    i=int(n1)
    e1.delete(0,END)
def div():
    n1=e1.get()
    global i,math
    math="Divide"
    i=int(n1)
    e1.delete(0,END)
def equal():
    n2=e1.get()
    global math
    e1.delete(0,END)
    try:
     if math=="Add":
        e1.insert(0,i+int(n2))
     elif math=="Subt":
        e1.insert(0,i-int(n2))
     elif math=="Mult":
        e1.insert(0, i*int(n2))
     elif math=="Divide":
        e1.insert(0, i/int(n2))
    except ZeroDivisionError:
        print("Error!!")
def clear():
    e1.delete(0,END)

b=Button(window, text="+",width=8,command=add)
b.place(x=70, y=170)
b=Button(window, text="-", width=8,command=subt)
b.place(x=140, y=170)
b=Button(window, text="/", width=8,command=div)
b.place(x=5, y=200)
b=Button(window, text="*", width=8,command=mult)
b.place(x=70, y=200)
b=Button(window, text="=", width=8,command=equal)
b.place(x=140, y=200)
b=Button(window, text="clear", width=28,command=clear)
b.place(x=5, y=230)

#Step-4:main loop call
mainloop()