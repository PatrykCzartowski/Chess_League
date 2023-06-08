from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from .models import Players, Games

# Create your views here.

def index(request):
    all_players = Players.objects.all
    all_games = Games.objects.all
    return render(request, 'index.html/', {'all_p': all_players, 'all_g': all_games})

def games(request):
    game = Games.objects.all
    return render(request,'games.html/', {'all': game})

def players(request):
    player = Players.objects.all
    return render(request,'players.html/', {'all': player})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request, 'games.html')
    else:
        return render(request, 'login.html')
    
def player_add(request):
    return render(request,'players_add.html/',)

def player_delete(request):
    return render(request,'players_delete.html/',)

def player_update(request):
    return render(request,'players_update.html/',)

def games_add(request):
    return render(request,'games_add.html/',)