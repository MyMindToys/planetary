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


class Film(models.Model):
    """Полнокупольная программа (фильм) в каталоге."""
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True)
    duration_minutes = models.PositiveIntegerField('Длительность (мин)', default=0)
    age_rating = models.CharField('Возраст', max_length=32, blank=True)
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
