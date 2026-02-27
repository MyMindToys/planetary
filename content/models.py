from django.db import models


class Image(models.Model):
    """Изображение для загрузки через админку."""
    title = models.CharField('Название', max_length=255, blank=True)
    image = models.ImageField('Файл', upload_to='content/%Y/%m/')
    alt_text = models.CharField('Подпись (alt)', max_length=255, blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['-created_at']

    def __str__(self):
        return self.title or str(self.image)


class Genre(models.Model):
    """Жанр фильма (можно назначать несколько на один фильм)."""
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

    def __str__(self):
        return self.name


class FilmCategory(models.Model):
    """Категория аудитории: детский сад, начальный класс и т.д."""
    name = models.CharField('Название', max_length=64)
    order = models.PositiveSmallIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class FilmContentType(models.Model):
    """Тип контента: аттракционы, клипы, краткометражные фильмы."""
    name = models.CharField('Название', max_length=64)
    order = models.PositiveSmallIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Тип контента'
        verbose_name_plural = 'Типы контента'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Film(models.Model):
    """Полнокупольная программа (фильм) в каталоге."""
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True)
    duration_minutes = models.PositiveIntegerField('Длительность (мин)', default=0)
    age_rating_min = models.PositiveSmallIntegerField('Возраст от', null=True, blank=True)
    age_rating_max = models.PositiveSmallIntegerField('Возраст до', null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True, verbose_name='Жанры')
    categories = models.ManyToManyField(FilmCategory, blank=True, verbose_name='Категории')
    content_types = models.ManyToManyField(FilmContentType, blank=True, verbose_name='Тип контента')
    is_new = models.BooleanField('Новинка', default=False)
    cover = models.ImageField('Обложка', upload_to='films/%Y/%m/', blank=True, null=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['title']

    def __str__(self):
        return self.title


class News(models.Model):
    """Новость или анонс."""
    title = models.CharField('Заголовок', max_length=255)
    date = models.DateField('Дата')
    excerpt = models.TextField('Краткий текст')
    body = models.TextField('Полный текст', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    """Изображение в галерее новости (внизу поста)."""
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='gallery', verbose_name='Новость')
    image = models.ImageField('Файл', upload_to='news/%Y/%m/')
    order = models.PositiveSmallIntegerField('Порядок', default=0)
    caption = models.CharField('Подпись', max_length=255, blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        verbose_name = 'Фото в новости'
        verbose_name_plural = 'Галерея новости'
        ordering = ['order', 'pk']

    def __str__(self):
        return self.caption or str(self.image)


class MenuCard(models.Model):
    """Карточка в блоке меню на главной (4 штуки по центру)."""
    title = models.CharField('Название', max_length=255)
    image = models.ImageField('Картинка', upload_to='menu_cards/%Y/%m/', blank=True, null=True)
    link = models.CharField('Ссылка', max_length=500, blank=True, help_text='Например: /catalog или /zayavka')
    order = models.PositiveSmallIntegerField('Порядок', default=0)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Карточка меню'
        verbose_name_plural = 'Карточки меню'
        ordering = ['order']

    def __str__(self):
        return self.title


class Zayavka(models.Model):
    """Заявка на проведение мероприятия."""
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Телефон', max_length=64)
    email = models.EmailField('Email', blank=True)
    desired_date = models.DateField('Желаемая дата', null=True, blank=True)
    message = models.TextField('Сообщение', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.created_at:%d.%m.%Y}'
