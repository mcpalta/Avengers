from django.urls import path
from . import views

app_name = 'comics'

urlpatterns = [
    path('', views.comic_list, name='list'),
]
