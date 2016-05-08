from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Movie, Rating, Rater
from datetime import datetime


# Create your views here.
def index(request):
    return HttpResponse("This is the index of ratings_app.")

def movie_detail_view(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'movies/detail.html', {'movie': movie})

def rater_detail(request, id):
    rater = get_object_or_404(Rater, pk=id)
    return render(request, 'raters/detail.html', {'rater': rater})

def top_movies(request, num):
    movie_list = Movie.get_top_movies(num)
    return render(request, 'movies/top_movies.html', {'movie_list': movie_list})

def profile(request):
    return render(request, 'accounts/profile.html')

def add_rating(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'raters/add_rating.html', {'movie': movie,"ratingchoices":[1,2,3,4,5]})

def update(request, id):
    movie = Movie.objects.get(id=id)
    rater = Rater.objects.get(id=request.POST['rater'])
    rating_value = request.POST['rating']
    if len(Rating.objects.filter(movie=movie).filter(rater=rater)) == 0:
        new_rating = Rating(movie=movie, rater=rater,rating_value=rating_value,time=datetime.now())
        new_rating.save()
    else:
        old_rating = Rating.objects.filter(movie=movie).get(rater=rater)
        old_rating.rating_value = rating_value
        old_rating.time = datetime.now()
        old_rating.save()
    return HttpResponseRedirect(reverse('ratings_app:rater_detail', args=(rater.id,)))
