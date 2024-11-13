from channels.generic.websocket import AsyncWebsocketConsumer
from Authentication.models import AuthenticationTokenTime
from os import path
import json
from channels.layers import get_channel_layer
from django.conf import settings
import logging
from django.shortcuts import get_object_or_404
from MultiplayerOnline.models import ChessLobbies
import chess, pdb
import asyncio
from channels.db import database_sync_to_async
import datetime
from PayPal_ChessCoin.Nush_ChessCoin import NushChessCoin

from ChessCoin.models import ChessCoin_Transaccions

logging.basicConfig(filename='socket.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s: ')




class ChessBoardCustomer(AsyncWebsocketConsumer):
    async def connect(self):
        
        if self.scope["user"].is_authenticated: 
            self.id = self.scope['session'].get('chess_match')
            self.room_group_name = f'ChessLobby_{self.id}'
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            self.piece_symbols = {
                        'pawn_white': '♙',    
                        'knight_white': '♘',  
                        'bishop_white': '♗',  
                        'rook_white': '♖',    
                        'queen_white': '♕',   
                        'king_white': '♔',    
                        'pawn_black': '♟',    
                        'knight_black': '♞',  
                        'bishop_black': '♝',  
                        'rook_black': '♜',    
                        'queen_black': '♛',   
                        'king_black': '♚'     
                    }
            try:
                csrf_token = self.scope['session'].get('rT7gM2sP5qW8jN4')
                self.data = await database_sync_to_async(AuthenticationTokenTime.objects.get)( pk= csrf_token)
                
                if self.data.valid_session: 
                    
                    self.match_query = await database_sync_to_async(ChessLobbies.objects.get)(pk=self.scope['session'].get('chess_match'))
                    match self.match_query.game_status:

                        case 'completed':
                            self.chess_match = {
                                self.scope['session'].get('chess_match'):chess.Board()
                            }
                        case 'playing':
                            self.chess_match = {
                                self.scope['session'].get('chess_match'):chess.Board(self.match_query.this_chessboard['board_fen']) #if board_fen is empty error
                            }
                        case 'Check Mate!':
                            self.chess_match = {
                                self.scope['session'].get('chess_match'):chess.Board(self.match_query.this_chessboard['board_fen'])
                            }
                        case 'timeout':
                            self.chess_match = {
                                self.scope['session'].get('chess_match'):chess.Board(self.match_query.this_chessboard['board_fen'])
                            }
                            await self.accept()
                            await self.send(text_data=json.dumps({'message':'checkmate','type':'checkmate', 'id': self.match_query.id})) 
                            await self.close()
                        case 'waiting':
                            self.chess_match = {
                                self.scope['session'].get('chess_match'):chess.Board()
                            }

                    await self.accept()
                    await self.send(text_data=json.dumps({'message':'','type':'__init__',
                
                        'username_white': self.match_query.white_player,
                        'username_black': self.match_query.black_player,
                        'chessboard': self.chess_match[self.scope['session'].get('chess_match')].fen(), 'turn': 'white' if self.chess_match[self.scope['session'].get('chess_match')].turn else 'black',
                        'white_timer': str(datetime.timedelta(seconds=self.match_query.timer_white_player))[-5:],
                        'black_timer': str(datetime.timedelta(seconds=self.match_query.timer_black_player))[-5:]
                    }))
                    await self.send(text_data=json.dumps({'message':'updated_chessboard','type':'updated_chessboard', 
                        'chessboard': self.chess_match[self.scope['session'].get('chess_match')].fen(), 'turn': 'white' if self.chess_match[self.scope['session'].get('chess_match')].turn else 'black',
                
                    }))
                    
                    if self.match_query.game_status in [ 'Check Mate!', 'draw']:
                        await self.close()
                    if self.match_query.this_chessboard['board_fen'] != 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR':
                        self.timer = asyncio.create_task(self.start_timer())
                else:
                    await self.close() 
            except Exception as e:
                logging.exception('sorry an error has ocurred: '+ str(e))
                await self.close()
        else:
            self.close()
    
    async def start_timer(self):
        while True:
            if self.chess_match[self.scope['session'].get('chess_match')].turn:  # Turno de blancas
                self.match_query.timer_white_player -= 1
                
                if self.match_query.timer_white_player <= 0:
                    self.match_query.game_status = 'timeout'
                    self.match_query.winning_player = self.match_query.black_player
                    await database_sync_to_async(self.match_query.save)()
                    await self.send_game_state('timer_update')
                    await self.send(text_data=json.dumps({'message':'checkmate','type':'checkmate', 'id': self.match_query.id})) 
                    await self.close()
            else:  # Turno de negras
                self.match_query.timer_black_player -= 1

                if self.match_query.timer_black_player <= 0:
                    self.match_query.game_status = 'timeout'
                    self.match_query.winning_player = self.match_query.white_player
                    await database_sync_to_async(self.match_query.save)()
                    await self.send_game_state('timer_update')
                    await self.send(text_data=json.dumps({'message':'checkmate','type':'checkmate', 'id': self.match_query.id})) 
                    await self.close()
            
            await database_sync_to_async(self.match_query.save)(update_fields=['timer_white_player','timer_black_player']) #set up only save the timer information
            if self.match_query.game_status !='playing':
                break 
            await self.send_game_state('timer_update')
            
            await asyncio.sleep(1)
      

    async def send_game_state(self, message_type):
        chess_match = self.chess_match[self.scope['session'].get('chess_match')]
        await self.send(text_data=json.dumps({
            'type': message_type,
            'chessboard': chess_match.fen(),
            'white_timer': str(datetime.timedelta(seconds=self.match_query.timer_white_player))[-5:],
            'black_timer': str(datetime.timedelta(seconds=self.match_query.timer_black_player))[-5:]
        }))     


    async def disconnect(self, close_code):
        
        self.match_query = await database_sync_to_async(ChessLobbies.objects.get)(pk=self.scope['session'].get('chess_match'))

        if self.match_query.game_status == 'waiting':
           self.match_query.delete()
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('data', '')

        # Envía el mensaje a todos los clientes en el grupo de sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'node',
                'data': message
            }
        )
    async def node(self, event):
        # Modifica el campo this_chessboard
        self.match_query = await database_sync_to_async(ChessLobbies.objects.get)(pk=self.scope['session'].get('chess_match'))

        chess_match = self.chess_match[self.scope['session'].get('chess_match')]


        turn = 'white' if chess_match.turn else 'black'

        message = ''
        if self.match_query.timer_white_player == 0 or self.match_query.timer_black_player == 0:
            self.match_query.winning_player = self.match_query.timer_white_player  if self.match_query.timer_white_player > 0 else self.match_query.black_player
            self.match_query.game_status = 'timeout'
            await database_sync_to_async(self.match_query.save)()

            self.closed()

        match event:
            
            
            case {'data': {'type':'legal_moves'}}:
                position = chess.parse_square(event['data']['position']) 
                legal_moves = chess_match.legal_moves
                legal_moves_pieces = [move for move in legal_moves if move.from_square == position]
                data = []
                message = ''
                #if legal_moves_pieces == []:
                
                for move in legal_moves_pieces:
                    data.append(move.uci())

 
                
                #pdb.set_trace()

                match turn:
                    case 'white':
                        try:

                            if chess_match.piece_at(chess.SQUARE_NAMES.index(event['data']['position'])).piece_type == 1 and '7' in event['data']['position'] and data != []:
                                data = list(set([move[:-1] for move in data]))
                                message = 'pawn-upgrade'
                        except:
                            pass
                    case 'black':
                        try:

                            if chess_match.piece_at(chess.SQUARE_NAMES.index(event['data']['position'])).piece_type == 1 and '2' in event['data']['position'] and data != []:
                                data = list(set([move[:-1] for move in data]))
                                message = 'pawn-upgrade'
                        except:
                            pass
                logging.debug(f'legal_moves:{event['data']['position']}: {data}')
                logging.debug(f"event img_id: {event['data']}")
                await self.send(text_data=json.dumps({'message':message,'type':'legal_moves','legal_moves':data, 'position':event['data']['position'], 'img_id': event['data']['img_id'], 'turn': turn })) 
                
                if data == []:             

                    if chess_match.is_check():
                        if chess_match.turn:
                            king_square = chess_match.king(chess.WHITE)

                        else:
                            king_square= chess_match.king(chess.BLACK)

                        await self.send(text_data=json.dumps({'message':'check','type':'legal_moves','legal_moves':data,'turn': turn, 'king_position': chess.square_name(king_square)}))

                    else:
                        pass#pdb.set_trace()
                
            case  {'data': {'type':'do_the_move'}}:
        
                legal_moves = chess_match.legal_moves
                legal_moves_pieces = [move for move in legal_moves if move.from_square == chess.parse_square(event['data']['position']) ]
                data = []

                for move in legal_moves_pieces:
                    data.append(move.uci())


                if event["data"]['move'] in data:
                    _move_ = chess.Move.from_uci(event["data"]['move'])
                    #this code is to get all capture pieces
                    to_square = _move_.to_square
                    piece = chess_match.piece_at(to_square)
                    chess_match.push(_move_)
                    if chess_match.is_capture(_move_):
                        if piece:
                            color = 'white' if chess_match.piece_at(to_square).color else 'black'
                            piece_type = piece.piece_type
                            piece_symbol = piece.symbol()
                            piece_name = chess.PIECE_NAMES[piece_type]
                           
                            if color =='white':
                                self.match_query.this_chessboard['pieces_captured']['white_captured'].append(self.piece_symbols[f'{piece_name}_{color}'])
                            elif color =='black':
                                self.match_query.this_chessboard['pieces_captured']['black_captured'].append(self.piece_symbols[f'{piece_name}_{color}'])
                            else:
                                logging.debug(f'color={color} capture ')
                    
                    

                    if self.match_query.game_status == 'completed':
                        self.match_query.game_status = 'playing'
                        
                        self.timer = asyncio.create_task(self.start_timer())
                    
                    
                    logging.debug(f'tracking: {event['data']}')
                    self.match_query.this_chessboard['board_fen'] = chess_match.fen()
                    self.match_query.this_chessboard['logs']['log_move'] = [move.uci() for move in chess_match.move_stack]
                    self.match_query.this_chessboard['logs']['logs_timers'].append(f'{self.match_query.timer_white_player}:{self.match_query.timer_black_player}')
                
                    
                    await database_sync_to_async(self.match_query.save)()

                    if 'promoter_pawn' in event['data']:
                        await self.send(text_data=json.dumps({'message':message,'type':'updated', 'turn': turn, 'move': event["data"]['move'],
                        'position':event["data"]['position'],'turn': turn,'chessboard': chess_match.fen(),
                        'img_id': event['data']['img_id'], 'promoter_pawn': event["data"]['promoter_pawn'], 'promoter_to': event["data"]['promoter_to'],
                        })) 
                    
                    else:
                        await self.send(text_data=json.dumps({'message':message,'type':'updated', 'turn': turn, 'move': event["data"]['move'][-2:],
                        'position':event["data"]['position'],'turn': turn,'chessboard': chess_match.fen(),
                        'img_id': event['data']['img_id']})) 
                    

                else:
                    logging.exception(f"invalid move: {event["data"]['move']} ||  position: {event["data"]['position']}")
                    logging.exception(f"data: {data} || legal_moves: {legal_moves} || legal_moves_pieces: {legal_moves_pieces}")

                if chess_match.is_checkmate():
                    await self.send(text_data=json.dumps({'message':'checkmate','type':'checkmate', 'id': self.match_query.id})) 
                    if chess_match.turn == chess.WHITE:
                        self.match_query.winning_player = self.match_query.black_player
                    else:
                        self.match_query.winning_player = self.match_query.white_player
                    self.match_query.game_status = 'Check Mate!'
                    await database_sync_to_async(self.match_query.save)()
                    await NushChessCoin().complete_transaccion(self.match_query.id)
                    await self.close()
                elif chess_match.is_insufficient_material():
                    await self.send(text_data=json.dumps({'message':'checkmate','type':'insuffimaterialcient ', 'id': self.match_query.id})) 
                    if chess_match.turn == chess.WHITE:
                        self.match_query.winning_player = 'draw'
                    else:
                        self.match_query.winning_player = 'draw'
                    self.match_query.game_status = 'draw'
                    await database_sync_to_async(self.match_query.save)()
                    
                    await self.close()
                    self.close()    

        

        await self.send(text_data=json.dumps({'message':'','type':'__init__',
                
            'username_white': self.match_query.white_player,
            'username_black': self.match_query.black_player,
            'chessboard': chess_match.fen(), 'turn': 'white' if chess_match.turn else 'black',
            'white_timer': str(datetime.timedelta(seconds=self.match_query.timer_white_player))[-5:],
            'black_timer': str(datetime.timedelta(seconds=self.match_query.timer_black_player))[-5:]
            }))
        await self.send(text_data=json.dumps({'message':'','type':'pieces_capture_update',

            'captured_white': self.match_query.this_chessboard['pieces_captured']['white_captured'],
            'captured_black' : self.match_query.this_chessboard['pieces_captured']['black_captured']
    
            }))