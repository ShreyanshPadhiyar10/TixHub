# Generated by Django 4.2.6 on 2024-05-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_movie_details_full_story'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theatre_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theatre_name', models.CharField(max_length=50)),
                ('theatre_address', models.CharField(max_length=100)),
            ],
        ),
    ]
