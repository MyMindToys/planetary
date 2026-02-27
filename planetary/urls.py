"""
URL configuration for planetary project.
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from pathlib import Path

from . import views as planetary_views

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIST = BASE_DIR / 'frontend' / 'dist'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': str(FRONTEND_DIST / 'assets')}),
    path('', planetary_views.spa_view),
    path('catalog/', planetary_views.spa_view),
    path('news/', planetary_views.spa_view),
    path('zayavka/', planetary_views.spa_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
