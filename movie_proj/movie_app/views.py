from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor


# Create your views here.

def show_all_movie(request):
    movies = Movie.objects.order_by('name')
    return render(request, 'movie_app/all_movies.html', {'movies': movies})


def show_one_movie(request, slug_movie: str):
    movie = Movie.objects.get(slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {'movie': movie})


def ddirectors(request):
    directors = Director.objects.all()
    for dir in directors:
        dir.save()
    return render(request, 'movie_app/director.html', {'directors': directors})


def name_director(request, slug_name: str):
    name_dir = get_object_or_404(Director, slug=slug_name)
    return render(request, 'movie_app/info_dir.html', {'name_dir': name_dir})


def info_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/actors.html', {'actors':actors})


def info_actor(request, id_act: int):
    actor = get_object_or_404(Actor, id=id_act)
    return render(request, 'movie_app/actor.html', {'actor':actor})
