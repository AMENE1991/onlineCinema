from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    film_file = models.FileField(upload_to='films/')  # Поле для загрузки файла фильма

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Фильм"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Пользователь"
    )
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Рейтинг"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    id_published = models.BooleanField(default=True,verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        unique_together = ('movie', 'user')
        ordering = ['-created_at']

        def __str__(self):
            return f"Отзыв от {self.user} на {self.movie}"
