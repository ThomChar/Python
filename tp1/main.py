from allClass import Date,Etudiant

#Tests des classes Date et Etudiant
date = Date(1990,11,12)
date2 = Date(1989,11,12)
date3 = Date(1991,11,12)
date4 = Date(1990,12,12)
date5 = Date(1990,10,12)
date6 = Date(1990,11,13)
date7 = Date(1990,11,11)
etu = Etudiant("prenom","nom",19)
#print(etu.__age__(date))
#print("prenom: " + etu.prenom + ", nom: " + etu.nom + ", age :" + str(etu.age))


#Permet d'extraire la liste des personne du fichier csv
listEtudiant = []
import csv
with open('fichetu.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in csvreader:
        #Creation objet date en fonction de delimiter "/"
        array = row[2].split("/")
        #print(array[0] + " "+array[1]+" "+array[2])
        listEtudiant.append(Etudiant(row[0],row[1],etu.__age__(Date(int(array[2]),int(array[1]),int(array[0])))))
        #print(', '.join(row))

# Affichage de la liste des Etudiants
print("\n Ma liste d'Etudiants : \n")
for etudiant in listEtudiant:    
    print(etudiant)

# Affichage de la liste des courriels des etudiants de la liste
print("\n Emails d'Etudiants : \n")
for etudiant in listEtudiant:    
    print(etu.__adresselec__(etudiant.prenom,etudiant.nom))