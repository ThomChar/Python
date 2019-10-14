# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *
from tkinter.messagebox import *
from math import *

# globally declare the expression variable
totalExpression = "" 
expression = ""
lastNumberInMemory = ""
lastOpInMemory = ""
piValue = str(pi)
mode=0


# Function to update expressiom 
# in the text entry box 
def press(num): 
	# point out the global expression variable 
	global totalExpression, expression, lastOpInMemory 

	if (lastOpInMemory != "="):
		expression = expression + str(num)
		currentNumber.set(expression)
	else:
		expression = str(num)
		currentNumber.set(expression)
		lastOpInMemory = ""

	if (totalExpression == " Erreur "):
		totalExpression = ""
		equation.set(totalExpression)
	# concatenation of string 
	#totalExpression = totalExpression + str(num)
	#expression = expression + str(num)  

	# update the expression by using set method 
	#equation.set(totalExpression)
	#currentNumber.set(expression)

def pressOp(operation): 
	# point out the global expression variable 
	global totalExpression, expression, lastNumberInMemory, lastOpInMemory 

	# concatenation of string 
	#totalExpression = totalExpression + str(num)
	totalExpression = totalExpression + expression + str(operation)
	lastNumberInMemory = expression
	lastOpInMemory = operation 
	

	# update the expression by using set method 
	equation.set(totalExpression)
	expression = ""
	currentNumber.set(expression)
	

# Function to evaluate the final expression 
def equalpress(): 
	# Try and except statement is used 
	# for handling the errors like zero 
	# division error etc. 

	# Put that code inside the try block 
	# which may generate the error 
	try: 

		global totalExpression,expression,lastNumberInMemory,lastOpInMemory

		# eval function evaluate the expression 
		# and str function convert the result 
		# into string 

		totalExpression = totalExpression + expression
		total = str(eval(totalExpression)) 
		expression = total
		currentNumber.set(expression)
		#equation.set(total) 
		#lastNumberInMemory = total

		# initialze the expression variable 
		# by empty string 
		totalExpression = ""
		equation.set(totalExpression)
		lastOpInMemory = "="

	# if error is generate then handle 
	# by the except block 
	except: 

		equation.set(" Erreur ")
		currentNumber.set("") 
		totalExpression = ""
		expression = "" 

def factofunction():

	global expression, lastOpInMemory
	#expression = ""
	#currentNumber.set(expression)
	if(expression == ""):
		press(1)
	else:
		factn = factorial(int(expression))
		expression = str(factn)
		currentNumber.set(expression)
		lastOpInMemory = ""

# Function to clear the contents 
# of text entry box 
def clear(): 
	global totalExpression, expression
	expression = "" 
	totalExpression = "" 
	equation.set("")
	currentNumber.set("0")

def alert():
    showinfo("Info", "hello")

def messageAide():
    showinfo("Aide", "Cette calculatrice possède 2 modes : \nBasique : Opérations de base\nScientifique : Opérations plus complexe")

def forgetButtonPosition():
	
	totalExpression_field.grid_forget()
	expression_field.grid_forget()
	button1.grid_forget()
	button2.grid_forget()
	button3.grid_forget()
	button4.grid_forget()
	button5.grid_forget()
	button6.grid_forget()
	button7.grid_forget()
	button8.grid_forget()
	button9.grid_forget()
	button0.grid_forget()
	plus.grid_forget()
	minus.grid_forget()
	multiply.grid_forget() 
	divide.grid_forget()
	changeSign.grid_forget()
	point.grid_forget()
	equal.grid_forget()
	clear.grid_forget()
	supCara.grid_forget()
	supNumber.grid_forget()
	parOuv.grid_forget()
	parFerm.grid_forget()
	pi.grid_forget()
	facto.grid_forget()
	seconde.grid_forget()
	

def ButtonBasic():
	gui.geometry("263x244")
	totalExpression_field.grid(columnspan=4, ipadx=70)
	expression_field.grid(columnspan=4, ipadx=70)
	button1.grid(row=5, column=0)
	button2.grid(row=5, column=1)
	button3.grid(row=5, column=2)
	button4.grid(row=4, column=0)
	button5.grid(row=4, column=1)
	button6.grid(row=4, column=2)
	button7.grid(row=3, column=0)
	button8.grid(row=3, column=1)
	button9.grid(row=3, column=2)
	button0.grid(row=6, column=1)
	plus.grid(row=2, column=3)
	minus.grid(row=3, column=3)
	multiply.grid(row=4, column=3)
	divide.grid(row=5, column=3)
	changeSign.grid(row=6, column=0)
	point.grid(row=6, column=2)
	equal.grid(row=6, column=3)
	clear.grid(row=2, column=1)
	supCara.grid(row=2, column=2)
	supNumber.grid(row=2, column=0)

def ButtonScientifique():
	gui.geometry("329x244")
	totalExpression_field.grid(columnspan=5, ipadx=102)
	expression_field.grid(columnspan=5, ipadx=102)
	button1.grid(row=5, column=1)
	button2.grid(row=5, column=2)
	button3.grid(row=5, column=3)
	button4.grid(row=4, column=1)
	button5.grid(row=4, column=2)
	button6.grid(row=4, column=3)
	button7.grid(row=3, column=1)
	button8.grid(row=3, column=2)
	button9.grid(row=3, column=3)
	button0.grid(row=6, column=2)
	plus.grid(row=2, column=4)
	minus.grid(row=3, column=4)
	multiply.grid(row=4, column=4)
	divide.grid(row=5, column=4)
	changeSign.grid(row=5, column=0)
	parOuv.grid(row=6, column=0)
	parFerm.grid(row=6, column=1)
	point.grid(row=6, column=3)
	equal.grid(row=6, column=4)
	clear.grid(row=2, column=2)
	supCara.grid(row=2, column=3)
	supNumber.grid(row=2, column=1)
	pi.grid(row=3, column=0)
	facto.grid(row=4, column=0)
	seconde.grid(row=2, column=0)

def changeMode(value):
	global mode
	mode = value
	if (mode == 0):
		forgetButtonPosition()
		ButtonBasic()
	elif (mode == 1):
		forgetButtonPosition()
		ButtonScientifique()

def changePosNeg():
	global totalExpression, expression
	if(expression !=""):
		if(float(expression)<0):
			expression = str(abs(float(expression)))
		else :
			expression = str(- float(expression))
		currentNumber.set(expression)		
	#elif(totalExpression !=""):
	#	if(int(totalExpression)<0):
	#		totalExpression = str(abs(int(totalExpression)))
	#	else :
	#		totalExpression = str(- int(totalExpression))
		#equation.set(expression)

# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="gray") 

	# set the title of GUI window 
	gui.title("Calculator") 

	# set the configuration of GUI window 
	gui.geometry("263x244") 

	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar()
	currentNumber = StringVar() 

	# create the text entry box for 
	# showing the expression
	totalExpression_field = Entry(gui, textvariable=equation, state="disabled", justify="right")
	expression_field = Entry(gui, textvariable=currentNumber, state="disabled", justify="right") 
	

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure .
	totalExpression_field.grid(columnspan=4, ipadx=70)
	expression_field.grid(columnspan=4, ipadx=70) 

	#Add a menu bar
	menubar = Menu(gui)

	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Basique",command= lambda : changeMode(0))
	menu1.add_command(label="Scientifique",command= lambda : changeMode(1))
	menu1.add_separator()
	menu1.add_command(label="Aide",command=messageAide)
	menu1.add_separator()
	menu1.add_command(label="Quitter", command=gui.quit)
	menubar.add_cascade(label="Menu", menu=menu1)

	gui.config(menu=menubar)

	equation.set('')
	currentNumber.set('0')

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed .
	#print(mode)
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
				command=lambda: pressOp("+"), height=2, width=7) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='white', 
				command=lambda: pressOp("-"), height=2, width=7) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' * ', fg='black', bg='white', 
					command=lambda: pressOp("*"), height=2, width=7) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='white', 
					command=lambda: pressOp("/"), height=2, width=7) 
	divide.grid(row=5, column=3) 

	changeSign = Button(gui, text=' +/- ', fg='black', bg='white', 
				command=changePosNeg, height=2, width=7) 
	changeSign.grid(row=6, column=0) 

	point = Button(gui, text=' . ', fg='black', bg='white', 
				command= lambda : press("."), height=2, width=7) 
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

	# Bouton pour la version scientifique
	seconde = Button(gui, text='2nd', fg='black', bg='white', 
				 state="disabled", height=2, width=7)
	pi = Button(gui, text='pi', fg='black', bg='white', 
				command= lambda : press(piValue), height=2, width=7)
	facto = Button(gui, text='n!', fg='black', bg='white', 
				command= lambda : factofunction(), height=2, width=7)
	parOuv = Button(gui, text='(', fg='black', bg='white', 
				command= lambda : press("("), height=2, width=7)
	parFerm = Button(gui, text=')', fg='black', bg='white', 
				command= lambda : press(")"), height=2, width=7)
	
	
	#print(str(''.format(pi, '.14f')))
	# start the GUI 
	gui.mainloop() 
