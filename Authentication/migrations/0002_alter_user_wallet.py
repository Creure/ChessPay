# Generated by Django 5.1 on 2024-09-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wallet',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
