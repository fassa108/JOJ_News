from django import forms
from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return f'{self.titre}'




class Commentaire(models.Model) :

    contenu = models.TextField()
    date_coms = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.auteur} - {self.article}"


class Inscription(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    mot_de_passe = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom}"
    

# class Connexion(models.Model):
#     email = models.EmailField()
#     mot_de_passe = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.email}"