from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('games/',views.games, name="games"),
    path('players/',views.players, name="players"),
    path('login/',views.log_in , name="login"),
    path('player_add/',views.player_add, name="player_add"),
    path('player_delete/',views.player_delete, name="player_delete"),
    path('player_update/',views.player_update, name="player_update"),
    path('game_add/',views.game_add, name="game_add"),
    path('game_delete/',views.game_delete, name="game_delete"),
    path('game_update/',views.game_update, name="game_update")
]