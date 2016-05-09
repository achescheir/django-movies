# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 21:01
from __future__ import unicode_literals
import csv
from django.db import migrations

def make_genre_string(genres_present):
    genre_names = ["unknown", "Action", "Adventure", "Animation",
                   "Children's", "Comedy", "Crime", "Documentary",
                   "Drama", "Fantasy", "Film-Noir", "Horror", "Musical",
                   "Mystery", "Romance", "Sci-Fi", "Thriller", "War",
                   "Western"]
    genre_list = []
    for genre_name, present in zip(genre_names,genres_present):
        if present == '1':
            genre_list.append(genre_name)
    return "|".join(genre_list)

def func(apps, schema_editor):
        Movie = apps.get_model("ratings_app", "Movie")
        with open('../ml-100k/u.item','r',encoding='latin-1') as data_file:
            fields = ["movieId", "title", "release_date",
                      "video_release_date", "imdb_url"]
            reader = csv.DictReader(data_file, delimiter="|", fieldnames=fields, restkey='genres')
            for each_movie in reader:
                mid = each_movie['movieId']
                genre_string = make_genre_string(each_movie['genres'])
                try:
                    old_movie = Movie.objects.get(id=mid)
                    old_movie.genres = genre_string
                    old_movie.save()
                except Exception as e:
                    print(each_movie)
                    raise(e)




class Migration(migrations.Migration):

    dependencies = [
        ('ratings_app', '0004_rating_review'),
    ]

    operations = [
    migrations.RunPython(func)
    ]
