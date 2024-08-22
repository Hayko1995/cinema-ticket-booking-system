# Generated by Django 4.1.3 on 2024-03-17 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_film_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='room',
        ),
        migrations.AlterField(
            model_name='film',
            name='room',
            field=models.CharField(choices=[('BLUE', 'Blue'), ('RED', 'Red'), ('GREEN', 'Green')], default='BLUE', max_length=100, verbose_name='Room'),
        ),
        migrations.AlterField(
            model_name='show',
            name='showtime',
            field=models.TimeField(default=datetime.time(12, 29, 55, 369110), verbose_name='Showtime'),
        ),
    ]
