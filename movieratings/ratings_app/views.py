from django.shortcuts import HttpResponse, render, get_object_or_404
from .models import Movie, Rating, Rater



# Create your views here.
def index(request):
    return HttpResponse("This is the index of ratings_app.")

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
