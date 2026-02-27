from django.urls import path
from . import views

app_name = 'content'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('news/', views.news, name='news'),
    path('zayavka/', views.zayavka, name='zayavka'),
]
