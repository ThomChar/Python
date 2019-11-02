from tkinter import *
from password import *

def register() :
    main = Toplevel()
    main.grab_set()
    main.title('Register Box')
    main.geometry('200x200')
    
    def clear_widget(event):
    
        # will clear out any entry boxes defined below when the user shifts
        # focus to the widgets defined below
        if username_box == main.focus_get() and username_box.get() == PSEUDO_DEFAULT_INPUT:
            username_box.delete(0, END)
        elif password_box == password_box.focus_get() and password_box.get() == '     ':
            password_box.delete(0, END)
    
    def repopulate_defaults(event):
    
        # will repopulate the default text previously inside the entry boxes defined below if
        # the user does not put anything in while focused and changes focus to another widget
        if username_box != main.focus_get() and username_box.get() == '':
            username_box.insert(0, PSEUDO_DEFAULT_INPUT)
        elif password_box != main.focus_get() and password_box.get() == '':
            password_box.insert(0, '     ')
    
    def cancel(*event) :
        main.destroy()

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
                save_register(login, hash(password))
                print("Writing complete")
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

    def signUp(*event):
    
        # Able to be called from a key binding or a button click because of the '*event'
        print ('Username: ' + username_box.get())
        print ('Password: ' + password_box.get())
        main.destroy()
        # If I wanted I could also pass the username and password I got above to another 
        # function from here.
    
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

   