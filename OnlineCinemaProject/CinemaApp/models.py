from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(
        #Movie,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Фильм"
    )
    user = models.ForeignKey(
        #User,<
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Пользователь"
    )
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Рейтинг"
    )
    cretaed_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    id_published = models.BooleanField(default=True,verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        unique_together = ('movie', 'user')
        ordering = ['-created_at']

        def __str__(self):
            return f"Отзыв от {self.user} на {self.movie}"