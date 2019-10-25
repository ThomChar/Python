# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *
from tkinter.messagebox import *
from math import *

# globally declare the expression variable

def messageAide():
    showinfo("Aide", "Message d'aide")

# Driver code 
def register():
    toplevel = Toplevel()

    Label(toplevel, text='MMS').pack(padx=30, pady=30)
    toplevel.grab_set() 

