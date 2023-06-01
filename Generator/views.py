from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'Generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(()__+~'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'Generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'Generator/about.html')