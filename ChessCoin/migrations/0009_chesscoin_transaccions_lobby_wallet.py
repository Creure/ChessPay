# Generated by Django 5.1 on 2024-11-03 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChessCoin', '0008_alter_chesscoin_transaccions_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chesscoin_transaccions',
            name='lobby_wallet',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]