from django.shortcuts import render
from django.http import HttpResponse
from .models import Games

# Create your views here.

def main(request):
    games = Games.objects.all()
    return render(request , "main/index.html" , context={'games': games})