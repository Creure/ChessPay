import uuid
from django.db import models

class ChessGame(models.Model):
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4, editable=False)
    white_player = models.CharField(max_length=100)
    black_player = models.CharField(max_length=100)
    game_status = models.CharField(max_length=20, default='pending')  # 'pending', 'cancel', 'finish'
    move_history = models.JSONField(default=list)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    result = models.CharField(max_length=10, null=True, blank=True)
    tokens = models.JSONField(default=dict)  # {'token_white': 'token_value', 'token_black': 'token_value'}

    def __str__(self):
        return f"{self.white_player} vs {self.black_player}"
