from django.contrib import admin
from .models import Genre, Movie
# Register your models here.

class GenreAdmin(admin.ModelAdmin): # (model + admin)
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin): # (model + admin)
    list_display = ('title', 'number_in_stock', 'daily_rate')

admin.site.register(Genre, GenreAdmin)  # register both Classes in interface
admin.site.register(Movie, MovieAdmin)