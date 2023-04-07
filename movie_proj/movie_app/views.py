from django.shortcuts import render
from .models import Movie


# Create your views here.

def show_all_movie(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/all_movies.html', {'movies': movies})


def show_one_movie(request, slug_movie: str):
    movie = Movie.objects.get(slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {'movie': movie})
