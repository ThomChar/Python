import datetime

class Date:
 
    def __init__(self, year, month, day):
        self.day = day
        self.month = month
        self.year = year
 
    def __eq__(self, dateCompared):
        if(self.day == dateCompared.day and self.month == dateCompared.month and self.year == dateCompared.year):
            return True
        else:
            return False
    def __lt__(self, dateCompared):
        if(self.year < dateCompared.year):
            return True
        else:
            if(self.month < dateCompared.month and self.year == dateCompared.year):
                return True
            else: 
                if(self.day < dateCompared.day and self.month == dateCompared.month and self.year == dateCompared.year):
                    return True
        return False


class Etudiant:
 
    def __init__(self,prenom, nom, age):
        self.prenom = prenom
        self.nom = nom
        self.age = age
    
    def __adresselec__(self,prenom,nom):
        return prenom+"."+nom+"@etu.univ-tours.fr"
    
    #Fonction Probablement incomplète
    def __age__(self,dateBirth):
        today  = datetime.datetime.now()
        myTodaydate = Date(today.year,today.month, today.day)

        if(dateBirth < myTodaydate):
            newAge = myTodaydate.year-dateBirth.year
            if(myTodaydate.month < dateBirth.month): # Cas ou mois de naissance n'est pas encore passé
                newAge = newAge - 1
            elif(myTodaydate.month == dateBirth.month and myTodaydate.day < dateBirth.day): # Cas ou mois et même que celui de naissance
                newAge = newAge - 1
            return newAge
        else:
            return 0
    
    def __str__(self):
     return "prenom : "+self.prenom+", nom : "+self.nom+", age : "+str(self.age)