# Generated by Django 4.2.6 on 2024-05-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_movie_casting_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_details',
            name='cast_members',
            field=models.ManyToManyField(related_name='movies', to='base.movie_casting'),
        ),
    ]
