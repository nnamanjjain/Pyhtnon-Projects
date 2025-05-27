#Button Handling:

#Step-1: Import Tkinter
from tkinter import *

#Step-2: GUI Interaction
window= Tk()

#Step-3: Input

window.title("Sample")
window.geometry("500x500")

def log_entry():
    print("Logged-in!!")

button1=Button(window, text="Login", bg="blue", fg="white",command=log_entry, activebackground="black", activeforeground="white",width=20,borderwidth=5,font=10)
button1.pack()


#Step-4: Mainloop
mainloop()