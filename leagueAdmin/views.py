from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from .models import Players, Games

#--------------------------------#
# Main pages rendering:
#--------------------------------#
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

#--------------------------------#
# Login page rendering and validation:
#--------------------------------#
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return games(request)
    else:
        return render(request, 'login.html')
    
#--------------------------------#
#Admins - player CRUD operations:
#--------------------------------#

# Player add form rendering and saving in the database:
def player_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        ranking = request.POST.get('ranking')
        new_player = Players(name=name, surname=surname, ranking=ranking)
        new_player.save()
        
    return render(request,'player_add.html',)

# Player delete form rendering and deleting from the database:
def player_delete(request):
    if request.method == 'POST':
        rm_id = request.POST.get('ID')
        try:
            ID = Players.objects.get(id=rm_id)
            ID.delete() 
        except:
            return players(request)
    return render(request,'player_delete.html',)

# Player update form rendering and updating the database:
def player_update(request):
    if request.method == 'POST':
        up_id = request.POST.get('ID')
        new_ranking = request.POST.get('ranking')
        try:
            player = Players.objects.get(id=up_id)
            player.ranking = new_ranking
            player.save()
        except:
            return players(request)
    return render(request,'player_update.html',)

#--------------------------------#
#Admins - game CRUD operations:
#--------------------------------#

# Game add form rendering and saving in the database:
def game_add(request):
    if request.method == 'POST':
        players = request.POST.get('players')
        result = request.POST.get('result')
        if result == '1:0' or result == '1:1' or result == '0:1':
            new_game = Games(players=players, result=result)
            new_game.save()
        else:
            return games(request)
    
    return render(request,'game_add.html',)

# Game delete form rendering and deleting from the database:
def game_delete(request):
    if request.method == 'POST':
        rm_id = request.POST.get('ID')
        try:
            ID = Games.objects.get(id=rm_id)
            ID.delete() 
        except:
            return games(request)
    return render(request,'game_delete.html',)

# Game update form rendering and updating the database:
def game_update(request):
    if request.method == 'POST':
        up_id = request.POST.get('ID')
        new_result = request.POST.get('result')
        try:
            game = Games.objects.get(id=up_id)
            game.result = new_result
            game.save()
        except:
            return games(request)
    return render(request,'game_update.html',)