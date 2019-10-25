# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *
from tkinter.messagebox import *
from math import *
from markov1 import *
import tkinter.font as tkFont
from pathlib import Path

# globally declare the expression variable

def messageAide():
    showinfo("Aide", "Veuillez choisir un type de chaine de markov et rentrer les paramètres appropriés pour obtenir un résultat")

def forgetButtonPosition():
	
	button1.grid_forget()
	button2.grid_forget()
	button3.grid_forget()


# Driver code 
if __name__ == "__main__": 
    
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="white") 

	# set the title of GUI window 
	gui.title("Processus Stochastique") 

	# set the configuration of GUI window 
	w =  gui.winfo_screenwidth()/2-160
	h =  gui.winfo_screenheight()/2-180
	gui.geometry("350x250+"+str(int(w))+"+"+str(int(h))) 

	gui.resizable(0,0)

	rows = 0 
	while rows < 3:
		gui.rowconfigure(rows,weight=1)
		gui.columnconfigure(rows,weight=1)
		rows +=1

	# create the text entry box for 
	# showing the expression
	helv20 = tkFont.Font(family='Helvetica', size=20, weight='normal')

	Label(gui, font=helv20,text='Chaine de Markov',background="white").grid(columnspan=3, ipadx=60)

	Label(gui, text='Indications:\nVeuillez chosir un type de chaine de markov à exploiter',background="white").grid(columnspan=3, ipadx=60)

	#Add a menu bar
	menubar = Menu(gui)

	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Aide",command=messageAide)
	menu1.add_separator()
	menu1.add_command(label="Quitter", command=gui.quit)
	menubar.add_cascade(label="Menu", menu=menu1)

	gui.config(menu=menubar)

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed .
	#print(mode)
	button1 = Button(gui, command= registerParamMarkov1, text=' M/M/1 ', fg='black', bg='white', height=2, width=7)
	button1.grid(row=2, column=0) 

	button2 = Button(gui, command= registerParamMarkov1K, text=' M/M/1/K ', fg='black', bg='white', height=2, width=7)
	button2.grid(row=2, column=1) 

	button3 = Button(gui, command= registerParamMarkovS, text=' M/M/S ', fg='black', bg='white', height=2, width=7)
	button3.grid(row=2, column=2) 
    


	gui.mainloop() 
