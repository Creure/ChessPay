import uuid
from django.db import models
from Authentication.models import User
from django.core.validators import MinValueValidator



class ChessLobbies(models.Model):
    id = models.CharField(primary_key=True, max_length=50, default=uuid.uuid4, editable=False)
    white_player = models.CharField(max_length=100, blank=True,)
    black_player = models.CharField(max_length=100 , blank=True)
    game_status = models.CharField(max_length=20, default='waiting')
    created_at = models.DateTimeField(auto_now_add=True)
    this_chessboard = models.JSONField(default=dict)
    winning_player = models.CharField(max_length=100, blank=True, null=True)
    timer_black_player = models.PositiveIntegerField(default=10)
    timer_white_player = models.PositiveIntegerField(default=10)
    timer = models.PositiveIntegerField(default=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    lobby_wallet = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f"Chess Lobby {self.id}"



class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    elo_rating = models.FloatField(default=1200, validators=[MinValueValidator(0)])  # Valor inicial típico para ELO
    games_played = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - Elo: {self.elo_rating}'

    def update_rating(self, opponent_rating, result):
        """
        Actualiza el Elo del jugador después de un juego.
        result: 1 si ganó, 0.5 si fue empate, 0 si perdió.
        opponent_rating: El Elo del oponente.
        """
        K = 32  # Constante de ajuste del Elo (puede ajustarse según el nivel de los jugadores)
        expected_score = 1 / (1 + 10 ** ((opponent_rating - self.elo_rating) / 400))
        new_rating = self.elo_rating + K * (result - expected_score)
        self.elo_rating = new_rating
        self.games_played += 1
        if result == 1:
            self.wins += 1
        elif result == 0.5:
            self.draws += 1
        else:
            self.losses += 1
        self.save()

class Game(models.Model):
    player_white = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='games_as_white')
    player_black = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='games_as_black')
    date = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=10, choices=[('1-0', 'White Wins'), ('0-1', 'Black Wins'), ('0.5-0.5', 'Draw')])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Actualizar los rankings de los jugadores después de guardar el resultado
        if self.result == '1-0':
            self.player_white.update_rating(self.player_black.elo_rating, 1)
            self.player_black.update_rating(self.player_white.elo_rating, 0)
        elif self.result == '0-1':
            self.player_white.update_rating(self.player_black.elo_rating, 0)
            self.player_black.update_rating(self.player_white.elo_rating, 1)
        else:  # Empate
            self.player_white.update_rating(self.player_black.elo_rating, 0.5)
            self.player_black.update_rating(self.player_white.elo_rating, 0.5)



class Division(models.Model):
    BRONCE = 'BR'
    PLATA = 'PL'
    ORO = 'OR'
    DIAMANTE = 'DI'
    MAESTRO = 'MA'
    GRAN_MAESTRO = 'GM'

    DIVISION_CHOICES = [
        (BRONCE, 'Bronce'),
        (PLATA, 'Plata'),
        (ORO, 'Oro'),
        (DIAMANTE, 'Diamante'),
        (MAESTRO, 'Maestro'),
        (GRAN_MAESTRO, 'Gran Maestro'),
    ]

    name = models.CharField(max_length=2, choices=DIVISION_CHOICES, default=BRONCE)

    def __str__(self):
        return self.get_name_display()

class PlayerRanking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def update_division(self):
        if self.points < 1000:
            self.division = Division.objects.get(name=Division.BRONCE)
        elif 1000 <= self.points < 3000:
            self.division = Division.objects.get(name=Division.PLATA)
        elif 3000 <= self.points < 5000:
            self.division = Division.objects.get(name=Division.ORO)
        elif 5000 <= self.points < 7000:
            self.division = Division.objects.get(name=Division.DIAMANTE)
        elif 7000 <= self.points < 9000:
            self.division = Division.objects.get(name=Division.MAESTRO)
        elif self.points >= 9000:
            self.division = Division.objects.get(name=Division.GRAN_MAESTRO)
        self.save()

    def __str__(self):
        return f'{self.user.username} - {self.division} ({self.points} pts)'