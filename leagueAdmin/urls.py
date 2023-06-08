from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('games/',views.games, name="games"),
    path('players/',views.players, name="players"),
    path('login/',views.log_in , name="login"),
    path('player_add/',views.player_add, name="player_add")
]