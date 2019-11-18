from tkinter import *
from password import *

def register() :
    main = Toplevel()
    main.grab_set()
    main.title('Register Box')
    main.geometry('200x200')
    
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
    
    # cancel : close register windows
    def cancel(*event) :
        main.destroy()

    # register : Event to register
    def register() :
        login = username_box.get()
        password = password_box.get()

        try:
            # verif login
            shortLogin = login.replace(' ',"")
            if login == PSEUDO_DEFAULT_INPUT or shortLogin == "":
                print("Pseudo invalide")
                raise ValueError("Pseudo invalide", "Vous devez entrer un login !")
            
            # verif password
            shortPassword = password.replace(' ',"")
            if len(shortPassword) < 4:
                print("Mot de passe invalide")
                raise ValueError("Mot de passe invalide", "Le mot de passe doit contenir au moins 4 caractères !")
            
            # verif if login is available
            if(pseudoIsExiste(login) == False) :
                save_register(login, hash_password(password))
                print("Writing complete")
                main.destroy()
            else:
                print("Le pseudo existe déjà.")
                messagebox.showerror("Pseudo déjà existant", "Le pseudo existe déjà : \""+login+"\".")   
        except ValueError as error:
            print(error)
            messagebox.showerror(error.args[0], error.args[1])

    def save_register(login, hashpassword) :
        with open(PSEUDOS_FILE, mode='a') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=';', lineterminator="\n")
            employee_writer.writerow([login, hashpassword])
    
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
    password_box.bind('<Return>', register)
    password_box.grid(row=2, column=5, sticky='NS')
    
    # adds register button and defines its properties
    register_btn = Button(main, text='Register', command=register)
    register_btn.bind('<Return>', register)
    register_btn.grid(row=6, column=5, sticky='NESW')

    # cancel
    cancel_btn = Button(main, text='Cancel', command=cancel)
    cancel_btn.bind('<Return>', cancel)
    cancel_btn.grid(row=6, column=6, sticky='NESW')

    main.mainloop()

   