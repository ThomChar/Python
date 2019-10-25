# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *
from tkinter import messagebox
from math import *
from chaine import *
import tkinter.font as subFont

def CreateCommonMenubar(gui):
    #Add a menu bar
	menubar = Menu(gui)

	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Aide",command= lambda:messageAideGeneral(" "))
	menu1.add_separator()
	menu1.add_command(label="Quitter", command=gui.quit)
	menubar.add_cascade(label="Menu", menu=menu1)

	gui.config(menu=menubar)

def messageAideGeneral(text):
    messagebox.showinfo("Aide",text)

def messageAlert(text):
    messagebox.showinfo("Alerte", text)

def registerParamMarkov1():
    toplevel = Toplevel()

    # set the background colour of GUI window 
    toplevel.configure(background="white") 
    # set the title of GUI window 
    toplevel.title("M/M/1")
    toplevel.geometry("290x270")
    toplevel.resizable(0,0)
    policeTitle = subFont.Font(family='Helvetica', size=14, weight='normal')

    CreateCommonMenubar(toplevel)

    rows = 0
    while rows < 4:
        toplevel.rowconfigure(rows,weight=1)
        toplevel.columnconfigure(rows,weight=1)
        rows +=1

    Label(toplevel, font=policeTitle, text='M/M/1',background="white").grid(columnspan=3, ipadx=110)
    Label(toplevel, text='Nbre Moy. clients (Lambda)',background="white").grid(row=1, column=0)   
    lambda_field = Entry(toplevel, justify="right")
    lambda_field.grid(row=1, column=1)
    Label(toplevel, text='Service en moyenne (Mu)',background="white").grid(row=2, column=0)   
    mu_field = Entry(toplevel, justify="right")
    mu_field.grid(row=2, column=1)

    Label(toplevel, text='',background="white").grid(row=3, column=0)

    button1 = Button(toplevel, command= lambda : registerMarkov1(lambda_field.get(),mu_field.get()), text=' Continuer ', fg='black', bg='white', height=2, width=7)
    button1.place(x=60,y=210)
    button2 = Button(toplevel, command= toplevel.destroy, text=' Annuler ', fg='black', bg='white', height=2, width=7)
    button2.place(x=170,y=210)

    toplevel.grab_set()

def registerParamMarkov1K():
    
    toplevel = Toplevel()
    # set the background colour of GUI window 
    toplevel.configure(background="white") 
    # set the title of GUI window 
    toplevel.title("M/M/S")
    toplevel.geometry("290x330")
    toplevel.resizable(0,0)
    policeTitle = subFont.Font(family='Helvetica', size=14, weight='normal')

    CreateCommonMenubar(toplevel)

    rows = 0
    while rows < 5:
        toplevel.rowconfigure(rows,weight=1)
        toplevel.columnconfigure(rows,weight=1)
        rows +=1

    Label(toplevel, font=policeTitle, text='M/M/S',background="white").grid(columnspan=3, ipadx=110)
    Label(toplevel, text='Nbre Moy. clients (Lambda)',background="white").grid(row=1, column=0)   
    lambda_field = Entry(toplevel, justify="right")
    lambda_field.grid(row=1, column=1)
    Label(toplevel, text='Service en moyenne (Mu)',background="white").grid(row=2, column=0)   
    mu_field = Entry(toplevel, justify="right")
    mu_field.grid(row=2, column=1)
    Label(toplevel, text='Borne Sup Nb clients (K)',background="white").grid(row=3, column=0)   
    k_field = Entry(toplevel, justify="right")
    k_field.grid(row=3, column=1)

    Label(toplevel, text='',background="white").grid(row=4, column=0)

    button1 = Button(toplevel, command= lambda : registerMarkov1K(lambda_field.get(),mu_field.get(), k_field.get()), text=' Continuer ', fg='black', bg='white', height=2, width=7)
    button1.place(x=60,y=270)
    button2 = Button(toplevel, command= toplevel.destroy, text=' Annuler ', fg='black', bg='white', height=2, width=7)
    button2.place(x=170,y=270)

    toplevel.grab_set()

def registerParamMarkovS():
    toplevel = Toplevel()
    # set the background colour of GUI window 
    toplevel.configure(background="white") 
    # set the title of GUI window 
    toplevel.title("M/M/S")
    toplevel.geometry("290x330")
    toplevel.resizable(0,0)
    policeTitle = subFont.Font(family='Helvetica', size=14, weight='normal')

    CreateCommonMenubar(toplevel)

    rows = 0
    while rows < 5:
        toplevel.rowconfigure(rows,weight=1)
        toplevel.columnconfigure(rows,weight=1)
        rows +=1

    Label(toplevel, font=policeTitle, text='M/M/S',background="white").grid(columnspan=3, ipadx=110)
    Label(toplevel, text='Nbre Moy. clients (Lambda)',background="white").grid(row=1, column=0)   
    lambda_field = Entry(toplevel, justify="right")
    lambda_field.grid(row=1, column=1)
    Label(toplevel, text='Service en moyenne (Mu)',background="white").grid(row=2, column=0)   
    mu_field = Entry(toplevel, justify="right")
    mu_field.grid(row=2, column=1)
    Label(toplevel, text='Nombre de Service (S)',background="white").grid(row=3, column=0)   
    s_field = Entry(toplevel, justify="right")
    s_field.grid(row=3, column=1)

    Label(toplevel, text='',background="white").grid(row=4, column=0)

    button1 = Button(toplevel, command= lambda : registerMarkovS(lambda_field.get(),mu_field.get(), s_field.get()), text=' Continuer ', fg='black', bg='white', height=2, width=7)
    button1.place(x=60,y=270)
    button2 = Button(toplevel, command= toplevel.destroy, text=' Annuler ', fg='black', bg='white', height=2, width=7)
    button2.place(x=170,y=270)

    toplevel.grab_set()


def nbClientsFileWindow(j,lamb,mu):
    try:
        jcontrol=float(j)
        if(j>=0):
            chaine=Markov1(lamb,mu)
            qj=chaine.__jClientFile__(jcontrol)
            
            toplevel = Toplevel()
            CreateCommonMenubar(toplevel)
            toplevel.resizable(0,0)
            toplevel.title("Qj")
            Label(toplevel, text='Pour j = '+j+', Qj =').grid(row=1, column=0)
            Label(toplevel, text=qj).grid(row=1, column=1)
            toplevel.grab_set()
        else:
            messageAlert('Erreur, veuillez entrer un entier positif.')
    except ValueError:
        #Handle the exception
        messageAlert('Erreur, veuillez entrer une valeur numérique pour j.')

def tempsSejourSystemWindow(t,lamb,mu):
    try:
        if(t>=0):
            tcontrol=int(t)
            chaine=Markov1(lamb,mu)
            ResTempsSejourSystem = chaine.__tempsSejourSysteme__(tcontrol)

            toplevel = Toplevel()
            CreateCommonMenubar(toplevel)
            toplevel.resizable(0,0)
            toplevel.title("P(Tau > t)")
            Label(toplevel, text='P(Tau > t) = ').grid(row=0, column=0)
            Label(toplevel, text=ResTempsSejourSystem).grid(row=0, column=1)
            toplevel.grab_set()
        else:
            messageAlert('Erreur, veuillez entrer un entier positif.')
    except ValueError:
        #Handle the exception
        messageAlert('Erreur, veuillez entrer un entier pour t.')

    
def nbClientsFileWindow1K(j,lamb,mu,k):
    try:
        if(j>=0):
            jcontrol=float(j)
            chaine=Markov1K(lamb,mu,k)
            qj=chaine.__jClientFile__(jcontrol)
            
            toplevel = Toplevel()
            CreateCommonMenubar(toplevel)
            toplevel.resizable(0,0)
            toplevel.title("Qj")
            Label(toplevel, text='Pour j = '+j+', Qj =').grid(row=1, column=0)
            Label(toplevel, text=qj).grid(row=1, column=1)
            toplevel.grab_set()
        else:
            messageAlert('Erreur, veuillez entrer un entier positif.')
    except ValueError:
        #Handle the exception
        messageAlert('Erreur, veuillez entrer une valeur numérique pour j.')

def tempsSejourSystemWindow1K(t,lamb,mu,k):
    try:
        if(t>=0):
            tcontrol=int(t)
            chaine=Markov1K(lamb,mu,k)
            ResTempsSejourSystem = chaine.__tempsSejourSysteme__(tcontrol)

            toplevel = Toplevel()
            CreateCommonMenubar(toplevel)
            toplevel.resizable(0,0)
            toplevel.title("P(Tau > t)")
            Label(toplevel, text='P(Tau > t) = ').grid(row=0, column=0)
            Label(toplevel, text=ResTempsSejourSystem).grid(row=0, column=1)
            toplevel.grab_set()
        else:
            messageAlert('Erreur, veuillez entrer un entier positif.')
    except ValueError:
        #Handle the exception
        messageAlert('Erreur, veuillez entrer un entier pour t.')

def nbClientsFileWindowS(j,lamb,mu,s):
    try:
        if(j>=0):
            jcontrol=float(j)
            chaine=MarkovS(lamb,mu,s)
            qj=chaine.__jClientFile__(jcontrol)
            
            toplevel = Toplevel()
            CreateCommonMenubar(toplevel)
            toplevel.resizable(0,0)
            toplevel.title("Qj")
            Label(toplevel, text='Pour j = '+j+', Qj =').grid(row=1, column=0)
            Label(toplevel, text=qj).grid(row=1, column=1)
            toplevel.grab_set()
        else:
            messageAlert('Erreur, veuillez entrer un entier positif.')
    except ValueError:
        #Handle the exception
        messageAlert('Erreur, veuillez entrer une valeur numérique pour j.')

def tempsSejourSystemWindowS(t,lamb,mu,s):
    try:
        if(t>=0):
            tcontrol=int(t)
            chaine=MarkovS(lamb,mu,s)
            ResTempsSejourSystem = chaine.__tempsSejourSysteme__(tcontrol)

            toplevel = Toplevel()
            CreateCommonMenubar(toplevel)
            toplevel.resizable(0,0)
            toplevel.title("P(Tau > t)")
            Label(toplevel, text='P(Tau > t) = ').grid(row=0, column=0)
            Label(toplevel, text=ResTempsSejourSystem).grid(row=0, column=1)
            toplevel.grab_set()
        else:
            messageAlert('Erreur, veuillez entrer un entier positif.')
    except ValueError:
        #Handle the exception
        messageAlert('Erreur, veuillez entrer un entier pour t.')

def DureeAttenteSansServiceS(t,lamb,mu,s):
    try:
        if(t>=0):
            tcontrol=int(t)
            chaine=MarkovS(lamb,mu,s)
            ResDureeAttenteSansService = chaine.__DureeAttenteSansService__(tcontrol)

            toplevel = Toplevel()
            CreateCommonMenubar(toplevel)
            toplevel.resizable(0,0)
            toplevel.title("P(TauQ > t)")
            Label(toplevel, text='P(TauQ > t) = ').grid(row=0, column=0)
            Label(toplevel, text=ResDureeAttenteSansService).grid(row=0, column=1)
            toplevel.grab_set()
        else:
            messageAlert('Erreur, veuillez entrer un entier positif.')
    except ValueError:
        #Handle the exception
        messageAlert('Erreur, veuillez entrer un entier pour t.')

# Driver code 
def registerMarkov1(lamb,mu):
    try:
        i=float(lamb)
        j=float(mu)
        
        if(i>=j):
            raise ValueError('Erreur','Attention, la condition lambda < mu (rho < 1) doit être satisfaite pour continuer.')
        if(i<0 or j<0):
            raise ValueError('Erreur','Attention, la condition lambda et mu >0 doit être satisfaite pour continuer.')

            toplevel = Tk() 
            CreateCommonMenubar(toplevel)
            toplevel.title("M/M/1 Résaultats")
            # set the background colour of GUI window 
            toplevel.configure(background="white") 
            w =  toplevel.winfo_screenwidth()/2+250
            h =  toplevel.winfo_screenheight()/2-350
            toplevel.geometry("390x315+"+str(int(w))+"+"+str(int(h))) 
            toplevel.resizable(0,0)
            policeTitle = subFont.Font(family='Helvetica', size=14, weight='normal')

            rows = 0
            while rows < 12:
                toplevel.rowconfigure(rows,weight=1)
                toplevel.columnconfigure(rows,weight=1)
                rows +=1

            chaine = Markov1(i,j)

            Label(toplevel, font=policeTitle, text='Résultats M/M/1',background="white").grid(columnspan=4, ipadx=110)
            
            #Lambda
            Label(toplevel, text='Lambda',background="white").grid(row=1, column=0)   
            Label(toplevel, text=i,background="white").grid(row=1, column=1)
            #Mu
            Label(toplevel, text='Mu',background="white").grid(row=1, column=2)   
            Label(toplevel, text=j,background="white").grid(row=1, column=3)
            #Calcul de Rho
            Label(toplevel, text='Rho',background="white").grid(row=2, column=0)   
            Label(toplevel, text=str(chaine.rho),background="white").grid(row=2, column=1)
            #Calcul de la duree moyenne de service
            Label(toplevel, text='Temps service',background="white").grid(row=2, column=2)   
            Label(toplevel, text='    '+str(chaine.tmpsServ),background="white").grid(row=2, column=3)
            #Nombre moyen de clients dans le système
            Label(toplevel, text='L',background="white").grid(row=3, column=0)   
            Label(toplevel, text=str(chaine.L),background="white").grid(row=3, column=1)
            #Nombre moyen de clients dans la file
            Label(toplevel, text='Lq',background="white").grid(row=3, column=2)   
            Label(toplevel, text='    '+str(chaine.Lq),background="white").grid(row=3, column=3)
            #Duree moyenne d'attente dans le système
            Label(toplevel, text='w',background="white").grid(row=4, column=0)   
            Label(toplevel, text=str(chaine.w),background="white").grid(row=4, column=1)
            #Duree moyenne d'attente dans la file
            Label(toplevel, text='wq',background="white").grid(row=4, column=2)   
            Label(toplevel, text='    '+str(chaine.wq),background="white").grid(row=4, column=3)
            #Calcul aucun clients dans la file_
            Label(toplevel, text='q0',background="white").grid(row=5, column=0)   
            Label(toplevel, text=str(chaine.q0),background="white").grid(row=5, column=1)
            #Calcul de j clients dans la file
            Label(toplevel, text='j =',background="white").grid(row=6, column=0)   
            QJ_field = Entry(toplevel, justify="right")
            QJ_field.grid(row=6, column=1)
            buttonQJ = Button(toplevel, command= lambda : nbClientsFileWindow(QJ_field.get(),chaine.lamb,chaine.mu), text='Calculer qj', fg='black', bg='white', height=1, width=10)
            buttonQJ.grid(row=6, column=2)
            #Temps de séjour dans le système
            Label(toplevel, text='t =',background="white").grid(row=7, column=0)   
            TmpsSej_field = Entry(toplevel, justify="right")
            TmpsSej_field.grid(row=7, column=1)
            buttonTmpsSej = Button(toplevel, command= lambda :tempsSejourSystemWindow(TmpsSej_field.get(),chaine.lamb,chaine.mu), text='P(Tau > t)', fg='black', bg='white', height=1, width=10)
            buttonTmpsSej.grid(row=7, column=2)
            

            Label(toplevel, text='',background="white").grid(row=8, column=0)

            button1 = Button(toplevel, command= toplevel.destroy, text=' Fermer ', fg='black', bg='white', height=1, width=15)
            button1.place(x=255,y=275)

    except ValueError as error:
        #Handle the exception
        if(error):
            messagebox.showerror(error.args[0], error.args[1])
        else :
            messageAlert('Erreur, veuillez entrer des valeurs numériques pour lambda et mu.')


def registerMarkov1K(lamb,mu,k):
    try:
        i=float(lamb)
        j=float(mu)
        K=int(k)
        toplevel = Tk() 
        CreateCommonMenubar(toplevel)
        toplevel.title("M/M/1/K Résaultats")
        # set the background colour of GUI window 
        toplevel.configure(background="white") 
        w =  toplevel.winfo_screenwidth()/2+250
        h =  toplevel.winfo_screenheight()/2-350
        toplevel.geometry("390x385+"+str(int(w))+"+"+str(int(h))) 
        toplevel.resizable(0,0)
        policeTitle = subFont.Font(family='Helvetica', size=14, weight='normal')

        rows = 0
        while rows < 13:
            toplevel.rowconfigure(rows,weight=1)
            toplevel.columnconfigure(rows,weight=1)
            rows +=1

        chaine = Markov1K(i,j,K)

        Label(toplevel, font=policeTitle, text='Résultats M/M/1/K',background="white").grid(columnspan=4, ipadx=110)
        
        #Lambda
        Label(toplevel, text='Lambda',background="white").grid(row=1, column=0)   
        Label(toplevel, text=i,background="white").grid(row=1, column=1)
        #Mu
        Label(toplevel, text='Mu',background="white").grid(row=1, column=2)   
        Label(toplevel, text=j,background="white").grid(row=1, column=3)
        #K
        Label(toplevel, text='K',background="white").grid(row=2, column=0)   
        Label(toplevel, text=K,background="white").grid(row=2, column=1)
        #Calcul de Rho
        Label(toplevel, text='Rho',background="white").grid(row=3, column=0)   
        Label(toplevel, text=str(chaine.rho),background="white").grid(row=3, column=1)
        #Calcul de la duree moyenne de service
        Label(toplevel, text='Temps service',background="white").grid(row=3, column=2)   
        Label(toplevel, text='    '+str(chaine.tmpsServ),background="white").grid(row=3, column=3)
        #Nombre moyen de clients dans le système
        Label(toplevel, text='L',background="white").grid(row=4, column=0)   
        Label(toplevel, text=str(chaine.__nbreMoyClientSysteme__()),background="white").grid(row=4, column=1)
        #Nombre moyen de clients dans la file
        Label(toplevel, text='Lq',background="white").grid(row=4, column=2)   
        Label(toplevel, text='    '+str(chaine.Lq),background="white").grid(row=4, column=3)
        #Duree moyenne d'attente dans le système
        Label(toplevel, text='w',background="white").grid(row=5, column=0)   
        Label(toplevel, text=str(chaine.w),background="white").grid(row=5, column=1)
        #Duree moyenne d'attente dans la file
        Label(toplevel, text='wq',background="white").grid(row=5, column=2)   
        Label(toplevel, text='    '+str(chaine.wq),background="white").grid(row=5, column=3)
        #Calcul aucun clients dans la file_
        Label(toplevel, text='q0',background="white").grid(row=6, column=0)   
        Label(toplevel, text=str(chaine.__jClientFile__(0)),background="white").grid(row=6, column=1)
        #Calcul de j clients dans la file
        Label(toplevel, text='j =',background="white").grid(row=7, column=0)   
        QJ_field = Entry(toplevel, justify="right")
        QJ_field.grid(row=7, column=1)
        buttonQJ = Button(toplevel, command= lambda : nbClientsFileWindow1K(QJ_field.get(),chaine.lamb,chaine.mu,chaine.K), text='Calculer qj', fg='black', bg='white', height=1, width=10)
        buttonQJ.grid(row=7, column=2)
        #Temps de séjour dans le système
        Label(toplevel, text='t =',background="white").grid(row=8, column=0)   
        TmpsSej_field = Entry(toplevel, justify="right")
        TmpsSej_field.grid(row=8, column=1)
        buttonTmpsSej = Button(toplevel, command= lambda :tempsSejourSystemWindow1K(TmpsSej_field.get(),chaine.lamb,chaine.mu,chaine.K), text='P(Tau > t)', fg='black', bg='white', height=1, width=10)
        buttonTmpsSej.grid(row=8, column=2)
        

        Label(toplevel, text='',background="white").grid(row=9, column=0)

        button1 = Button(toplevel, command= toplevel.destroy, text=' Fermer ', fg='black', bg='white', height=1, width=15)
        button1.place(x=255,y=345)

    except ValueError:
        #Handle the exception
        messageAlert('Erreur, veuillez entrer des valeurs numériques pour lambda, mu et K, \noù K doit être un entier')


def registerMarkovS(lamb,mu,s):
    try:
        i=float(lamb)
        j=float(mu)
        S=int(s)
        if(S>1):
            toplevel = Tk() 
            CreateCommonMenubar(toplevel)
            toplevel.title("M/M/S Résaultats")
            # set the background colour of GUI window 
            toplevel.configure(background="white") 
            w =  toplevel.winfo_screenwidth()/2+250
            h =  toplevel.winfo_screenheight()/2-350
            toplevel.geometry("390x385+"+str(int(w))+"+"+str(int(h))) 
            toplevel.resizable(0,0)
            policeTitle = subFont.Font(family='Helvetica', size=14, weight='normal')

            rows = 0
            while rows < 14:
                toplevel.rowconfigure(rows,weight=1)
                toplevel.columnconfigure(rows,weight=1)
                rows +=1

            chaine = MarkovS(i,j,S)

            Label(toplevel, font=policeTitle, text='Résultats M/M/S',background="white").grid(columnspan=4, ipadx=110)
            
            #Lambda
            Label(toplevel, text='Lambda',background="white").grid(row=1, column=0)   
            Label(toplevel, text=i,background="white").grid(row=1, column=1)
            #Mu
            Label(toplevel, text='Mu',background="white").grid(row=1, column=2)   
            Label(toplevel, text=j,background="white").grid(row=1, column=3)
            #S
            Label(toplevel, text='S',background="white").grid(row=2, column=0)   
            Label(toplevel, text=S,background="white").grid(row=2, column=1)
            #Calcul de Rho
            Label(toplevel, text='Rho',background="white").grid(row=3, column=0)   
            Label(toplevel, text=str(chaine.rho),background="white").grid(row=3, column=1)
            #Calcul de la duree moyenne de service
            Label(toplevel, text='Temps service',background="white").grid(row=3, column=2)   
            Label(toplevel, text='    '+str(chaine.tmpsServ),background="white").grid(row=3, column=3)
            #Nombre moyen de clients dans le système
            Label(toplevel, text='L',background="white").grid(row=4, column=0)   
            Label(toplevel, text=str(chaine.L),background="white").grid(row=4, column=1)
            #Nombre moyen de clients dans la file
            Label(toplevel, text='Lq',background="white").grid(row=4, column=2)   
            Label(toplevel, text='    '+str(chaine.Lq),background="white").grid(row=4, column=3)
            #Duree moyenne d'attente dans le système
            Label(toplevel, text='w',background="white").grid(row=5, column=0)   
            Label(toplevel, text=str(chaine.w),background="white").grid(row=5, column=1)
            #Duree moyenne d'attente dans la file
            Label(toplevel, text='wq',background="white").grid(row=5, column=2)   
            Label(toplevel, text='    '+str(chaine.wq),background="white").grid(row=5, column=3)
            #Calcul aucun clients dans la file_
            Label(toplevel, text='q0',background="white").grid(row=6, column=0)   
            Label(toplevel, text=str(chaine.q0),background="white").grid(row=6, column=1)
            #Calcul de j clients dans la file
            Label(toplevel, text='j =',background="white").grid(row=7, column=0)   
            QJ_field = Entry(toplevel, justify="right")
            QJ_field.grid(row=7, column=1)
            buttonQJ = Button(toplevel, command= lambda : nbClientsFileWindowS(QJ_field.get(),chaine.lamb,chaine.mu,chaine.S), text='Calculer qj', fg='black', bg='white', height=1, width=10)
            buttonQJ.grid(row=7, column=2)
            #Temps de séjour dans le système
            Label(toplevel, text='t =',background="white").grid(row=8, column=0)   
            TmpsSej_field = Entry(toplevel, justify="right")
            TmpsSej_field.grid(row=8, column=1)
            buttonTmpsSej = Button(toplevel, command= lambda :tempsSejourSystemWindowS(TmpsSej_field.get(),chaine.lamb,chaine.mu,chaine.S), text='P(Tau > t)', fg='black', bg='white', height=1, width=10)
            buttonTmpsSej.grid(row=8, column=2)
            #DureeAttenteSansService
            Label(toplevel, text='t =',background="white").grid(row=9, column=0)   
            TmpsSej_field = Entry(toplevel, justify="right")
            TmpsSej_field.grid(row=9, column=1)
            buttonTmpsSej = Button(toplevel, command= lambda :DureeAttenteSansServiceS(TmpsSej_field.get(),chaine.lamb,chaine.mu,chaine.S), text='P(Tauq > t)', fg='black', bg='white', height=1, width=10)
            buttonTmpsSej.grid(row=9, column=2)
            

            Label(toplevel, text='',background="white").grid(row=10, column=0)

            button1 = Button(toplevel, command= toplevel.destroy, text=' Fermer ', fg='black', bg='white', height=1, width=15)
            button1.place(x=255,y=345)

        else :
            messageAlert('Attention, la condition S > 1 doit être satisfaite pour continuer.')
    except ValueError:
        #Handle the exception
        messageAlert('Erreur, veuillez entrer des valeurs numériques pour lambda, mu et S, \noù S doit être un entier')

