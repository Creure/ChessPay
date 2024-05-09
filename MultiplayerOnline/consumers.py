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

logging.basicConfig(filename='debug.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s: ')


class ChessBoardCustomer(WebsocketConsumer):
    
    def connect(self):
        # Connect the client to the group
        self.session = self.scope['session']
        
        if self.scope["user"].is_authenticated: 
            
            try:
                data = AuthenticationTokenTime.objects.get(pk=self.session.get('rT7gM2sP5qW8jN4'))
                if data.valid_session: # Match token I need to add here
                     #verify credentials before to accept the coneection 
                    self.group_name =  self.session.get('chess_match')

                      # Replace 'group_name' with the name of your group
                    async_to_sync(self.channel_layer.group_add)(
                        self.group_name,
                        self.channel_name
                    )
                    self.accept()

                    self.send(text_data=json.dumps({'message': 'OK'}))  
            except Exception as e:
                logging.error(str(e))
               #debugging the error          
        else:
            logging.error("Not authenticated")
            
       
        
    def disconnect(self, close_code):
        # Disconnect the client from the group
        try:
            async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
            )
        except:
            pass

    def receive(self, text_data):
        # Receive a message from the client
        # Parse the received JSON message
        data = json.loads(text_data)
        message = data['data']

        # Send the message to all clients in the group
        logging.debug(message)
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'node',
                'message': message
            }
        )

    def node(self, event):
        game = get_object_or_404(ChessLobbies, pk= self.session.get('chess_match'))
    
        # Modifica el campo this_chessboard
        if 'board' in json.dumps({'message':event['message']}):
            game.this_chessboard =json.dumps({'message':event['message']['board']})   # Modifica según sea necesario
        
        # Guarda los cambios
        game.save()
        self.send(text_data=json.dumps({'message':event['message']}))

