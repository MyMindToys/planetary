from django.shortcuts import render


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
