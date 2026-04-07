from django.contrib import admin

# Register your models here.
from .models import Article, Categorie, Commentaire, Inscription

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_publication')
    list_filter = ('categorie',)
    search_fields = ('titre',)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'article', 'date_coms')
    list_filter = ('article',)

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')