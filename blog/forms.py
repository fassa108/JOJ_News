

from django import forms

from .models import Categorie, Article, Commentaire, Inscription


class CategorieForm(forms.ModelForm):
    
    class Meta :
        model = Categorie
        fields = ['nom']


class ArticleForm(forms.ModelForm) :
    
    class Meta :
        model = Article
        fields = ['titre','contenu','categorie']


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']

    
class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['nom', 'prenom', 'email', 'mot_de_passe']