from django.contrib import admin
from .models import Comic
from django.utils.html import format_html

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue_number', 'img_tag', 'created', 'updated')

    def img_tag(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="50" />', obj.img.url)
        return "-"
    img_tag.short_description = 'Imagen'
