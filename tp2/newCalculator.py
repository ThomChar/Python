# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *
from tkinter.messagebox import *

# globally declare the expression variable 
expression = "" 


# Function to update expressiom 
# in the text entry box 
def press(num): 
	# point out the global expression variable 
	global expression 

	# concatenation of string 
	expression = expression + str(num) 

	# update the expression by using set method 
	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	# Try and except statement is used 
	# for handling the errors like zero 
	# division error etc. 

	# Put that code inside the try block 
	# which may generate the error 
	try: 

		global expression 

		# eval function evaluate the expression 
		# and str function convert the result 
		# into string 
		total = str(eval(expression)) 

		equation.set(total) 

		# initialze the expression variable 
		# by empty string 
		expression = "" 

	# if error is generate then handle 
	# by the except block 
	except: 

		equation.set(" error ") 
		expression = "" 


# Function to clear the contents 
# of text entry box 
def clear(): 
	global expression 
	expression = "" 
	equation.set("0")

def alert():
    showinfo("Info", "hello")

def changePosNeg():
	global expression
	if(expression !=""):
		if(int(expression)<0):
			expression = str(abs(int(expression)))
		else :
			expression = str(- int(expression))
		equation.set(expression)

# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="gray") 

	# set the title of GUI window 
	gui.title("Calculator") 

	# set the configuration of GUI window 
	gui.geometry("264x226") 

	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for 
	# showing the expression . 
	expression_field = Entry(gui, textvariable=equation) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	expression_field.grid(columnspan=4, ipadx=70) 

	#Add a menu bar
	menubar = Menu(gui)

	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Basique",command=alert)
	menu1.add_command(label="Scientifique",command=alert)
	menu1.add_separator()
	menu1.add_command(label="Aide",command=alert)
	menu1.add_separator()
	menu1.add_command(label="Quitter", command=gui.quit)
	menubar.add_cascade(label="Menu", menu=menu1)

	gui.config(menu=menubar)

	equation.set('0') 

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	button1 = Button(gui, text=' 1 ', fg='black', bg='white', 
					command=lambda: press(1), height=2, width=7) 
	button1.grid(row=5, column=0) 

	button2 = Button(gui, text=' 2 ', fg='black', bg='white', 
					command=lambda: press(2), height=2, width=7) 
	button2.grid(row=5, column=1) 

	button3 = Button(gui, text=' 3 ', fg='black', bg='white', 
					command=lambda: press(3), height=2, width=7) 
	button3.grid(row=5, column=2) 

	button4 = Button(gui, text=' 4 ', fg='black', bg='white', 
					command=lambda: press(4), height=2, width=7) 
	button4.grid(row=4, column=0) 

	button5 = Button(gui, text=' 5 ', fg='black', bg='white', 
					command=lambda: press(5), height=2, width=7) 
	button5.grid(row=4, column=1) 

	button6 = Button(gui, text=' 6 ', fg='black', bg='white', 
					command=lambda: press(6), height=2, width=7) 
	button6.grid(row=4, column=2) 

	button7 = Button(gui, text=' 7 ', fg='black', bg='white', 
					command=lambda: press(7), height=2, width=7) 
	button7.grid(row=3, column=0) 

	button8 = Button(gui, text=' 8 ', fg='black', bg='white', 
					command=lambda: press(8), height=2, width=7) 
	button8.grid(row=3, column=1) 

	button9 = Button(gui, text=' 9 ', fg='black', bg='white', 
					command=lambda: press(9), height=2, width=7) 
	button9.grid(row=3, column=2) 

	button0 = Button(gui, text=' 0 ', fg='black', bg='white', 
					command=lambda: press(0), height=2, width=7) 
	button0.grid(row=6, column=1) 

	plus = Button(gui, text=' + ', fg='black', bg='white', 
				command=lambda: press("+"), height=2, width=7) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='white', 
				command=lambda: press("-"), height=2, width=7) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' * ', fg='black', bg='white', 
					command=lambda: press("*"), height=2, width=7) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='white', 
					command=lambda: press("/"), height=2, width=7) 
	divide.grid(row=5, column=3) 

	changeSign = Button(gui, text=' +/- ', fg='black', bg='white', 
				command=changePosNeg, height=2, width=7) 
	changeSign.grid(row=6, column=0) 

	point = Button(gui, text=' . ', fg='black', bg='white', 
				command=equalpress, height=2, width=7) 
	point.grid(row=6, column=2) 

	equal = Button(gui, text=' = ', fg='black', bg='white', 
				command=equalpress, height=2, width=7) 
	equal.grid(row=6, column=3) 

	clear = Button(gui, text='Clear', fg='black', bg='white', 
				command=clear, height=2, width=7) 
	clear.grid(row=2, column=1) 

	supCara = Button(gui, text='<-', fg='black', bg='white', 
				command=clear, height=2, width=7) 
	supCara.grid(row=2, column=2) 

	supNumber = Button(gui, text='CE', fg='black', bg='white', 
				command=clear, height=2, width=7) 
	supNumber.grid(row=2, column=0) 

	# start the GUI 
	gui.mainloop() 
