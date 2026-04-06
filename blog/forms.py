

from django import forms

from .models import Categorie, Article


class CategorieForm(forms.ModelForm):
    
    class Meta :
        model = Categorie
        fields = ['nom']
    

    

class ArticleForm(forms.ModelForm) :
    
    class Meta :
        model = Article
        fields = ['titre','contenu','categorie']