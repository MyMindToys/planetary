from django.contrib import admin
from .models import Image, MenuCard


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'alt_text')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(MenuCard)
class MenuCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'link', 'image')
    list_editable = ('order',)
    ordering = ('order',)
    readonly_fields = ('created_at', 'updated_at')
