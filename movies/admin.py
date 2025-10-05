from django.contrib import admin
from .models import Movie
from django.utils.html import format_html

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'poster_tag', 'release_date', 'created', 'updated')

    def poster_tag(self, obj):
        if obj.poster:
            return format_html('<img src="{}" width="50" />', obj.poster.url)
        return "-"
    poster_tag.short_description = 'Poster'
