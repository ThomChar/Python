import sqlite3
import csv


# Create a database in RAM
db = sqlite3.connect('mydbCommune.db')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('mydbCommune.db')

####################################################"POP TABLE REGION"###############################################


def Pop():
    cursor = db.cursor()
    print("\nInsertion Régions : \n")
    with open('csv_files/regions.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        error = 0
        # Skip the first lines
        for i in range(0,8):
            next(spamreader)

        for row in spamreader:
            try:
            # Si le code région est null, on considère que la ligne n'est pas valide pour insertion
                if(row[0]!=""):
                    cursor.execute('''INSERT INTO region(code_region, nom_region)
                        VALUES(?,?)''', (row[0], row[1]))
            except:
                error = error + 1
                print(str(row[0])+' : '+ str(row[1])+' -> insertion impossible car la clé code_région existe déjà')
            
        print("\nNombre d'erreurs rencontrées lors de l'insertion de région : "+ str(error)+"\n")
    #db.commit()


    ####################################################"POP TABLE DEPARTEMENT"###############################################

    print("\nInsertion Départements : \n")
    cursor = db.cursor()
    with open('csv_files/departements.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        error = 0
        # Skip the first lines
        for i in range(0,8):
            next(spamreader)

        for row in spamreader:
            try:
            # Si le code département est null, on considère que la ligne n'est pas valide pour insertion
                if(row[2]!=""):
                    cursor.execute('''INSERT INTO departement(code_departement, nom_departement, code_region, code_nouvelle_region)
                        VALUES(?,?,?,?)''', (row[2], row[3], row[0], 0))
            except:
                error = error + 1
                print(str(row[2])+' : '+ str(row[3])+' , Région : '+ str(row[0])+ '-> insertion impossible car la clé code_département existe déjà')
            
        print("\nNombre d'erreurs rencontrées lors de l'insertion de départements : "+ str(error)+"\n")
    #db.commit()

    db.commit()


    ####################################################"POP TABLE COMMUNE"###############################################

    print("\nInsertion Communes : \n")
    cursor = db.cursor()
    with open('csv_files/communes.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        error = 0
        # Skip the first lines
        for i in range(0,8):
            next(spamreader)

        for row in spamreader:
            try:
            # Si le code commune est null, on considère que la ligne n'est pas valide pour insertion
                if(row[5]!=""):
                    popInt = row[9].replace(' ','')
                    cursor.execute('''INSERT INTO commune(nom_commune,code_commune , population_totale,code_departement)
                        VALUES(?,?,?,?)''', (row[6], row[5], popInt, row[2]))
            except:
                error = error + 1
                print(str(row[5])+' : '+ str(row[6])+' , '+ popInt +' habitants, Département : '+ str(row[2])+ '-> insertion impossible car la clé code_département existe déjà')
            
        print("\nNombre d'erreurs rencontrées lors de l'insertion de communes : "+ str(error)+"\n")
    db.commit()



####################################################"POP TABLE NOUVELLE REGION"###############################################
def PopNouvellesRegions():

    # Ajout des nouvelles regions dans la table Nouvelles régions à partir de la fin du document zones-2016.csv
    cursor = db.cursor()
    print("\nInsertion Nouvelles Régions : \n")
    with open('csv_files/zones-2016.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        error = 0

        # Skip the first lines
        for i in range(0,8):
            next(spamreader)

        for row in spamreader:
            try:
                #Saute des lignes dans le doc jusqu'à la ligne correspondat aux regions
                if (row[0]=="REG"):
                    #Si le code région est null, on considère que la ligne n'est pas valide pour insertion
                    if(row[1]!=""):
                        cursor.execute('''INSERT INTO nouvelleRegion(code_region, nom_region,nb_com)
                            VALUES(?,?,?)''', (row[1], row[2],row[3]))
            except:
                error = error + 1
                print(str(row[1])+' : '+ str(row[2])+' nombre communes '+ str(row[3])+' -> insertion impossible car la clé code_région existe déjà')
            
        print("\nNombre d'erreurs rencontrées lors de l'insertion de nouvelle région : "+ str(error)+"\n")
    
    
    # Ajout des liens entre départements et nouvelles régions à partir du document communes-2016.csv
    cursor = db.cursor()
    print("\nInsertion Nouvelles Régions : \n")
    with open('csv_files/communes-2016.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        error = 0

        # Skip the first lines
        for i in range(0,7):
            next(spamreader)

        for row in spamreader:
            try:
                #Si le code région est null, on considère que la ligne n'est pas valide pour insertion
                if(row[0]!=""):
                    code_departement = row[2]
                    cursor.execute('''UPDATE departement
                                        SET code_nouvelle_region = ?
                                        WHERE code_departement = ?''',(int(row[3]), code_departement))
            except:
                error = error + 1
                print(' Region '+ str(row[2])+' departement '+ str(row[3])+" -> impossible d'effectuer l'update")
            
        print("\nNombre d'erreurs rencontrées lors de l'insertion de code nouvelle région dans département : "+ str(error)+"\n")
        db.commit()

Pop()
PopNouvellesRegions()



db.close()