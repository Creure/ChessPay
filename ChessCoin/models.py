import uuid
from django.db import models
from Authentication.models import User
from django.core.validators import MinValueValidator


class ChessCoin_Transaccions(models.Model):
    id = models.CharField(primary_key=True, max_length=50, editable=False)
    white_player = models.CharField(max_length=100, blank=True,)
    black_player = models.CharField(max_length=100 , blank=True)
    game_status = models.CharField(max_length=20, default='None')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    ended_at = models.DateTimeField(null=True)
    this_chessboard = models.JSONField(default=dict)
    winning_player = models.CharField(max_length=100, blank=True, null=True, default='N/A')
    timer_black_player = models.PositiveIntegerField(default=10)
    timer_white_player = models.PositiveIntegerField(default=10)
    timer = models.PositiveIntegerField(default=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaccion_status = models.BooleanField(default=False) 
    lobby_wallet = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    fee_match_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    validation_message = models.CharField(max_length=100, blank=True,)
    def __str__(self):
        return f"ChessCoin_Transaccions {self.id}"