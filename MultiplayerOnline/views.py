from django.shortcuts import render, redirect
from MultiplayerOnline.models import ChessLobbies
import json, os
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import logging, pdb
from django.db.models import Q
from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return redirect('/wallet/')

@login_required
def profile(request):
    search_lobbies = ChessLobbies.objects.filter(
        (
            (Q(white_player=request.session['username']) | Q(black_player=request.session['username'])) &
            Q(game_status__in=['waiting','completed', 'playing'])
        )
    ).first()
    try:
        id_info = str(search_lobbies.id)
    except:
        id_info = False
    
    return render(request, 'profile.html', {"profile": 'true', 'user' : request.user, 'join': id_info})




@login_required
def lobbies(request, page):

    

    all_lobbies = ChessLobbies.objects.filter(game_status='waiting')
    paginator = Paginator(all_lobbies, 10)
    user = request.user
    page_obj = paginator.get_page(page)
    
    if page < paginator.num_pages :
        Next = str(page + 1)
    else:
        Next = str(paginator.num_pages)

    search_lobbies = ChessLobbies.objects.filter(
        (
            (Q(white_player=request.session['username']) | Q(black_player=request.session['username'])) &
            Q(game_status__in=['waiting','completed', 'playing'])
        )
    ).first()
    try:
        id_info = str(search_lobbies.id)
    except:
        id_info = False

   
    return render(request, 'lobbies.html', {'lobbies_information': page_obj, 'before': str(page - 1), 'next':Next, 'user' : user, "lobbies": 'true', 'join': id_info })

@login_required
def wallet(request):
    search_lobbies = ChessLobbies.objects.filter(
        (
            (Q(white_player=request.session['username']) | Q(black_player=request.session['username'])) &
            Q(game_status__in=['waiting','completed', 'playing'])
        )
    ).first()
    try:
        id_info = str(search_lobbies.id)
    except:
        id_info = False
    return render(request, 'wallet.html', {"wallet": 'true', 'user' : request.user, 'join': id_info})

@login_required
def join(request, id_info):
    match_query = get_object_or_404(ChessLobbies, pk=id_info) #needs to verify if there an user before to apply the changes

    if not match_query:
        return HttpResponse('Match not found', status=404)

    username = request.session.get('username')

    if not match_query.white_player:
        match_query.white_player = username
        match_query.save()
        request.session['chess_match'] = match_query.id
        return redirect(f'/chess/{str(match_query.id)}')
    else:
        match_query.black_player = username
        match_query.game_status = 'completed'
        match_query.save()
        request.session['chess_match'] = match_query.id
        return redirect(f'/chess/{str(match_query.id)}')
        


@login_required
def CreateMatch(request, amount, piece,timer):
    amount = float(amount.replace(',', '.'))

    
    player_username = request.session['username']
    search_lobbies = ChessLobbies.objects.filter(
        (
            (Q(white_player=player_username) | Q(black_player=player_username)) &
            Q(game_status__in=['completed', 'waiting', 'playing'])
        )
    ).first()
    
    if search_lobbies:
        try:
            request.session['chess_match'] = str(search_lobbies.id)
            return JsonResponse({'id': str(search_lobbies.id), 'game_status': search_lobbies.game_status}) 
        except:
            pass
    else:
        if piece == 'white':
            new_lobby = ChessLobbies.objects.create(
                white_player=player_username,
                game_status='waiting',
                bet_amount=amount,
                timer_black_player=timer * 60,
                timer_white_player=timer * 60,
                timer = timer,
                this_chessboard= {
                        "logs": {
                            "log_move": [],
                            "logs_timers": []
                        },
                        "board_fen": 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR',
                        'pieces_captured': {
                            'white_captured':[],
                            'black_captured': []
                        }
                    }
            )
        else:
             new_lobby = ChessLobbies.objects.create(
                black_player=player_username,
                game_status='waiting',
                bet_amount=amount,
                timer_black_player=timer * 60,
                timer_white_player=timer * 60,
                timer = timer,
                this_chessboard= {
                        "logs": {
                            "log_move": [],
                            "logs_timers": []
                        },
                        "board_fen": 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR',
                        'pieces_captured': {
                            'white_captured':[],
                            'black_captured': []
                        }
                    }
            )
        
        new_lobby.save()
        request.session['chess_match'] = str(new_lobby.id)
        return JsonResponse({'id': str(new_lobby.id), 'game_status': new_lobby.game_status})

@login_required
def chess(request, ID):
    lobby = ChessLobbies.objects.filter(id=ID).first()
    player_color = 'white' if request.session.get('username') == lobby.white_player else 'black' if request.session.get('username') == lobby.black_player else None
    
    if lobby.game_status in ['waiting', 'playing', 'completed']:
        return render(request, 'chess.html', {
            'id': player_color,
            'cookie': request.session.get('rT7gM2sP5qW8jN4'),
            'chess': 'true',
            'lobby_info': lobby,
            'timer_white': lobby.timer_white_player // 60,
            'timer_black': lobby.timer_black_player // 60,
            'timer': lobby.timer,
            'id_lobby': lobby.id,
            
            
            
        }) if player_color else HttpResponse(f'No disponible: {ID}')

    elif lobby.game_status in ['timeout', 'Check Mate!', 'draw']:
        return redirect('/result/' + lobby.id)


def result(request, ID):
    lobby = ChessLobbies.objects.filter(id=ID).first()
    player_color = 'white' if request.session.get('username') == lobby.white_player else 'black' if request.session.get('username') == lobby.black_player else None
    if lobby.game_status in ['waiting', 'playing', 'completed']:
        return redirect('/chess/' + lobby.id)
    info_dict = {
        'id': player_color,
        'cookie': request.session.get('rT7gM2sP5qW8jN4'),
        'result': 'true',
        'lobby_info': lobby,
        'timer_white': lobby.timer_white_player // 60,
        'timer_black': lobby.timer_black_player // 60,
        'timer': lobby.timer,
        'id_lobby': lobby.id,
        'player': request.session.get('username'),
        'status': True,
        'board_fen':lobby.this_chessboard['board_fen']
    }
    if request.session.get('username') == lobby.winning_player:

        info_dict['result'] = True
        info_dict['ChessCoin']= lobby.bet_amount / 2 if lobby.bet_amount < 10 else float(lobby.bet_amount)* 0.90
        
    else:
        info_dict['result'] = False
        info_dict['ChessCoin']= lobby.bet_amount 
    return render(request, 'result.html',info_dict ) if player_color else HttpResponse(f'No disponible: {ID}')



