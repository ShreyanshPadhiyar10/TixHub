from django.shortcuts import render
from django.shortcuts import get_object_or_404
from base.models import Movie_details, Theatre_details
from django.contrib.auth.decorators import login_required

def home(req):
    return render(req, "index.html")

def more_details(request):
    movie_id = request.GET.get('id')
    movie = get_object_or_404(Movie_details, id = movie_id)
    
    return render(request, 'more.html', {'movie' : movie})

@login_required
def ticket_booking(request):
    movie_id = request.GET.get('id')
    movie = get_object_or_404(Movie_details, id = movie_id)
    
    theatre = Theatre_details.objects.all()
    
    return render(request, 'Bookings/ticket_booking.html', {'movie' : movie, 'theatre' : theatre})
