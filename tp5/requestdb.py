import sqlite3
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import xml.dom.minidom
import codecs
from xml.dom import minidom

# Create a database in RAM
db = sqlite3.connect('mydbCommune.db')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('mydbCommune.db')

####################################################"DISPLAY TABS"###############################################

cursor = db.cursor()
cursor1 = db.cursor()
cursor2 = db.cursor()


# Display all regions
def getAllRegions():
    cursor.execute('''SELECT code_region, nom_region FROM region''')
    print("\nListe des régions : \n")
    all_rows = cursor.fetchall()
    for row in all_rows:
        # row[0] returns the first column in the query (code_region), row[1] returns nom_region column.
        print('{0} : {1}'.format(row[0], row[1]))


# Display all departements
def getAllDepartements():
    cursor.execute('''SELECT code_departement, nom_departement, code_region FROM departement''')
    print("\nListe des départements : \n")
    all_rows = cursor.fetchall()
    for row in all_rows:
        # row[0] returns the first column in the query (code_region), row[1] returns nom_region column.
        print('{0} : {1} , Région {2}'.format(row[0], row[1], row[2]))

# Display all communes
def getAllCommunes():
    cursor.execute('''SELECT code_commune, nom_commune, population_totale,code_departement FROM commune''')
    print("\nListe des communces : \n")
    all_rows = cursor.fetchall()
    for row in all_rows:
        # row[0] returns the first column in the query (code_communce), row[1] returns nom_communce column.
        print(' Département : {3}, {0} : {1} , {2} habitants,'.format(row[0], row[1], row[2], row[3]))


# Calcul Pop Total des départements
def getPopdepartements():
    cursor.execute('''SELECT code_departement, nom_departement, code_region FROM departement''')
    print("\nCalcul de population par dépatement : \n")
    popDepartementTemp = 0
    all_rows = cursor.fetchall()
    for row in all_rows:
        cursor1.execute('''SELECT code_commune, nom_commune, population_totale,code_departement FROM commune WHERE code_departement =?''', (row[0],))
        all_rows1 = cursor1.fetchall()
        for row1 in all_rows1:
            popDepartementTemp = popDepartementTemp + row1[2]
        print(' Population totale du département {0} : {1} : {2} habitants,'.format(row[0], row[1], popDepartementTemp))
        popDepartementTemp=0

# Calcul Pop Total des régions
def getPopRegions():
    print("\nCalcul de population par région : \n")
    popRegionTemp = 0
    popDepartementTemp = 0
    cursor.execute('''SELECT code_region, nom_region FROM region''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        cursor1.execute('''SELECT code_departement, nom_departement, code_region FROM departement WHERE code_region =?''', (row[0],))
        all_rows1 = cursor1.fetchall()
        for row1 in all_rows1:
            cursor2.execute('''SELECT code_commune, nom_commune, population_totale,code_departement FROM commune WHERE code_departement =?''', (row1[0],))
            all_rows2 = cursor2.fetchall()
            for row2 in all_rows2:
                popDepartementTemp = popDepartementTemp + row2[2]
            popRegionTemp = popRegionTemp +popDepartementTemp
            popDepartementTemp = 0
        print(' Population totale de la région {0} : {1} : {2} habitants,'.format(row[0], row[1], popRegionTemp))
        popRegionTemp = 0

# Get Communce même nom mais département différent
def getCommunesDepDiff():
    nbSameName = 0
    cursor.execute('''SELECT code_commune, nom_commune, population_totale,code_departement FROM commune ''')
    print("\nListe des communces ayant le mème nom mais des départements différents : \n")
    all_rows = cursor.fetchall()
    for row in all_rows:
        cursor1.execute('''SELECT code_commune, nom_commune, population_totale,code_departement FROM commune WHERE nom_commune =? AND code_departement != ?''', (row[1],row[3]))
        all_rows1 = cursor1.fetchall() 
        if(all_rows1.__len__()>1):
            print('{0} : '.format(row[1]))
            for row1 in all_rows1:
                print(row1[3] + ', ')
            nbSameName = nbSameName +1
    print(nbSameName + ' villes ayant un même nom pour un département différent')


# Export DataBase to xmlfile
def XmlExport():

    #Recherche des régions
    cursor.execute('''SELECT code_region, nom_region FROM region ''')
    all_rows = cursor.fetchall()

    top = Element('top')

    region = SubElement(top, 'region')

    for row in all_rows:
        code_region = SubElement(region, 'code_region')
        code_region.text = str(row[0])
        nom_region = SubElement(region, 'nom_region')
        nom_region.text = str(row[1])

    departement = SubElement(top, 'departement')
    cursor.execute('''SELECT code_departement, nom_departement, code_region FROM departement ''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        code_departement = SubElement(departement, 'code_departement')
        code_departement.text = str(row[0])
        nom_departement = SubElement(departement, 'nom_departement')
        nom_departement.text = str(row[1])
        code_region = SubElement(departement, 'code_region')
        code_region.text = str(row[2])

    commune = SubElement(top, 'commune')
    cursor.execute('''SELECT nom_commune,code_commune,population_totale,code_departement FROM commune ''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        nom_commune = SubElement(commune, 'nom_commune')
        nom_commune.text = str(row[0])
        code_commune = SubElement(commune, 'code_commune')
        code_commune.text = str(row[1])
        population_totale = SubElement(commune, 'population_totale')
        population_totale.text = str(row[2])
        code_departement = SubElement(commune, 'code_departement')
        code_departement.text = str(row[3])


    dom = xml.dom.minidom.parseString(tostring(top))
    pretty_xml_as_string = dom.toprettyxml(indent="\t")
    print (pretty_xml_as_string)
    
    #Ecriture dans fichier d'export
    xmlstr = minidom.parseString(tostring(top)).toprettyxml(indent="   ")
    with codecs.open("ExportDatabase.xml", 'w', encoding='utf8') as f:
        f.write(xmlstr)

    print ('\n Sauvegarde de la base de données dans ExportDatabase.xml faite !')

# Import DataBase from xmlfile
def XmlImport():

    from xml.etree import ElementTree

    dom = ElementTree.parse('ExportDatabase.xml')

    # Recuperer les arguments d'une région et les stockers dans une liste
    args_list = ([t.text for t in dom.iter(tag)] for tag in ['code_region','nom_region'])

    # create the tuples from the argument list
    sqltuples = list(zip(*args_list))
    for row in sqltuples:
        print(row[0],row[1])
        cursor.execute('''INSERT INTO region(code_region, nom_region)
                  VALUES(?,?)''',((int(row[0])),str(row[1])))
    db.commit()

    # Recuperer les arguments d'un département et les stockers dans une liste
    args_list1 = ([t.text for t in dom.iter(tag)] for tag in ['code_departement','nom_departement','code_region'])

    # create the tuples from the argument list 1
    sqltuples1 = list(zip(*args_list1))
    for row1 in sqltuples1:
        print(row1[0],row1[1])
        cursor.execute('''INSERT INTO departement(code_departement, nom_departement, code_region)
                  VALUES(?,?,?)''',((str(row1[0])),str(row1[1]),int(row1[2])))
    db.commit()

    # Recuperer les arguments d'une commune et les stockers dans une liste
    args_list2 = ([t.text for t in dom.iter(tag)] for tag in ['nom_commune','code_commune','population_totale','code_departement'])

    # create the tuples from the argument list 1
    sqltuples2 = list(zip(*args_list2))
    for row2 in sqltuples2:
        cursor.execute('''INSERT INTO commune(nom_commune, code_commune ,population_totale,code_departement)
                  VALUES(?,?,?,?)''',(str(row2[0]),int(row2[1]),int(row2[2]),str(row2[3])))
    db.commit()

    print('\n Upload de la base de données dans ExportDatabase.xml faite !')

# Calcul Pop Total des nouvelles régions
def getPopNouvellesRegions():
    print("\nCalcul de population par région : \n")
    popRegionTemp = 0
    popDepartementTemp = 0
    cursor.execute('''SELECT code_region, nom_region FROM nouvelleRegion''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        cursor1.execute('''SELECT code_departement, nom_departement, code_region, code_nouvelle_region FROM departement WHERE code_nouvelle_region =?''', (row[0],))
        all_rows1 = cursor1.fetchall()
        for row1 in all_rows1:
            cursor2.execute('''SELECT code_commune, nom_commune, population_totale,code_departement FROM commune WHERE code_departement =?''', (row1[0],))
            all_rows2 = cursor2.fetchall()
            for row2 in all_rows2:
                popDepartementTemp = popDepartementTemp + row2[2]
            popRegionTemp = popRegionTemp +popDepartementTemp
            popDepartementTemp = 0
        print(' Population totale de la nouvelle région {0} : {1} : {2} habitants,'.format(row[0], row[1], popRegionTemp))
        popRegionTemp = 0


############################################## EXECUTION DES FONCTIONS ##################################################

#getAllRegions()
#getAllDepartements()
#getAllCommunes()
#getPopdepartements()
#getPopRegions()
#getCommunesDepDiff()
#XmlExport()
#XmlImport()
getPopNouvellesRegions()

db.close()