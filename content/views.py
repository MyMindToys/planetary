from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import MenuCard, Film, Genre, FilmCategory, FilmContentType


def api_catalog_filters(request):
    """JSON: списки значений для фильтров каталога из моделей (категории, жанры, типы контента)."""
    return JsonResponse({
        'categories': [c.name for c in FilmCategory.objects.all()],
        'genres': [g.name for g in Genre.objects.all()],
        'content_types': [t.name for t in FilmContentType.objects.all()],
    })


def api_films(request):
    """JSON: список фильмов для каталога (id, название, описание, возраст от/до, жанры, категории, обложка)."""
    films = []
    for f in Film.objects.all():
        films.append({
            'id': f.pk,
            'title': f.title,
            'description': f.description,
            'duration_minutes': f.duration_minutes,
            'age_rating_min': f.age_rating_min,
            'age_rating_max': f.age_rating_max,
            'genres': [g.name for g in f.genres.all()],
            'categories': [c.name for c in f.categories.all()],
            'content_types': [t.name for t in f.content_types.all()],
            'is_new': f.is_new,
            'cover': f.cover.url if f.cover else None,
        })
    return JsonResponse({'films': films})


def api_film_detail(request, pk):
    """JSON: один фильм по id (вся информация)."""
    f = get_object_or_404(Film, pk=pk)
    return JsonResponse({
        'id': f.pk,
        'title': f.title,
        'description': f.description,
        'duration_minutes': f.duration_minutes,
        'age_rating_min': f.age_rating_min,
        'age_rating_max': f.age_rating_max,
        'genres': [g.name for g in f.genres.all()],
        'categories': [c.name for c in f.categories.all()],
        'content_types': [t.name for t in f.content_types.all()],
        'is_new': f.is_new,
        'cover': f.cover.url if f.cover else None,
    })


def api_menu_cards(request):
    """JSON: карточки меню для главной (название, картинка, ссылка)."""
    cards = []
    for card in MenuCard.objects.all()[:4]:
        cards.append({
            'title': card.title,
            'image': card.image.url if card.image else None,
            'link': card.link or '#',
        })
    return JsonResponse({'cards': cards})


def index(request):
    """Главная."""
    return render(request, 'content/index.html')


def catalog(request):
    """Каталог фильмов — статичный контент."""
    return render(request, 'content/catalog.html')


def news(request):
    """Новости — статичный контент."""
    return render(request, 'content/news.html')


def zayavka(request):
    """Оставить заявку — статичная форма."""
    return render(request, 'content/zayavka.html')
