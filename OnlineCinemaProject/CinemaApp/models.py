from django.db import models


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

