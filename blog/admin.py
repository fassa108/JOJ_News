from django.contrib import admin

# Register your models here.
from .models import Article, Categorie

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_publication')
    list_filter = ('categorie',)
    search_fields = ('titre',)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)