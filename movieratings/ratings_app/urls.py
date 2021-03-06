from django.conf.urls import url, include

from . import views

app_name = "ratings_app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movie(?P<id>[0-9]+)/add_rating/', views.add_rating, name="rate_movie"),
    url(r'^movie(?P<id>[0-9]+)/', views.movie_detail_view, name="movie_detail_url"),
    url(r'^user(?P<id>[0-9]+)/', views.rater_detail, name="rater_detail"),
    url(r'^top(?P<num>[0-9]+)/', views.Top_Movies.as_view(), name="top_movies"),
    url(r'^genre/(?P<genre>[A-Za-z]+)/', views.top_genre, name="top_genre"),
    url(r'^profile/', views.profile, name="profile"),
    url(r'^', include('django.contrib.auth.urls'))
    ]
