from django.shortcuts import render
from django.http import JsonResponse
from .models import MenuCard


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
