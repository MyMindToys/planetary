from django.contrib import admin
from .models import Image, MenuCard, Genre, FilmCategory, FilmContentType, Film


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(FilmCategory)
class FilmCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(FilmContentType)
class FilmContentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration_minutes', 'age_rating_min', 'age_rating_max')
    list_filter = ('genres', 'categories', 'content_types')
    search_fields = ('title', 'description')
    filter_horizontal = ('genres', 'categories', 'content_types')
    readonly_fields = ('created_at', 'updated_at')


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
