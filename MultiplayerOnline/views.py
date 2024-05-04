from django.shortcuts import render
from MultiplayerOnline.models import ChessGame, ChessLobbies
import json, os
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse    
import logging
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def CreateMatch(request):

    player_username = request.session['username']
    completed_lobby = ChessLobbies.objects.filter(
    (Q(white_player=player_username) & Q(game_status='completed')) |
    (Q(black_player=player_username) & Q(game_status='completed'))).first()
    if completed_lobby:
        return JsonResponse({'id': completed_lobby.id, 'game_status': completed_lobby.game_status})
    
    existing_lobby = ChessLobbies.objects.filter(white_player=player_username, game_status='waiting').first()
   
    if existing_lobby:
        return JsonResponse({'id': existing_lobby.id, 'game_status': existing_lobby.game_status})

    available_lobby = ChessLobbies.objects.exclude(white_player=player_username).filter(game_status='waiting', black_player='').first()

    if available_lobby:
        available_lobby.black_player = player_username
        available_lobby.game_status = 'completed'
        available_lobby.game_data['black'] = [request.session['rT7gM2sP5qW8jN4'], player_username, '32523caacfbc25d536b7e7ccbc7e3e97baf4b9e38fc43d229de3da54c36e7a4b']
        
        available_lobby.save()
        return JsonResponse({'id': available_lobby.id, 'game_status': available_lobby.game_status})

    else:
        new_lobby = ChessLobbies.objects.create(
            white_player=player_username,
            game_status='waiting'
        )

        json_data = {
            'ID_Room': str(new_lobby.id),
            "white": [request.session['rT7gM2sP5qW8jN4'], player_username, 'dc724af18fbdd4e59189f5fe768a5f8311527050d9b8a52c989f6e7f085e8b90'],
            "black": [],
            'move': [],
        }
        new_lobby.game_data = json_data
        new_lobby.save()

        return JsonResponse({'id': new_lobby.id, 'game_status': new_lobby.game_status})


def chess(request, ID):

    lobby = ChessLobbies.objects.filter(id=ID).first()
    
    request.session['chess_match'] = ID
    if request.session['username'] == lobby.game_data['white'][1]:

        return render(request, 'chess.html', {'id': lobby.game_data['white'][2], 'cookie': request.session['rT7gM2sP5qW8jN4'] })
    elif request.session['username'] == lobby.game_data['black'][1]:
        return render(request, 'chess.html', {'id': lobby.game_data['black'][2], 'cookie': request.session['rT7gM2sP5qW8jN4'] }) 
    else:
        pass