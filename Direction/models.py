from django.db import models


class Direction(models.Model):
    """Направления"""

    title = models.CharField(
        max_length=255,
        verbose_name='Направление'
    )
    position = models.PositiveIntegerField(
        default=1,
        verbose_name='Позиция'
    )

    class Meta:
        ordering = ['position']
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.title
