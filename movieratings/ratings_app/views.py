from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect
from datetime import datetime
from .models import Movie, Rating, Rater
from django.core.urlresolvers import reverse
from .forms import RatingForm


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

def add_rating(request, id):
    movie = get_object_or_404(Movie, pk=id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rater = request.user.rater
            if len(Rating.objects.filter(movie=movie).filter(rater=rater)) == 0:
                new_rating = Rating(movie=movie, rater=rater,rating_value=form.cleaned_data['rating_value'],review=form.cleaned_data['review'])
                new_rating.save()
            else:
                old_rating = Rating.objects.filter(movie=movie).get(rater=rater)
                old_rating.rating_value = form.cleaned_data['rating_value']
                old_rating.review = form.cleaned_data['review']
                old_rating.save()
            return HttpResponseRedirect(reverse('ratings_app:rater_detail', args=(request.user.id,)))
        else:
            return HttpResponse('Invalid data')
    else:
        form = RatingForm()
        return render(request, 'raters/add_rating.html', {'form':form})

def profile(request):
    return render(request, 'accounts/profile.html')

def parse_genre(genre):
    genre = genre.lower()
    genre_dict =  {'unknown'     : 'unknown',
                    'action'     : "Action",
                    'adventure'  : "Adventure",
                    'animation'  : "Animation",
                    'childrens'  : "Children's",
                    'comedy'     : "Comedy",
                    'crime'      : "Crime",
                    'documentary': "Documentary",
                    'drama'      : "Drama",
                    "fantasy"    : "Fantasy",
                    "filmnoir"   : "Film-Noir",
                    "horror"     : "Horror",
                    "musical"    : "Musical",
                    "mystery"    : "Mystery",
                    "romance"    : "Romance",
                    "scifi"      : "Sci-Fi",
                    "thriller"   : "Thriller",
                    "war"        : "War",
                    "western"    : "Western"
                    }
    return genre_dict[genre]

def top_genre(request, genre):
    genre = parse_genre(genre)
    movie_list = Movie.get_top_genre_movies(genre, 25)
    return render(request, 'movies/top_movies.html', {'movie_list': movie_list})
