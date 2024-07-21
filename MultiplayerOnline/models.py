import uuid
from django.db import models



class ChessLobbies(models.Model):
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4, editable=False)
    white_player = models.CharField(max_length=100)
    black_player = models.CharField(max_length=100, default='')
    game_status = models.CharField(max_length=20, default='pending')
    game_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    this_chessboard = models.JSONField(default=dict)
    def __str__(self):
        return f"Chess Lobby {self.id}"

class ChessGame(models.Model):
    ChessLobbies_id = models.ForeignKey(ChessLobbies, on_delete=models.CASCADE, null=True)
    white_player = models.CharField(max_length=100)
    black_player = models.CharField(max_length=100)
    game_status = models.CharField(max_length=20, default='pending')  # 'pending', 'cancel', 'Check Mate'
    move_history = models.JSONField(default=list)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    result = models.CharField(max_length=10, null=True, blank=True)
    config = models.JSONField(blank=True)
    def __str__(self):
        return f"{self.white_player} vs {self.black_player}"