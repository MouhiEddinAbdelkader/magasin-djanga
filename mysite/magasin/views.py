from django.shortcuts import render, redirect
from .models import Produit
from .forms import ProduitForm, FournisseurForm ,UserRegistrationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic.detail import DetailView
from .models import Produit
from django.views import generic
from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Produit
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse 

# Create your views here.
def mesProduit(request):
    list = Produit.objects.all()
    return render(request, 'magasin/vitrine.html', {'list': list})

def addProduit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')

    else:
        form = ProduitForm()
    return render(request,'magasin/majProduits.html',{'form':form})

def nouveauFournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    
    else :
        form = FournisseurForm()
    return render(request,'magasin/fournisseur.html',{'form':form})
    



def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('/magasin/mesProduit')
    else :
        form = UserCreationForm()
    return render(request,'magasin/registration/register.html',{'form' : form})


# def LoginView(request):
#     if request.method == 'POST':
#         user = authenticate(request, username=request.POST["username"],
#                             password=request.POST["password"])
#         if user:
#             login(request, user)
#             messages.success(request, 'Logged in successfully')
#             return redirect('magasin/mesProduit')
#         else:
#             messages.error(request, 'Logged in Fail')
#     return render(request,'registration/login.html')

def logout_view(request):
    logout(request)
    # Redirige l'utilisateur vers une page une fois déconnecté, par exemple la page d'accueil.
    return redirect(reverse('logout'))


    
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProduitForm
from .models import Produit

from django.views import generic
from .models import Produit  # Assuming 'Produit' is your model name

class ListeProduits(generic.ListView):
    model = Produit
    context_object_name = 'liste_produits'
    template_name = 'magasin/liste_produit.html'
    def get_queryset(self):
        # Dynamically filter the queryset to get products with 'war' in their label
        return Produit.objects.filter(libelle__icontains='war')[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context




from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)