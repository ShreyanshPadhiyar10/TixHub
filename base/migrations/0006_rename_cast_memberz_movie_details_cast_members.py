# Generated by Django 4.2.6 on 2024-05-18 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_movie_details_cast_members_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie_details',
            old_name='cast_memberz',
            new_name='cast_members',
        ),
    ]