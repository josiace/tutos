from django.shortcuts import render
from .models import Acceuilperso, Contenus
# Create your views here.
def contenu(request):
    contenus = Contenus.objects.all()
    return render(request, 'blogs.html', {'contenus': contenus})

def acceuil(request):
    acceuils = Acceuilperso.objects.all()
    return render(request, 'acceuil.html',{'acceuils': acceuils})