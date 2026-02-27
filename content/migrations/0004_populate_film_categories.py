# Generated manually

from django.db import migrations


def create_categories(apps, schema_editor):
    FilmCategory = apps.get_model('content', 'FilmCategory')
    for order, name in enumerate([
        'детский сад',
        'начальный класс',
        'средний класс',
        'старший класс',
    ]):
        FilmCategory.objects.get_or_create(name=name, defaults={'order': order})


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_film_genre_category_age'),
    ]

    operations = [
        migrations.RunPython(create_categories, noop),
    ]
