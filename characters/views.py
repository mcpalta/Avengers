from django.shortcuts import render
from .models import Character
from django.core.paginator import Paginator

def char_list(request):
    characters = Character.objects.all()
    paginator = Paginator(characters, 10)  # 10 por página
    page_number = request.GET.get('page')
    characters = paginator.get_page(page_number)
    return render(request, 'characters/char_list.html', {'characters': characters})

