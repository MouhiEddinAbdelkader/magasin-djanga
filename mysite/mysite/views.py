from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def acceuil(request):
    return render(request,'acceuil.html' )

# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# @login_required
# def acceuil(request):
#     context={'val':"Menu Acceuil"}
#     return render(request,'acceuil.html', context )

def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('magasin/mesProduit')
        else:
            messages.error(request, 'Logged in Fail')
    return render(request, 'acceuil.html')

from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)