from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from Authentication.models import AuthenticationTokenTime
from os import path
import json
from channels.layers import get_channel_layer
from django.conf import settings
import logging
from django.shortcuts import get_object_or_404
from MultiplayerOnline.models import ChessGame, ChessLobbies
import chess, pdb

logging.basicConfig(filename='debug.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s: ')


class ChessBoardCustomer(WebsocketConsumer):
    
    def connect(self):
        
        # Connect the client to the group
        

        if self.scope["user"].is_authenticated: 
            
            try:
                csrf_token = self.scope['session'].get('rT7gM2sP5qW8jN4')
                data = AuthenticationTokenTime.objects.get(pk=csrf_token)
                if data.valid_session: 
                    # Match token I need to add here
                     #verify credentials before to accept the coneection 
                    self.match_query = get_object_or_404(ChessLobbies, pk= self.scope['session'].get('chess_match'))
                    self.group_name =  self.scope['session'].get('chess_match')
                    
                        # Replace 'group_name' with the name of your group
                    async_to_sync(self.channel_layer.group_add)(
                        self.group_name,
                        self.channel_name
                    )
                   

                    if self.match_query.game_status == 'completed':
                        
                        self.chess_match = {
                        self.scope['session'].get('chess_match'):chess.Board()
                        }
                    
                        
                    elif self.match_query.game_status == 'playing':
                        self.chess_match = {
                        self.scope['session'].get('chess_match'):chess.Board(self.match_query.this_chessboard['board_fen'])
                        }
                    else:
                        pass

                    if self.chess_match[self.scope['session'].get('chess_match')].turn:
                        turn = 'black'
                    else:
                        turn = 'white'

                    self.chess_match['white'] = [self.match_query.white_player, 'cookie']
                    self.chess_match['black'] = [self.match_query.black_player, 'cookie']
                    self.chess_match['status'] = self.match_query.game_status
                    self.accept()


                    self.send(text_data=json.dumps({'message':'updated_chessboard','type':'', 'chessboard': self.chess_match[self.scope['session'].get('chess_match')].fen(), 'turn': turn })) #updating the Chess_board
                    
            except Exception as e:
                logging.error('sorry an error has ocurred: '+ str(e))
               #debugging the error          
        else:
            logging.error("Not authenticated")
            self.close()
            
       
        
    def disconnect(self, close_code):
        # Disconnect the client from the group
        self.group_name = 'Disconnecting'
        try:
            async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
            )
        except Exception as e:
            logging.error(f'Error: {e}')

    def receive(self, text_data):
        # Receive a message from the client
        # Parse the received JSON message
        data = json.loads(text_data)
        
        

        # Send the data to all clients in the group
        logging.debug(data['data'])
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'node',
                'data': data['data']
            }
        )

    def node(self, event):
        logging.debug(f'obj self.chess_match: {self.chess_match}')
        # Modifica el campo this_chessboard
        chess_match = self.chess_match[self.scope['session'].get('chess_match')]
        if chess_match.turn:
            turn = 'white'
        else:
            turn = 'black'

        message = ''
        if event["data"]['type'] == 'legal_moves' :
            position = chess.parse_square(event['data']['position']) 
            legal_moves = chess_match.legal_moves
            legal_moves_pieces = [move for move in legal_moves if move.from_square == position]
            data = []
            #if legal_moves_pieces == []:
            #    pdb.set_trace()
            for move in legal_moves_pieces:
                data.append(move.uci())

            logging.debug(f'legal_moves:{event['data']['position']}: {data}')
            logging.debug(f"event img_id: {event['data']}")
            self.send(text_data=json.dumps({'message':'','type':'legal_moves','legal_moves':data, 'position':event['data']['position'], 'img_id': event['data']['img_id'], 'turn': turn })) 

        if  event["data"]['type'] == 'do_the_move':
            chess_match.push(chess.Move.from_uci(event["data"]['move']))
            piece = chess_match.piece_type_at(chess.parse_square(event["data"]['move'][-2:]))
            if chess_match.turn:
                turn = 'black'
            else:
                turn = 'white'

            if chess_match.is_game_over():
                if chess_match.is_checkmate():
                    message = "¡Jaque mate!"
                elif chess_match.is_stalemate():
                    message = "¡Ahogado!"
                elif chess_match.is_insufficient_material():
                    message = "Insuficiencia de material"
                elif chess_match.is_seventyfive_moves():
                    message = "Regla de los 50 movimientos"
                else:
                    message = "Fin de la partida por otros motivos"
            
            
            if self.match_query.game_status == 'completed':
                self.match_query.game_status = 'playing'
            self.match_query.this_chessboard = {
                'board_fen': self.chess_match[self.scope['session'].get('chess_match')].fen(),
                'moves':[move.uci() for move in chess_match.move_stack]
            }
            
            self.match_query.save()

            # {
            #   'board_fen': ''rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR';'
            #   'moves': ['a2','c2.....]
            #}
            self.send(text_data=json.dumps({'message':message,'type':'updated', 'turn': turn, 'move': event["data"]['move'][-2:],
             'position':event["data"]['position'],'turn': turn,
             'img_id': event['data']['img_id']})) 
            
        
        
        if chess_match.is_checkmate():
            self.send(text_data=json.dumps({'message':'','type':'checkmate'})) 
            
        