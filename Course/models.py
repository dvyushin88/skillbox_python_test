from django.db import models

from Direction.models import Direction


class Course(models.Model):
    """Курсы"""

    title = models.CharField(
        max_length=255,
        verbose_name='Название'
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
