from django.contrib import admin
from base.models import Movie_casting
from base.models import Movie_details

# Register your models here.
class cast_admin(admin.ModelAdmin):
    list_display = ('cast_name', 'cast_image')
    
admin.site.register(Movie_casting, cast_admin)

class Movie_admin(admin.ModelAdmin):
    list_display = ('title', 'poster', 'genre', 'year', 'runtime', 'rating', 'director', 'actors', 'story')
    
admin.site.register(Movie_details, Movie_admin)