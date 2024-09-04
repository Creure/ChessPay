from django.shortcuts import render, redirect
from MultiplayerOnline.models import ChessLobbies
import json, os
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import logging
from django.db.models import Q
from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404
# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html', {"profile": 'true', 'user' : request.user, })




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
            Q(game_status__in=['completed', 'playing'])
        )
    ).first()
    try:
        id_info = str(search_lobbies.id)
    except:
        id_info = False

   
    return render(request, 'lobbies.html', {'lobbies_information': page_obj, 'before': str(page - 1), 'next':Next, 'user' : user, "lobbies": 'true', 'join': id_info })
@login_required
def wallet(request):
    return render(request, 'wallet.html', {"wallet": 'true', 'user' : request.user, })

@login_required
def join(request, id_info):
    match_query = get_object_or_404(ChessLobbies, pk=id_info) #needs to verify if there an user before to apply the changes

    if not match_query:
        return HttpResponse('Match not found', status=404)

    username = request.session.get('username')

    if not match_query.white_player:
        match_query.white_player = username
        match_query.save()
        return redirect(f'/chess/{str(match_query.id)}')
    else:
        match_query.black_player = username
        match_query.game_status = 'completed'
        match_query.save()
        request.session['chess_match'] = id_info
        return redirect(f'/chess/{str(match_query.id)}')
        


@login_required
def CreateMatch(request, amount, piece):
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
                bet_amount=amount
            )
        else:
             new_lobby = ChessLobbies.objects.create(
                black_player=player_username,
                game_status='waiting',
                bet_amount=amount
            )
        
        new_lobby.save()
        request.session['chess_match'] = str(new_lobby.id)
        return JsonResponse({'id': str(new_lobby.id), 'game_status': new_lobby.game_status})

@login_required
def chess(request, ID):

    lobby = ChessLobbies.objects.filter(id=ID).first()

    #logic problems when who created the lobby get it

    
    if request.session['username'] == lobby.white_player:
        return render(request, 'chess.html', {'id': 'white', 'cookie': request.session['rT7gM2sP5qW8jN4'], 'chess': 'true','lobby_info': lobby})
    elif request.session['username'] == lobby.black_player:
        return render(request, 'chess.html', {'id': 'black', 'cookie': request.session['rT7gM2sP5qW8jN4'], 'chess': 'true','lobby_info': lobby }) 
    else:
        return HttpResponse(f'No disponible: {id_info}')









