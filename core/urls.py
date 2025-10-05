from django.urls import path
from core import views as view_core

app_name = "core"

urlpatterns = [
    path('', view_core.home, name="home")

]
