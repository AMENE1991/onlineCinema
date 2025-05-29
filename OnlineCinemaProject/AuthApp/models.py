from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Reviews(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="фильм"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="пользователь"
    )
    text = models.TextField(verbose_name="Текст коментария")
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Рейтинг"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        uique_together = ('movie', 'user')
        ordering = ['-created_at']

        def __str__(self):
            return f"Отзыв от {self.user} на {self.movie}"

