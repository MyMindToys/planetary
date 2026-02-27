"""
Отдача SPA (Vue) для деплоя на одном домене с Django.
"""
from pathlib import Path
from django.http import HttpResponse, Http404

BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = BASE_DIR / 'frontend' / 'dist' / 'index.html'


def spa_view(request):
    """Отдаёт index.html Vue для маршрутов SPA (/, /catalog, /news, /zayavka)."""
    if not INDEX_PATH.exists():
        raise Http404('Frontend not built. Run: cd frontend && pnpm run build')
    return HttpResponse(INDEX_PATH.read_bytes(), content_type='text/html')
