from json import loads, dumps
from channels.generic.websocket import WebsocketConsumer

class ChessBoardCustomer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = loads(text_data)
        message = text_data_json['data']

        self.send(text_data=dumps({
            'message': message
        }))