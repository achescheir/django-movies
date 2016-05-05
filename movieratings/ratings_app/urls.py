from django.conf.urls import url

from . import views

app_name = "ratings_app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movie(?P<id>[0-9]+)/', views.movie_detail_view, name="movie_detail_url"),
    url(r'^user(?P<id>[0-9]+)/', views.rater_detail, name="rater_detail"),
    ]
