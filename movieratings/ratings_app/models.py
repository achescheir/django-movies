from django.db import models
import csv
from datetime import datetime


# Create your models here.
class Movie(models.Model):
    movie_id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=320)
    genres = models.CharField(max_length=320)


    def __str__(self):
        return self.title


    @staticmethod
    def read(data_file_name):
        with open(data_file_name,'r') as data_file:
            reader = csv.DictReader(data_file)
            for each_movie in reader:
                new_movie = Movie(movie_id=each_movie['movieId'], title=each_movie['title'], genres=each_movie['genres'])
                new_movie.save()

class Rating(models.Model):
    movie_id = models.ForeignKey("Movie")
    rating_value = models.FloatField()
    rater_id = models.ForeignKey("Rater")
    time = models.DateTimeField()


    def __str__(self):
        return "Movie:{}-User:{}-Rating:{}".format(self.movie_id, self.rater_id, self.rating_value)


    @staticmethod
    def read(data_file_name):
        with open(data_file_name,'r') as data_file:
            reader = csv.DictReader(data_file)
            for each_rating in reader:
                new_rater = Rater(rater_id=each_rating['userId'])
                new_rater.save()
                mid = Movie.objects.get(movie_id=each_rating['movieId'])
                rid = new_rater#each_rating['userId']
                rv = each_rating['rating']
                ts = datetime.fromtimestamp(float(each_rating['timestamp']))
                new_rating = Rating(movie_id=mid, rater_id=rid, rating_value=rv,time=ts)
                new_rating.save()

class Rater(models.Model):
    rater_id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return rater_id
