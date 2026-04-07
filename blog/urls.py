


from django.urls import path

from blog import views


urlpatterns = [
    path('accueil/', views.accueil, name = 'accueil'),
    path('detail/<int:pk>/', views.detail, name = 'detail'),
    path('modifier/<int:pk>/', views.CommentUpdateView.as_view(), name = 'modifier_commentaire'),
    path('supprimer/<int:pk>/', views.CommentDeleteView.as_view(), name = 'supprimer_commentaire'),


]