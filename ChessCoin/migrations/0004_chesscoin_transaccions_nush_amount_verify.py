# Generated by Django 5.1 on 2024-09-23 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChessCoin', '0003_alter_chesscoin_transaccions_fee_match_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='chesscoin_transaccions',
            name='nush_amount_verify',
            field=models.JSONField(default=dict),
        ),
    ]