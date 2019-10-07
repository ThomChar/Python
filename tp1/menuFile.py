# 1. Choisir nom d'un fichier
# 2. Ajouter du texte
# 3. Afficher le fichier complet
# 4. Vider le fichier
# 5. Quitter le programme
file = input("Choisir un nom de fichier pour commencer : ")
request = True
while request:
    choice = input("Chosir une opition parmi les suivantes :\n"
    "1. Choisir nom d'un fichier \n"
    "2. Ajouter du texte \n"
    "3. Afficher le fichier complet \n"
    "4. Vider le fichier \n"
    "5. Quitter le programme \n" 
    )

    if choice == "1":
        file = input("Choisir un nom de fichier : ")
    elif choice == "2":
        textadded = input("Entrer le texte à ajouter : ")
        with open(file,'a') as fic:
            fic.write(textadded+"\n")
        fic.close()
    elif choice == "3":
        with open(file,'r') as fic:
            print(fic.read())
        fic.close()
    elif choice == "4":
        fic = open(file,'wt')
        fic.flush()
        fic.close()
    else:
        request = False

