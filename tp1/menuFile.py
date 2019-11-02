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
        try:
            textadded = input("Entrer le texte à ajouter : ")
            with open(file,'a') as fic:
                fic.write(textadded+"\n")
        except:
            print("Une erreur est survenue lors de l'écriture du texte.\n")
        else:
            print("L'ajout du texte a été effectué  avec succès.\n")
        finally:
            fic.close()
    elif choice == "3":
        try:
            with open(file,'r') as fic:
                print(fic.read())
        except:
            print("Une erreur est survenue lors de la lecture du fichier.\n")
        finally:
            fic.close()
    elif choice == "4":
        try:
            fic = open(file,'wt')
            fic.flush()
        except:
            print("Le fichier n'a pas pu être vidé.\n")
        else:
            print("Le fichier a été vidé avec succès.\n")
        finally:
            fic.close()
    else:
        request = False

