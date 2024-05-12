from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Categorie(models.Model): 
    name = models.CharField(max_length=50, default='Alimentaire')
    TYPE_CHOICES = [
        ('Al', 'Alimentaires'),
        ('Mb', 'Meuble'),
        ('Sn', 'Sanitaire'),
        ('Vs', 'Vaisselle'),
        ('Vt', 'Vêtement'),
        ('Jx', 'Jouets'),
        ('Lg', 'Linge de Maison'),
        ('Bj', 'Bijou'),
        ('Dc', 'Decor')
    ]
    
class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    telephone = models.CharField(max_length=8)

class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non définie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    TYPE_CHOICES = [('em', 'Emballé'), ('fr', 'Frais'), ('cs', 'Conserve')]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='em')
    img = models.ImageField(blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return f"{self.libelle} - {self.description} - {self.prix} - "
    
class ProduitNC(Produit):
    Duree_garantie = models.CharField(max_length=100) 

class Commande(models.Model):
    dateCde = models.DateField(null=True, default=timezone.now)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField(Produit)