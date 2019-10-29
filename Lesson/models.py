from django.db import models

from Course.models import Course


class LessonMaterial(models.Model):
    """Материалы к уроку"""

    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    material1 = models.CharField(
        max_length=255,
        verbose_name='Материал 1'
    )
    material2 = models.TextField(
        verbose_name='Материал 2'
    )
    material3 = models.ImageField(
        upload_to='lesson_materials/%Y/%m/%d/',
        verbose_name='Материал 3'
    )
    material4 = models.FileField(
        upload_to='lesson_materials/%Y/%m/%d/',
        verbose_name='Материал 4'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Уроки"""

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
    courses = models.ManyToManyField(
        Course,
        related_name='lessons',
        verbose_name='Курсы'
    )
    materials = models.ManyToManyField(
        LessonMaterial,
        related_name='lessons',
        verbose_name='Материалы к уроку'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title
