from django.db import models

# Create your models here.
class Movie_casting(models.Model):
    cast_image = models.FileField(upload_to = 'cast_images/', max_length=300, null=True, default=None)
    cast_name = models.CharField(max_length=40)
    
class Movie_details(models.Model):
    title = models.CharField(max_length = 50)
    poster = models.FileField(upload_to='movie_posters/', max_length=300, null=True, default=None)
    genre = models.CharField(max_length = 50)
    year = models.IntegerField()
    runtime = models.CharField(max_length = 20)
    rating = models.CharField(max_length = 20)
    director = models.CharField(max_length = 50)
    actors = models.CharField(max_length = 100)
    story = models.CharField(max_length = 500)
    cast_members = models.ManyToManyField(Movie_casting, related_name='movies')
    
    def cast_members_display(self):
        return ', '.join(cast_member.cast_name for cast_member in self.cast_members.all())

    cast_members_display.short_description = 'Cast Members'
