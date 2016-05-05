from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movie(?P<movie_id>[0-9]+)/$', views.movie_detail, name="movie_detail"),
    url(r'^user(?P<rater_id>[0-9]+)/$', views.rater_detail, name="rater_detail_view"),
    ]
