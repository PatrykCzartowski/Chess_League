from django.shortcuts import render
from django.http import HttpResponse
from .models import Players, Games

# Create your views here.

def index(request):
    all_players = Players.objects.all
    all_games = Games.objects.all
    return render(request, 'index.html/', {'all_p': all_players, 'all_g': all_games})

def games(request):
    return render(request,'games.html/')

def players(request):
    return render(request,'players.html/')