from django.shortcuts import render
from django.shortcuts import get_object_or_404
from base.models import Movie_details

def home(req):
    return render(req, "index.html")


def more_details(request):
    # movie_det = Movie_details.objects.all()
    # data = { 'movie_det' : movie_det }

    movie_title = request.GET.get('movie_title')
    movie = get_object_or_404(Movie_details, title = movie_title)

    
    return render(request, 'more.html', {'movie' : movie})

