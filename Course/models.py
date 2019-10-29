from django.db import models

from Direction.models import Direction


class Course(models.Model):
    """Курсы"""

    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    anons = models.TextField(
        verbose_name='Анонс'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    link_to_video = models.CharField(
        max_length=255,
        verbose_name='Ссылка на видео'
    )
    link_to_file = models.CharField(
        max_length=255,
        verbose_name='Ссылка на файл'
    )
    position = models.PositiveIntegerField(
        default=1,
        verbose_name='Позиция'
    )
    direction = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name='Направление'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        ordering = ['position']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title
