from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from Authentication.models import AuthenticationTokenTime
from os import path
import json
from channels.layers import get_channel_layer
from django.conf import settings
import logging

logging.basicConfig(filename='Chess_Lobbies/debug.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s: ')

class ChessBoardCustomer(WebsocketConsumer):
    
    def connect(self):
        # Connect the client to the group
        self.accept()
        self.session = self.scope['session']

        if self.scope["user"].is_authenticated: 
            print(self.scope.get('rT7gM2sP5qW8jN4'))
            if True:
                data = AuthenticationTokenTime.objects.get(pk=self.session.get('rT7gM2sP5qW8jN4'))
                if data.valid_session: # Match token I need to add here
                     #verify credentials before to accept the coneection 
                    match_info = {
                        'ID_match':'',
                        'white': '',
                        'black': '',
                        'move':'',
                    }

                    if not path.exists('Chess_Lobbies/lobby1/match.json'):
                        with open('Chess_Lobbies/lobby1/match.json', 'w') as match:
                            match_info['white'] = data.username
                            match_info['ID_match'] = '253434'
                            rw =  json.dump(match_info, match)
                            self.group_name = match_info['ID_match']
                    else:
                        with open('Chess_Lobbies/lobby1/match.json', 'r+') as match:
                            rw = json.load(match)
                            if rw['white'] == '':
                                rw['white'] = data.username
                                rw['ID_match'] = '253434'
                            else:
                                rw['black'] = data.username
                            self.group_name = rw['ID_match']

                        with open('Chess_Lobbies/lobby1/match.json', 'w') as match_update:
                            json.dump(rw, match_update)
                                

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

        if 'type' in data:
            print(data['turn'])
            if data['turn'] == 'white':
                data['response'] = '32523caacfbc25d536b7e7ccbc7e3e97baf4b9e38fc43d229de3da54c36e7a4b'
            else:
                data['response'] = 'dc724af18fbdd4e59189f5fe768a5f8311527050d9b8a52c989f6e7f085e8b90'
        if 'response' in data:
                logging.debug(data)

        self.send(text_data=json.dumps({
            'message': data
        }))
