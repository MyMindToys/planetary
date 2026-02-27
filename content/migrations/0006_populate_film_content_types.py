# Generated manually

from django.db import migrations


def create_content_types(apps, schema_editor):
    FilmContentType = apps.get_model('content', 'FilmContentType')
    for order, name in enumerate([
        'Аттракционы',
        'Клипы',
        'Краткометражные фильмы',
    ]):
        FilmContentType.objects.get_or_create(name=name, defaults={'order': order})


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_film_content_type'),
    ]

    operations = [
        migrations.RunPython(create_content_types, noop),
    ]
