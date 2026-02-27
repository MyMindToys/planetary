from django.contrib import admin
from .models import Image, MenuCard, Genre, FilmCategory, FilmContentType, Film, News, NewsImage


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
    list_display = ('title', 'is_new', 'duration_minutes', 'age_rating_min', 'age_rating_max')
    list_editable = ('is_new',)
    list_filter = ('genres', 'categories', 'content_types', 'is_new')
    search_fields = ('title', 'description')
    filter_horizontal = ('genres', 'categories', 'content_types')
    readonly_fields = ('created_at', 'updated_at')


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 0
    ordering = ('order',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    list_filter = ('date',)
    search_fields = ('title', 'excerpt', 'body')
    date_hierarchy = 'date'
    inlines = [NewsImageInline]
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
