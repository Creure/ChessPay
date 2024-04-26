from django.shortcuts import render
from MultiplayerOnline.models import ChessGame
import json, os
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse    
# Create your views here.
def white(request):
    return render(request, 'white.html', {'id': 'dc724af18fbdd4e59189f5fe768a5f8311527050d9b8a52c989f6e7f085e8b90'})

def black(request):
    return render(request, 'black.html', {'id': '32523caacfbc25d536b7e7ccbc7e3e97baf4b9e38fc43d229de3da54c36e7a4b'})

def home(request):
    return render(request, 'home.html')

@login_required
def CreateMatch(request):

    player_username = request.session['username']
    
    if not os.path.exists('Chess_Lobbies/rooms.json'):


        new_game = ChessGame.objects.create(white_player=player_username, black_player="None", game_status="pending", move_history=[], 
                                            start_time=None, end_time=None, result=None, 
                                            tokens={"token_white": 
                                                    request.session['rT7gM2sP5qW8jN4'], "token_black": ""
                                                    })
        match_info = {
            "rooms": [
                {
                "ID_Room": str(new_game.id),
                "white":[request.session['rT7gM2sP5qW8jN4'], new_game.white_player],
                "black":[],
                "status": "waiting",
                "Move": []
                }
                
            ]
        }
        with open('Chess_Lobbies/rooms.json', 'w') as match:
            rw =  json.dump(match_info, match)
        
        return JsonResponse({'id': str(new_game.id)})
    else:
        with open('Chess_Lobbies/rooms.json', 'r+') as match:
            rooms = json.load(match)
            
            for room in rooms['rooms']:
                if room['white'] == [request.session['rT7gM2sP5qW8jN4'], player_username] or room['black'] == [request.session['rT7gM2sP5qW8jN4'], player_username] :
                    if  room['status'] == 'completed' or room['status'] == 'waiting':
                        return  JsonResponse(room) 
                
                if room['status'] == 'waiting':
                    if room['white'][1] != player_username and room['black'] == []:
                        room['black'] = [request.session['rT7gM2sP5qW8jN4'], player_username]
                        room['status'] = 'completed'
                        with open('Chess_Lobbies/rooms.json', 'w') as match_update:
                            json.dump(rooms, match_update)
                        return  JsonResponse({'id': str(room['ID_Room']), 'status': 'completed'}) 
                    else:
                        pass
            

        new_game = ChessGame.objects.create(white_player=player_username, black_player="None", game_status="pending", move_history=[], 
                                            start_time=None, end_time=None, result=None, 
                                            tokens={"token_white": 
                                                    request.session['rT7gM2sP5qW8jN4'], "token_black": ""
                                                    })
        
        with open('Chess_Lobbies/rooms.json', 'w') as match:
            new_room = {
                "ID_Room": str(new_game.id),
                "white":[request.session['rT7gM2sP5qW8jN4'], new_game.white_player],
                "black":[],
                "status": "waiting",
                "Move": []
                }
            rooms['rooms'].append(new_room)
            rw =  json.dump(rooms, match)
            return JsonResponse({'id': str(new_game.id)})
            