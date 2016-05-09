from django.db import models
from django.db.models import Avg, Count
from django.contrib.auth.models import User
import csv
from datetime import datetime, date
# from  .utilities import get_unassigned_user


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=256)
    release_date = models.DateField(null=True)
    video_release_date = models.DateField(null=True)
    imdb_url = models.CharField(max_length=512, blank=True)
    genres = models.CharField(max_length=256)


    def __str__(self):
        return self.title

    def get_average(self):
        avg = Rating.objects.filter(movie = self.id).aggregate(Avg('rating_value'))
        return avg['rating_value__avg']

    def get_ratings(self):
        return Rating.objects.filter(movie=self.id)

    @staticmethod
    def get_top_movies(number):
        sig_sample = Movie.objects.annotate(count = Count('rating')).filter(count__gt = 10)
        sorted_movies = sig_sample.annotate(avg_rating = Avg('rating__rating_value')).order_by('-avg_rating')
        return sorted_movies[:int(number)]


class Rating(models.Model):
    movie = models.ForeignKey("Movie")
    rating_value = models.PositiveIntegerField()
    rater = models.ForeignKey("Rater")
    time = models.DateTimeField(auto_now=True)
    review = models.TextField(blank=True)


    def __str__(self):
        return "Movie:{}-User:{}-Rating:{}".format(self.movie, self.rater, self.rating_value)


class Rater(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1)
    occupation = models.CharField(max_length=16)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return str(self.id)


    def get_ratings(self):
        return Rating.objects.filter(rater=self.id)
