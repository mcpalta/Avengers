from django.shortcuts import render
from movies.models import Movie
from characters.models import Character
from comics.models import Comic

def home(request):
    movie_list = Movie.objects.all()[:10]        # Limitar 10 registros
    char_list = Character.objects.all()[:10]
    comic_list = Comic.objects.all()[:10]
    return render(request, "core/home.html", {
        'movie_list': movie_list,
        'char_list': char_list,
        'comic_list': comic_list,
    })
