from django.urls import path

from blog import views


urlpatterns = [
    path('', views.accueil, name = 'accueil'),
    path('articles/', views.articles, name = 'articles'),
    path('categorie/', views.categorie, name = 'categorie'),
    path('detail/<int:pk>/', views.detail, name = 'detail'),
    path('modifier/<int:pk>/', views.CommentUpdateView.as_view(), name = 'modifier_commentaire'),
    path('supprimer/<int:pk>/', views.CommentDeleteView.as_view(), name = 'supprimer_commentaire'),
    path('connexion/', views.connexion, name = 'connexion'),
    path('inscription/', views.inscription, name = 'inscription'),
]