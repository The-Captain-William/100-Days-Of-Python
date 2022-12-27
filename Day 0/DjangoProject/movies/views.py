from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):  # index = main page
    # Movie.objects.all()  # SELECT * FROM movies_movie
    # Movie.objects.filter(release_year=1985)  # SELECT * FROM movies_movie WHERE
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    return render(request, 'index.html', {'movies': movies})