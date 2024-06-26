# Generated by Django 4.2.6 on 2024-03-24 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_casting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast_image', models.FileField(default=None, max_length=300, null=True, upload_to='cast_images/')),
                ('cast_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('poster', models.FileField(default=None, max_length=300, null=True, upload_to='movie_posters/')),
                ('genre', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('runtime', models.CharField(max_length=20)),
                ('rating', models.CharField(max_length=20)),
                ('director', models.CharField(max_length=50)),
                ('actors', models.CharField(max_length=100)),
                ('story', models.CharField(max_length=500)),
            ],
        ),
    ]
