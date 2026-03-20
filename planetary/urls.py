"""
URL configuration for planetary project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from content.views import api_menu_cards, api_films, api_film_detail, api_catalog_filters, api_news_list, api_news_detail, api_banners

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/banners/', api_banners),
    path('api/menu-cards/', api_menu_cards),
    path('api/films/', api_films),
    path('api/films/<int:pk>/', api_film_detail),
    path('api/catalog-filters/', api_catalog_filters),
    path('api/news/', api_news_list),
    path('api/news/<int:pk>/', api_news_detail),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
