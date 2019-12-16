import sqlite3


# Create a database in RAM
db = sqlite3.connect('mydbCommune.db')
# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('mydbCommune.db')

####################################################"DROP ALL TABLE"###############################################
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS commune')
db.commit()
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS departement')
db.commit()
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS region')
db.commit()
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS nouvelleRegion')
db.commit()

####################################################"CREATE ALL TABLE"###############################################

# CREATE : Communes
# CREATE TABLE commune(nom_commune VARCHAR ,code_commune INTEGER,population_totale INTEGER, code_departement VARCHAR, PRIMARY KEY ([code_departement],[code_commune]))
cursor = db.cursor()
cursor.execute('''
     CREATE TABLE commune(nom_commune VARCHAR ,code_commune INTEGER,population_totale INTEGER, code_departement VARCHAR)
''')
db.commit()

# CREATE : Departement
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE departement(code_departement VARCHAR PRIMARY KEY, nom_departement TEXT, code_region INTEGER,  'code_nouvelle_region' INTEGER)
''')
db.commit()

# CREATE : Region
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE region(code_region INTEGER PRIMARY KEY, nom_region TEXT)
''')
db.commit()

# CREATE : Nouvelles Regions
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE nouvelleRegion(code_region INTEGER PRIMARY KEY, nom_region TEXT, nb_com INTEGER)
''')
db.commit()


db.close()