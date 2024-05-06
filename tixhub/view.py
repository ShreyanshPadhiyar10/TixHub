from django.shortcuts import render

def home(req):
    return render(req, "index.html")


def more_details(request):
    movie_id = request.GET.get('movie_id')
    
    return render(request, 'more.html', {'movie_id': movie_id})

