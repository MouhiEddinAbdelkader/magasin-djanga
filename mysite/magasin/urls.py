from django.urls import path   
from . import views
from .views import ListeProduits 
from django.contrib.auth import views as auth_views
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views

app_name = "magasin"
urlpatterns = [	
    path('mesProduit/', views.mesProduit,name="mesProduit" ),
    path('addProduit/', views.addProduit ,name="addProduit" ),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouvFournisseur'),
    path('register/',views.register, name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name='magasin/registration/login.html'), name = 'login'),  
    path('logout/', views.logout_view, name = 'logout'),
    
    
    
path('liste_produits', views.ListeProduits.as_view(), name='liste_produits'),
# path('<slug:slug>/', views.DetailProduit, name='produit'),
# path('ajouter/', CreerProduit.as_view(), name='creer_produit'),
# path('<int:pk>/modifier/', ModifierProduit.as_view(), name='modifier_produit'),
# path('<int:pk>/supprimer/', SupprimerProduit.as_view(), name='supprimer_produit'),
 
    ]
