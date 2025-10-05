from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('', views.char_list, name='list'),
]

