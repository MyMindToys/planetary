"""
URL configuration for planetary project.
"""
from pathlib import Path

from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from content.views import api_menu_cards, api_films, api_film_detail, api_catalog_filters, api_news_list, api_news_detail, api_banners, api_submit_zayavka
from planetary.views import spa_view

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIST = BASE_DIR / 'frontend' / 'dist'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/banners/', api_banners),
    path('api/menu-cards/', api_menu_cards),
    path('api/films/', api_films),
    path('api/films/<int:pk>/', api_film_detail),
    path('api/catalog-filters/', api_catalog_filters),
    path('api/news/', api_news_list),
    path('api/news/<int:pk>/', api_news_detail),
    path('api/zayavka/', api_submit_zayavka),
    # Собранный Vite (Render и прод на одном домене с API)
    re_path(
        r'^assets/(?P<path>.*)$',
        serve,
        {'document_root': FRONTEND_DIST / 'assets'},
    ),
    re_path(
        r'^img/(?P<path>.*)$',
        serve,
        {'document_root': FRONTEND_DIST / 'img'},
    ),
    re_path(
        r'^header_fon\.jpg$',
        serve,
        {'path': 'header_fon.jpg', 'document_root': FRONTEND_DIST},
    ),
    path('', spa_view),
    re_path(r'^catalog', spa_view),
    re_path(r'^news', spa_view),
    re_path(r'^zayavka', spa_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
