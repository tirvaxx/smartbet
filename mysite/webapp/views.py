from django.shortcuts import render
from django.http import HttpResponse
from mailchimp3 import Mailchimp

def index(request):    
# Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'webapp/index.html', locals())
# Create your views here.


