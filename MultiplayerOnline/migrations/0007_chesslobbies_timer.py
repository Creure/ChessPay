# Generated by Django 4.0.1 on 2024-09-08 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MultiplayerOnline', '0006_division_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chesslobbies',
            name='timer',
            field=models.PositiveIntegerField(default=10),
        ),
    ]