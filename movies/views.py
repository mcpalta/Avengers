from django.shortcuts import render
from .models import Movie
from django.core.paginator import Paginator

def movie_list(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)  # Sobrescribe la variable
    return render(request, 'movies/movie_list.html', {'movies': movies})
