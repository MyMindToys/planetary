from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import MenuCard, Film, Genre, FilmCategory, FilmContentType, News, BannerImage


def api_catalog_filters(request):
    """JSON: списки значений для фильтров каталога из моделей (категории, жанры, типы контента)."""
    return JsonResponse({
        'categories': [c.name for c in FilmCategory.objects.all()],
        'genres': [g.name for g in Genre.objects.all()],
        'content_types': [t.name for t in FilmContentType.objects.all()],
    })


def api_films(request):
    """JSON: список фильмов для каталога с пагинацией и фильтрацией (по 16 на странице)."""
    page = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 16))
    
    queryset = Film.objects.all()
    
    # Фильтры
    categories = request.GET.getlist('categories')
    genres = request.GET.getlist('genres')
    content_types = request.GET.getlist('content_types')
    age_min = request.GET.get('age_min')
    age_max = request.GET.get('age_max')
    
    if categories:
        queryset = queryset.filter(categories__name__in=categories).distinct()
    if genres:
        queryset = queryset.filter(genres__name__in=genres).distinct()
    if content_types:
        queryset = queryset.filter(content_types__name__in=content_types).distinct()
    if age_min:
        queryset = queryset.filter(age_rating_max__gte=int(age_min))
    if age_max:
        queryset = queryset.filter(age_rating_min__lte=int(age_max))
    
    total = queryset.count()
    
    start = (page - 1) * page_size
    end = start + page_size
    
    films = []
    for f in queryset[start:end]:
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
    
    return JsonResponse({
        'films': films,
        'total': total,
        'page': page,
        'page_size': page_size,
        'total_pages': (total + page_size - 1) // page_size if total > 0 else 0,
    })


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


def api_news_list(request):
    """JSON: список новостей (id, заголовок, дата, краткий текст)."""
    items = []
    for n in News.objects.all():
        items.append({
            'id': n.pk,
            'title': n.title,
            'date': n.date.isoformat(),
            'excerpt': n.excerpt,
        })
    return JsonResponse({'news': items})


def api_news_detail(request, pk):
    """JSON: одна новость по id (полный текст + галерея)."""
    n = get_object_or_404(News, pk=pk)
    gallery = [{'url': img.image.url, 'caption': img.caption} for img in n.gallery.all()]
    return JsonResponse({
        'id': n.pk,
        'title': n.title,
        'date': n.date.isoformat(),
        'excerpt': n.excerpt,
        'body': n.body,
        'gallery': gallery,
    })


def api_banners(request):
    """JSON: активные баннеры для карусели (только с is_active=True)."""
    banners = []
    for b in BannerImage.objects.filter(is_active=True):
        banners.append({
            'id': b.pk,
            'image': b.image.url,
        })
    return JsonResponse({'banners': banners})


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
