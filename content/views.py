from django.shortcuts import render


def index(request):
    """Главная — заглушка под бэк на шаблонах / точку входа для Vue."""
    return render(request, 'content/index.html')
