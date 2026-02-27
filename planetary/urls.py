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
from content.views import api_menu_cards

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIST = BASE_DIR / 'frontend' / 'dist'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menu-cards/', api_menu_cards),
    re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': str(FRONTEND_DIST / 'assets')}),
    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': str(FRONTEND_DIST / 'img')}),
    re_path(r'^(?P<path>header_fon\.jpg)$', serve, {'document_root': str(FRONTEND_DIST)}),
    path('', planetary_views.spa_view),
    path('catalog/', planetary_views.spa_view),
    path('news/', planetary_views.spa_view),
    path('zayavka/', planetary_views.spa_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
