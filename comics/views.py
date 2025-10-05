from django.shortcuts import render
from .models import Comic
from django.core.paginator import Paginator

def comic_list(request):
    comics = Comic.objects.all()
    paginator = Paginator(comics, 10)  # 10 por página
    page_number = request.GET.get('page')
    comics = paginator.get_page(page_number)
    return render(request, 'comics/comic_list.html', {'comics': comics})
