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
