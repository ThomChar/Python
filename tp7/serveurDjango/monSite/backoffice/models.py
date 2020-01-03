from django.db import models

# account
class Account(models.Model):
    pseudo = models.CharField(max_length = 100)
    password = models.CharField(max_length = 225)

    def __unicode__(self) :
        return "{0}".format(self.pseudo)

# informations
class data(models.Model) :
    texte = models.CharField(max_length = 300)