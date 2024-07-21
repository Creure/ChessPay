from django.shortcuts import render
from MultiplayerOnline.models import ChessGame, ChessLobbies
import json, os
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse    
import logging
from django.db.models import Q

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def CreateMatch(request):


    
    player_username = request.session['username']
    search_lobbies = ChessLobbies.objects.filter(
        (
            (Q(white_player=player_username) | Q(black_player=player_username)) &
            Q(game_status__in=['completed', 'waiting', 'playing'])
        )
    ).first()
    
    
    if search_lobbies:
        return JsonResponse({'id': search_lobbies.id, 'game_status': search_lobbies.game_status})
   

    
    
    available_lobby = ChessLobbies.objects.exclude(white_player=player_username).filter(game_status='waiting', black_player='').first()
    playing_lobby = ChessLobbies.objects.exclude(white_player=player_username).filter(game_status='playing', black_player='').first()

    if available_lobby:
        available_lobby.black_player = player_username
        available_lobby.game_status = 'completed'
        available_lobby.game_data['black'] = [request.session['rT7gM2sP5qW8jN4'], player_username, 'black']
        
        available_lobby.save()
        return JsonResponse({'id': available_lobby.id, 'game_status': available_lobby.game_status})

    elif playing_lobby:
        return JsonResponse({'id': playing_lobby.id, 'game_status': playing_lobby.game_status}) 
    else:
        new_lobby = ChessLobbies.objects.create(
            white_player=player_username,
            game_status='waiting'
        )

        json_data = {
            'ID_Room': str(new_lobby.id),
            "white": [request.session['rT7gM2sP5qW8jN4'], player_username, 'white'],
            "black": [],
            
        }
        new_lobby.game_data = json_data
        new_lobby.save()

        return JsonResponse({'id': new_lobby.id, 'game_status': new_lobby.game_status})

@login_required
def chess(request, ID):

    lobby = ChessLobbies.objects.filter(id=ID).first()


    request.session['chess_match'] = ID
    players = {
        'white': lobby.game_data['white'][1], 'black': lobby.game_data['black'][1],
    }
    if request.session['username'] == lobby.game_data['white'][1]:
        return render(request, 'chess.html', {'id': lobby.game_data['white'][2], 'cookie': request.session['rT7gM2sP5qW8jN4'], 'players': players})
    elif request.session['username'] == lobby.game_data['black'][1]:
        return render(request, 'chess.html', {'id': lobby.game_data['black'][2], 'cookie': request.session['rT7gM2sP5qW8jN4'], 'players': players }) 
    else:
        pass