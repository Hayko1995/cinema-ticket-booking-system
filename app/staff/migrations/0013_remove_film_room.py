# Generated by Django 4.1.3 on 2024-08-21 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0012_remove_film_movie_genre_remove_film_movie_lang_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='room',
        ),
    ]
