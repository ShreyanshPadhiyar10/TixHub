from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from base.models import Movie_details

# Create your views here.

def home(request):
    movie_det = Movie_details.objects.all()
    data = { 'movie_det' : movie_det }
    
    return render(request, "index.html", data)


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("base:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form" : form})
