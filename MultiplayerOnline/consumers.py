from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from Authentication.models import AuthenticationTokenTime
from os import path
import json
from channels.layers import get_channel_layer
from django.conf import settings
import logging
from MultiplayerOnline.models import ChessGame, ChessLobbies

logging.basicConfig(filename='debug.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s: ')

class ChessBoardCustomer(WebsocketConsumer):
    
    def connect(self):
        # Connect the client to the group
        self.accept()
        self.session = self.scope['session']

        if self.scope["user"].is_authenticated: 
            #print(self.scope.get('rT7gM2sP5qW8jN4'))
            if True:
                data = AuthenticationTokenTime.objects.get(pk=self.session.get('rT7gM2sP5qW8jN4'))
                if data.valid_session: # Match token I need to add here
                    id_match = self.session.get('chess_match')
                    self.group_name = id_match
                    lobby = ChessLobbies.objects.filter(id=id_match).first()
                    if lobby.game_data['white'][0] == self.session.get('rT7gM2sP5qW8jN4'):
                        self.channel_name = id_match +'_'+  lobby.game_data['white'][0][0:50]
                    elif lobby.game_data['black'][0] == self.session.get('rT7gM2sP5qW8jN4'):
                        self.channel_name = id_match +'_'+lobby.game_data['white'][0][0:50]
                    else:
                        pass
                     #verify credentials before to accept the coneection 
                   
                      # Replace 'group_name' with the name of your group
                    async_to_sync(self.channel_layer.group_add)(
                        self.group_name,
                        self.channel_name
                    )
                
                    self.send(text_data=json.dumps({'message': 'OK'}))  
            #except Exception as e:
            #   self.send(text_data=json.dumps({'message': str(e)})  ) #debug change this
               #debugging the error          
        else:
            self.send(text_data=json.dumps({'message': 'Not Auth'})) 
            self.close()

            
       
        
    def disconnect(self, close_code):
        # Disconnect the client from the group
        logging.error(close_code)

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
        logging.debug(f'WARNING: !!{message}')
        id_match = self.session.get('chess_match')
        lobby = ChessLobbies.objects.filter(id=id_match).first()
        if message['sender'] == lobby.game_data['black'][0]:
            msg_id_receiver = id_match +'_'+  lobby.game_data['white'][0][0:50]
        elif message['sender'] == lobby.game_data['white'][0]:
            msg_id_receiver = id_match +'_'+lobby.game_data['black'][0][0:50]
        else:
            pass


        # Send the message to all clients in the group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'send_group_message',
                'message': message
            }
        )

    def send_group_message(self, event):
        # Send a message to the client
        data = event['message']
        # Send the JSON message to the client via WebSocket
        print(self.scope['user'])
        if 'type' in data:
            if data['type'] == 'match':
                print(data['turn'])
                logging.error(data)
                if data['turn'] == 'white':
                    data['response'] = '32523caacfbc25d536b7e7ccbc7e3e97baf4b9e38fc43d229de3da54c36e7a4b'
                elif data['turn'] == 'black':
                    data['response'] = 'dc724af18fbdd4e59189f5fe768a5f8311527050d9b8a52c989f6e7f085e8b90'
                else:
                    pass
            logging.debug(data)

            self.send(text_data=json.dumps({
                'message': data
            }))


    