import uuid
from django.db import models



class ChessLobbies(models.Model):
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4, editable=False)
    white_player = models.CharField(max_length=100, blank=True)
    black_player = models.CharField(max_length=100 , blank=True)
    game_status = models.CharField(max_length=20, default='pending')
    game_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    this_chessboard = models.JSONField(default=dict)
    bet_amount = models.DecimalField(max_digits=12, decimal_places=2, default=1.00)
    winning_player = models.CharField(max_length=100, blank=True, null=True)
    timer = models.PositiveIntegerField(default=10)
    def __str__(self):
        return f"Chess Lobby {self.id}"
