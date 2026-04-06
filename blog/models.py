from django import forms
from django.db import models

# Create your models here.
class Categorie(models.Model) :

    nom = models.CharField(max_length = 100, unique=True)
    
    def __str__(self):
        return self.nom

class Article(models.Model) :

    titre = models.CharField(max_length = 255)
    contenu = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete = models.SET_NULL, null = True, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)