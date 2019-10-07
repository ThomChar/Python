from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()
fenetre.geometry("230x270+300+200")
fenetre.title("Calculatrice")
nb1 = ""

def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Basique", command=alert)
menu1.add_command(label="Scientifique", command=alert)
menu1.add_separator()
menu1.add_command(label="Aide", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Menu", menu=menu1)

fenetre.config(menu=menubar)

def ajout(nb):
    global nb1
    nb1 += nb
    label["text"]= nb1

def num1():
    ajout("1")

def num2():
    ajout("2")

def num3():
    ajout("3")

def num4():
    ajout("4")

def num5():
    ajout("5")

def num6():
    ajout("6")

def num7():
    ajout("7")

def num8():
    ajout("8")

def num9():
    ajout("9")

def num0():
    ajout("0")

def point():
    ajout(".")

def clear():
    global nb1,nb2
    nb1=""
    nb2 =""
    label["text"] = nb1

def clearCurrentnb():
    global nb1,nb2
    if(op == 0):
        nb1 =""
        label["text"] = nb1
    else:
        nb2=""
        label["text"] = nb2

def add():
    global nb1,op,nb2
    nb2 = float(nb1)
    nb1 =""
    op = 1
    label["text"] = "+"

def dif():
    global nb1,op,nb2
    nb2 = float(nb1)
    nb1 =""
    op = 2
    label["text"] = "-"

def mult():
    global nb1,op,nb2
    nb2 = float(nb1)
    nb1 =""
    op = 3
    label["text"] = "*"

def div():
    global nb1,op,nb2
    nb2 = float(nb1)
    nb1 =""
    op = 4
    label["text"] = "/"

def egal():
    global nb1
    if(nb1!=""):
        nb1 = float(nb1)
        if (op==1):
            result = round(nb2 + nb1,10)
        if (op==2):
            result = round(nb2 - nb1,10)
        if (op==3):
            result = round(nb2 * nb1,10)
        if (op==4):
            result = round(nb2 / nb1,10)
        label["text"] = result
        nb1 = str(result)
        result = 0

def changesign():
    global nb1
    if(nb1<0):
        nb1 = nb1
    else:
        nb1 = -nb1
    label["text"] = nb1

mainLabel = Label(fenetre,text="")
mainLabel.place(x=10,y=10)
label = Label(fenetre,text="0")
label.place(x=10,y=40)

button1 = Button(fenetre,text=" 1  ",command=num1,height = 1, width = 3)
button1.place(x=10,y=110)
button2 = Button(fenetre,text=" 2  ",command=num2,height = 1, width = 3)
button2.place(x=70,y=110)
button3 = Button(fenetre,text=" 3  ",command=num3,height = 1, width = 3)
button3.place(x=130,y=110)
button4 = Button(fenetre,text=" 4  ",command=num4,height = 1, width = 3)
button4.place(x=10,y=150)
button5 = Button(fenetre,text=" 5  ",command=num5,height = 1, width = 3)
button5.place(x=70,y=150)
button6 = Button(fenetre,text=" 6  ",command=num6,height = 1, width = 3)
button6.place(x=130,y=150)
button7 = Button(fenetre,text=" 7  ",command=num7,height = 1, width = 3)
button7.place(x=10,y=190)
button8 = Button(fenetre,text=" 8  ",command=num8,height = 1, width = 3)
button8.place(x=70,y=190)
button9 = Button(fenetre,text=" 9  ",command=num9,height = 1, width = 3)
button9.place(x=130,y=190)
button0 = Button(fenetre,text=" 0  ",command=num0,height = 1, width = 3)
button0.place(x=70,y=230)
buttonPoint = Button(fenetre,text=" .  ",command=point,height = 1, width = 3)
buttonPoint.place(x=130,y=230)

buttonCE = Button(fenetre,text="CE",command=clearCurrentnb,height = 1, width = 3)
buttonCE.place(x=10,y=70)
buttonC = Button(fenetre,text=" C  ",command=clear,height = 1, width = 3)
buttonC.place(x=70,y=70)
buttonBack = Button(fenetre,text=" <- ",command=clear,height = 1, width = 3)
buttonBack.place(x=130,y=70)
buttonAdd = Button(fenetre,text=" + ",command=add,height = 1, width = 3)
buttonAdd.place(x=190,y=190)
buttonDif = Button(fenetre,text=" - ",command=dif,height = 1, width = 3)
buttonDif.place(x=190,y=150)
buttonMul = Button(fenetre,text=" * ",command=mult,height = 1, width = 3)
buttonMul.place(x=190,y=110)
buttonDiv = Button(fenetre,text=" / ",command=div,height = 1, width = 3)
buttonDiv.place(x=190,y=70)
buttonEgal = Button(fenetre,text=" = ",command=egal,height = 1, width = 3)
buttonEgal.place(x=190,y=230)
buttonSign = Button(fenetre,text=" +/- ",command=changesign,height = 1, width = 3)
buttonSign.place(x=10,y=230)
#label = Label (fenetre, text="Hello World")
#label.pack()

fenetre.mainloop()