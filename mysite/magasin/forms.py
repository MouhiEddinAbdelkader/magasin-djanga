from django import forms 
from .models import Produit, Fournisseur
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['libelle', 'description', 'prix', 'type', 'img', 'categorie', 'fournisseur']

class FournisseurForm(forms.ModelForm):
    class Meta :
       model = Fournisseur
       fields = ['nom', 'adresse','email','telephone' ]
       
class UserRegistrationForm(UserCreationForm):
      first_name = forms.CharField(label='Prénom')
      last_name = forms.CharField(label='Nom')
      email = forms.EmailField(label='Adresse e-mail')
      class Meta(UserCreationForm.Meta):
         model = User
         fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')

