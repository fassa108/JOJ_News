


from django.urls import path

from blog import views


urlpatterns = [
    path('accueil/', views.accueil, name = 'accueil'),
]