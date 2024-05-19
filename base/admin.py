from django.contrib import admin
from base.models import Movie_casting
from base.models import Movie_details
from .models import *

# Register your models here.

class Movie_admin(admin.ModelAdmin):
    list_display = ('title', 'poster', 'genre', 'year', 'runtime', 'rating', 'director', 'actors', 'story', 'cast_members_display')
    
admin.site.register(Movie_details, Movie_admin)

class cast_admin(admin.ModelAdmin):
    list_display = ('cast_name', 'cast_image')
    
admin.site.register(Movie_casting, cast_admin)