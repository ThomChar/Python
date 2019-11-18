#!/usr/bin/python
  
from tkinter import *
from register import *
from password import *

main = Tk()
main.title('Authentication Box')
main.geometry('300x200')
 

# clear_widget : Clear values in username_box and in password_box
def clear_widget(event):
    if username_box == main.focus_get() and username_box.get() == PSEUDO_DEFAULT_INPUT:
        username_box.delete(0, END)
    elif password_box == password_box.focus_get() and password_box.get() == '     ':
        password_box.delete(0, END)
 
# repopulate_defaults : Put values of defaults in username_box and in password_box
def repopulate_defaults(event):
    if username_box != main.focus_get() and username_box.get() == '':
        username_box.insert(0, PSEUDO_DEFAULT_INPUT)
    elif password_box != main.focus_get() and password_box.get() == '':
        password_box.insert(0, '     ')
 
# login : Event of login
def login(*event):
    login = username_box.get()
    password = password_box.get()

    try:
        #verif login && password
        if(pseudoIsExiste(login) == False) :
            raise ValueError("Identifiant incorrecte", "L'identifiant est incorrecte.")

        passwordOfPseudo = getPasswordByPseudo(login)
        if(verify_password(passwordOfPseudo, password) == False) :
            raise ValueError("Identifiant incorrecte", "Le mot de passe est incorrecte.")

        print("Vous êtes connectés !")
    except ValueError as error:
        print(error)
        messagebox.showerror(error.args[0], error.args[1])

    #main.destroy()

#reader()
# defines a grid 50 x 50 cells in the main window
rows = 0
while rows < 10:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1
 
 
# adds username entry widget and defines its properties
username_box = Entry(main)
username_box.insert(0, 'Enter Username')
username_box.bind("<FocusIn>", clear_widget)
username_box.bind('<FocusOut>', repopulate_defaults)
username_box.grid(row=1, column=5, sticky='NS')
 
 
# adds password entry widget and defines its properties
password_box = Entry(main, show='*')
password_box.insert(0, '     ')
password_box.bind("<FocusIn>", clear_widget)
password_box.bind('<FocusOut>', repopulate_defaults)
password_box.bind('<Return>', login)
password_box.grid(row=2, column=5, sticky='NS')
 
 
# adds login button and defines its properties
login_btn = Button(main, text='Login', command=login)
login_btn.bind('<Return>', login)
login_btn.grid(row=5, column=5, sticky='NESW')
 
 # adds register button and defines its properties
register_btn = Button(main, text='Register', command=register)
register_btn.bind('<Return>', register)
register_btn.grid(row=6, column=5, sticky='NESW')


main.mainloop()
