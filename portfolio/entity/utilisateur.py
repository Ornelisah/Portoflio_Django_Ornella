from django.db import models

    
class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    poste = models.CharField(max_length=50)
    observation = models.CharField(max_length=250)
    mail = models.CharField(max_length=30)
    mdp= models.CharField(max_length=15)
    
    


